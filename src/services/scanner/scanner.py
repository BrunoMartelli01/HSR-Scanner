import asyncio
import time

import pyautogui
import win32gui
from PIL import Image as PILImage
from pynput.keyboard import Key
from PyQt6.QtCore import QObject, QSettings, pyqtSignal

from config.character_scan import CHARACTER_NAV_DATA
from enums.increment_type import IncrementType
from enums.log_level import LogLevel
from enums.scan_mode import ScanMode
from models.game_data import GameData
from utils.data import resource_path
from utils.navigation import Navigation
from utils.ocr import image_to_string, preprocess_char_count_img, preprocess_uid_img
from utils.screenshot import Screenshot
from utils.window import bring_window_to_foreground

from .parsers.character_parser import CharacterParser
from .parsers.light_cone_strategy import LightConeStrategy
from .parsers.relic_strategy import RelicStrategy

SUPPORTED_ASPECT_RATIOS = ["16:9"]


class InterruptedScanException(Exception):
    """Exception raised when the scan is interrupted"""

    pass


class HSRScanner(QObject):
    """HSRScanner class is responsible for scanning the game for light cones, relics, and characters"""

    update_signal = pyqtSignal(int)
    log_signal = pyqtSignal(object)
    complete_signal = pyqtSignal()

    def __init__(self, config: dict, game_data: GameData, scan_mode: int = 0):
        """Constructor

        :param config: The config dict
        :param game_data: The GameData class instance
        :raises Exception: Thrown if the game is not found
        :raises Exception: Thrown if no scan options are selected
        """
        super().__init__()
        for i, game_name in enumerate(
            [
                "Honkai: Star Rail",
                "崩坏：星穹铁道",
                "崩壞：星穹鐵道",
                "붕괴:\u00A0스타레일",
                "崩壊：スターレイル",
                "Honkai\u00A0: Star Rail",
            ]
        ):
            self._hwnd = win32gui.FindWindow("UnityWndClass", game_name)
            if self._hwnd:
                self._is_en = i == 0
                break
        if not self._hwnd:
            raise Exception(
                "Honkai: Star Rail not found. Please open the game and try again."
            )
        self._config = config
        self._game_data = game_data
        self._scan_mode = scan_mode

        self._nav = Navigation(self._hwnd)

        self._aspect_ratio = self._nav.get_aspect_ratio()
        if self._aspect_ratio not in SUPPORTED_ASPECT_RATIOS:
            raise Exception(
                f"Aspect ratio {self._aspect_ratio} not supported. Supported aspect ratios: {SUPPORTED_ASPECT_RATIOS}"
            )

        self._screenshot = Screenshot(
            self._hwnd,
            self.log_signal,
            self._aspect_ratio,
            config["debug"],
            config["debug_output_location"],
        )
        self._databank_img = PILImage.open(resource_path("assets/images/databank.png"))

        self._interrupt_event = asyncio.Event()

    async def start_scan(self) -> dict:
        """Starts the scan

        :raises InterruptedScanException: Thrown if the scan is interrupted
        :return: The scan results
        """
        self._log("Config: " + str(self._config), LogLevel.DEBUG)

        if not self._is_en:
            self._log(
                "Non-English game name detected. The scanner only works with English text.",
                LogLevel.WARNING,
            )
        bring_window_to_foreground(self._hwnd)

        uid = None
        if self._config["include_uid"] and not self._interrupt_event.is_set():
            self._nav_sleep(1)
            uid_img = self._screenshot.screenshot_uid()
            uid = image_to_string(uid_img, "0123456789", 7, False, preprocess_uid_img)[
                :9
            ]
            if len(uid) != 9:
                uid = image_to_string(
                    uid_img, "0123456789", 7, True, preprocess_uid_img
                )[:9]
            if len(uid) != 9:
                self._log(f"Failed to parse UID. Got '{uid}' instead.", LogLevel.ERROR)
                uid = None
            else:
                self._log(f"UID: {uid}.")

        light_cones = []
        if self._config["scan_light_cones"] and not self._interrupt_event.is_set():
            self._log("Scanning light cones...")
            light_cones = self.scan_inventory(
                LightConeStrategy(
                    self._game_data,
                    self.log_signal,
                    self.update_signal,
                    self._interrupt_event,
                    self._config["debug"],
                )
            )
            (
                self._log("Finished scanning light cones.")
                if not self._interrupt_event.is_set()
                else None
            )

        relics = []
        if self._config["scan_relics"] and not self._interrupt_event.is_set():
            self._log("Scanning relics...")
            relics = await self.scan_inventory(
                RelicStrategy(
                    self._game_data,
                    self.log_signal,
                    self.update_signal,
                    self._interrupt_event,
                    self._config["debug"],
                )
            )
            (
                self._log("Finished scanning relics.")
                if not self._interrupt_event.is_set()
                else None
            )

        characters = []
        if self._config["scan_characters"] and not self._interrupt_event.is_set():
            self._log("Scanning characters...")
            characters = self.scan_characters()
            (
                self._log("Finished scanning characters.")
                if not self._interrupt_event.is_set()
                else None
            )

        if self._interrupt_event.is_set():
            await asyncio.gather(*light_cones, *relics, *characters)
            return

        self.complete_signal.emit()
        self._log("Starting OCR process. Please wait...")

        return {
            "source": "HSR-Scanner",
            "build": "v1.0.0",
            "version": 3,
            "metadata": {
                "uid": int(uid) if uid else None,
                "trailblazer": (
                    "Stelle"
                    if QSettings("kel-z", "HSR-Scanner").value("is_stelle", True)
                    == "true"
                    else "Caelus"
                ),
            },
            "light_cones": await asyncio.gather(*light_cones),
            "relics": await asyncio.gather(*relics),
            "characters": await asyncio.gather(*characters),
        }

    def stop_scan(self) -> None:
        """Stops the scan"""
        self._interrupt_event.set()

    async def scan_inventory(
        self, strategy: LightConeStrategy | RelicStrategy
    ) -> set[asyncio.Task]:
        """Scans the inventory for light cones or relics

        :param strategy: The strategy to use
        :raises InterruptedScanException: Thrown if the scan is interrupted
        :raises ValueError: Thrown if the quantity could not be parsed
        :return: The tasks to await
        """
        nav_data = strategy.NAV_DATA[self._aspect_ratio]

        # Navigate to correct tab from cellphone menu
        self._nav_sleep(1)
        self._nav.key_tap(Key.esc)
        self._nav_sleep(2)
        self._nav.key_tap(self._config["inventory_key"])
        self._nav_sleep(1.5)

        # Get quantity
        max_retry = 5
        retry = 0
        while True:
            self._nav.move_cursor_to(*nav_data["inv_tab"])
            time.sleep(0.05)
            self._nav.click()
            self._nav_sleep(1.5)

            # TODO: using quantity to know when to scan the bottom row is not ideal
            #       because it will not work for tabs that do not have a quantity
            #       (i.e. materials).
            #
            #       for now, it will work for light cones and relics.
            quantity = self._screenshot.screenshot_quantity()
            quantity = image_to_string(quantity, "0123456789/", 7)

            try:
                self._log(f"Quantity: {quantity}.")
                quantity = quantity_remaining = int(quantity.split("/")[0])
                break
            except ValueError:
                retry += 1
                if retry > max_retry:
                    raise ValueError(
                        "Failed to parse quantity from inventory screen."
                        + (f' Got "{quantity}" instead.' if quantity else "")
                    )
                else:
                    self._log(
                        f"Failed to parse quantity. Retrying... ({retry}/{max_retry})",
                        LogLevel.WARNING,
                    )
                self._nav_sleep(1)

        current_sort_method = image_to_string(
            self._screenshot.screenshot_sort(), "RarityLvDate obtained", 7
        )
        optimal_sort_method = "Date obtained"
        if self._scan_mode != ScanMode.RECENT_RELICS.value:
            optimal_sort_method = strategy.get_optimal_sort_method(
                self._config["filters"]
            )

        if optimal_sort_method != current_sort_method:
            self._log(f"Sorting by {optimal_sort_method} (was {current_sort_method}).")
            self._nav.move_cursor_to(*nav_data["sort"]["button"])
            time.sleep(0.05)
            self._nav.click()
            self._nav_sleep(0.5)
            self._nav.move_cursor_to(*nav_data["sort"][optimal_sort_method])
            self._nav.click()
            current_sort_method = optimal_sort_method
            self._nav_sleep(0.5)

        tasks = set()
        scanned_per_scroll = nav_data["rows"] * nav_data["cols"]
        num_times_scrolled = 0
        scanned = 0

        def should_stop():
            if self._scan_mode == ScanMode.RECENT_RELICS.value:
                return (
                    quantity_remaining <= 0
                    or scanned >= self._config["recent_relics_num"]
                )
            return quantity_remaining <= 0

        while not should_stop():
            if (
                quantity_remaining <= scanned_per_scroll
                and not quantity <= scanned_per_scroll
            ):
                x, y = nav_data["row_start_bottom"]
                todo_rows = self._ceildiv(quantity_remaining, nav_data["cols"]) - 1
                y -= todo_rows * nav_data["offset_y"]
            else:
                x, y = nav_data["row_start_top"]

            for _ in range(nav_data["rows"]):
                for _ in range(nav_data["cols"]):
                    if should_stop():
                        break

                    # Next item
                    self._nav.move_cursor_to(x, y)
                    time.sleep(0.05)
                    self._nav.click()
                    self._scan_sleep(0.1)
                    quantity_remaining -= 1

                    # Get stats
                    stats_dict = self._screenshot.screenshot_stats(strategy.SCAN_TYPE)
                    item_id = quantity - quantity_remaining
                    x += nav_data["offset_x"]

                    # Check if item satisfies filters
                    if "filters" in self._config:
                        filter_results, stats_dict = strategy.check_filters(
                            stats_dict,
                            self._config["filters"],
                            item_id,
                        )
                        if (
                            current_sort_method == "Lv"
                            and "min_level" in filter_results
                            and not filter_results["min_level"]
                        ):
                            quantity_remaining = 0
                            self._log(
                                f"Reached minimum level filter (got level {stats_dict['level']})."
                            )
                            break
                        if (
                            current_sort_method == "Rarity"
                            and "min_rarity" in filter_results
                            and not filter_results["min_rarity"]
                        ):
                            quantity_remaining = 0
                            self._log(
                                f"Reached minimum rarity filter (got rarity {stats_dict['rarity']})."
                            )
                            break
                        if (
                            self._scan_mode == ScanMode.RECENT_RELICS.value
                            and current_sort_method == "Date obtained"
                            and "min_rarity" in filter_results
                            and filter_results["min_rarity"]
                        ):
                            scanned += 1
                        if not all(filter_results.values()):
                            continue

                    # Update UI count
                    self.update_signal.emit(strategy.SCAN_TYPE.value)




                    critRate = {1: [2.592, 2.916, 3.24],
                                2: [5.184, 5.508, 5.832000000000001, 5.832, 6.156000000000001, 6.48],
                                3: [7.776, 8.1, 8.424, 8.424, 8.748000000000001, 9.072000000000001, 8.748, 9.072, 9.396,
                                    9.72],
                                4: [10.368, 10.692, 11.016, 11.016, 11.34, 11.664, 11.34, 11.664, 11.988000000000001,
                                    12.312000000000001, 11.664, 11.988, 12.312, 12.636000000000001, 12.96],
                                5: [12.96, 13.284, 13.608, 13.608, 13.932, 14.256, 13.932, 14.256, 14.58, 14.904,
                                    14.256, 14.58, 14.904, 15.228000000000002, 15.552000000000001, 14.58, 14.904,
                                    15.228, 15.552, 15.876000000000001, 16.200000000000003],
                                6: [15.552000000000001, 15.876000000000001, 16.200000000000003, 16.2, 16.524, 16.848,
                                    16.524, 16.848, 17.172, 17.496000000000002, 16.848, 17.172, 17.496000000000002,
                                    17.82, 18.144, 17.172, 17.496000000000002, 17.82, 18.144, 18.468000000000004,
                                    18.792, 17.496, 17.82, 18.144, 18.468, 18.792, 19.116, 19.440000000000005]}
                    dmg = {1: [5.184, 5.832, 6.48],
                           2: [10.368, 11.016, 11.664000000000001, 11.664, 12.312000000000001, 12.96],
                           3: [15.552, 16.2, 16.848, 16.848, 17.496000000000002, 18.144000000000002, 17.496, 18.144,
                               18.792, 19.44],
                           4: [20.736, 21.384, 22.032, 22.032, 22.68, 23.328, 22.68, 23.328, 23.976000000000003,
                               24.624000000000002, 23.328, 23.976, 24.624, 25.272000000000002, 25.92],
                           5: [25.92, 26.568, 27.216, 27.216, 27.864, 28.512, 27.864, 28.512, 29.16, 29.808, 28.512,
                               29.16, 29.808, 30.456000000000003, 31.104000000000003, 29.16, 29.808, 30.456, 31.104,
                               31.752000000000002, 32.400000000000006],
                           6: [31.104000000000003, 31.752000000000002, 32.400000000000006, 32.4, 33.048, 33.696, 33.048,
                               33.696, 34.344, 34.992000000000004, 33.696, 34.344, 34.992000000000004, 35.64, 36.288,
                               34.344, 34.992000000000004, 35.64, 36.288, 36.93600000000001, 37.584, 34.992, 35.64,
                               36.288, 36.936, 37.584, 38.232, 38.88000000000001]}
                    effectHpAtk = {1: [3.456, 3.888, 4.32], 2: [6.912, 7.343999999999999, 7.776, 7.776, 8.208, 8.64],
                                   3: [10.368, 10.8, 11.232, 11.232, 11.664, 12.096, 11.664, 12.096, 12.528, 12.96],
                                   4: [13.824, 14.256, 14.688, 14.688, 15.120000000000001, 15.552, 15.12, 15.552,
                                       15.984, 16.416, 15.552, 15.984, 16.416, 16.848, 17.28],
                                   5: [17.28, 17.712, 18.144, 18.144, 18.576, 19.008000000000003, 18.576,
                                       19.008000000000003, 19.44, 19.872, 19.008, 19.439999999999998, 19.872,
                                       20.304000000000002, 20.736, 19.439999999999998, 19.872, 20.304000000000002,
                                       20.736, 21.168, 21.6],
                                   6: [20.736, 21.168, 21.6, 21.6, 22.032, 22.464, 22.031999999999996, 22.464, 22.896,
                                       23.328000000000003, 22.464, 22.896, 23.328000000000003, 23.76, 24.192, 22.896,
                                       23.328, 23.759999999999998, 24.192, 24.624000000000002, 25.056,
                                       23.327999999999996, 23.759999999999998, 24.192, 24.624000000000002, 25.056,
                                       25.488, 25.92]}
                    dif = {1: [4.32, 4.86, 5.4], 2: [8.64, 9.18, 9.72, 9.72, 10.260000000000002, 10.8],
                           3: [12.96, 13.5, 14.040000000000001, 14.04, 14.58, 15.120000000000001, 14.580000000000002,
                               15.120000000000001, 15.660000000000002, 16.200000000000003],
                           4: [17.28, 17.82, 18.36, 18.36, 18.9, 19.44, 18.9, 19.439999999999998, 19.98,
                               20.520000000000003, 19.44, 19.980000000000004, 20.520000000000003, 21.060000000000002,
                               21.6],
                           5: [21.6, 22.14, 22.68, 22.68, 23.22, 23.759999999999998, 23.22, 23.759999999999998,
                               24.299999999999997, 24.840000000000003, 23.759999999999998, 24.299999999999997,
                               24.839999999999996, 25.380000000000003, 25.92, 24.3, 24.840000000000003,
                               25.380000000000003, 25.92, 26.46, 27.0],
                           6: [25.92, 26.46, 27.0, 27.0, 27.54, 28.08, 27.54, 28.08, 28.619999999999997,
                               29.159999999999997, 28.08, 28.619999999999997, 29.159999999999997, 29.699999999999996,
                               30.240000000000002, 28.619999999999997, 29.159999999999997, 29.699999999999996,
                               30.239999999999995, 30.78, 31.32, 29.16, 29.700000000000003, 30.240000000000002, 30.78,
                               31.32, 31.86, 32.4]}
                    spd = {1: [2, 2.3, 2.6], 2: [4, 4.3, 4.6, 4.6, 4.9, 5.2],
                           3: [6, 6.3, 6.6, 6.6, 6.9, 7.199999999999999, 6.8999999999999995, 7.199999999999999, 7.5,
                               7.800000000000001],
                           4: [8, 8.3, 8.6, 8.6, 8.9, 9.2, 8.899999999999999, 9.2, 9.5, 9.799999999999999, 9.2, 9.5,
                               9.799999999999999, 10.1, 10.4],
                           5: [10, 10.3, 10.6, 10.600000000000001, 10.9, 11.2, 10.899999999999999, 11.2, 11.5,
                               11.799999999999999, 11.2, 11.499999999999998, 11.799999999999999, 12.1,
                               12.399999999999999, 11.5, 11.799999999999999, 12.1, 12.399999999999999, 12.7, 13.0],
                           6: [12, 12.3, 12.6, 12.600000000000001, 12.9, 13.2, 12.900000000000002, 13.200000000000001,
                               13.5, 13.799999999999999, 13.2, 13.499999999999998, 13.799999999999999, 14.1,
                               14.399999999999999, 13.5, 13.799999999999999, 14.099999999999998, 14.399999999999999,
                               14.7, 14.999999999999998, 13.8, 14.1, 14.399999999999999, 14.7, 14.999999999999998,
                               15.299999999999999, 15.6]}
                    difAtkFlat = {1: [16, 19, 21], 2: [33, 35, 38, 38, 40, 42],
                                  3: [50, 52, 55, 55, 57, 59, 57, 59, 61, 63],
                                  4: [67, 69, 71, 71, 74, 76, 74, 76, 78, 80, 76, 78, 80, 82, 84],
                                  5: [84, 86, 88, 88, 91, 93, 91, 93, 95, 97, 93, 95, 97, 99, 101, 95, 97, 99, 101, 103,
                                      105],
                                  6: [101, 103, 105, 105, 107, 110, 107, 110, 112, 114, 110, 112, 114, 116, 118, 112,
                                      114, 116, 118, 120, 122, 114, 116, 118, 120, 122, 124, 127]}
                    hpFlat = {1: [33, 38, 42], 2: [67, 71, 76, 76, 80, 84],
                              3: [101, 105, 110, 110, 114, 118, 114, 118, 122, 127],
                              4: [135, 139, 143, 143, 148, 152, 148, 152, 156, 160, 152, 156, 160, 165, 169],
                              5: [169, 173, 177, 177, 182, 186, 182, 186, 190, 194, 186, 190, 194, 198, 203, 190, 194,
                                  198, 203, 207, 211],
                              6: [203, 207, 211, 211, 215, 220, 215, 220, 224, 228, 220, 224, 228, 232, 237, 224, 228,
                                  232, 237, 241, 245, 228, 232, 237, 241, 245, 249, 254]}

                    subsatlevel = {"HP": hpFlat, "ATK": difAtkFlat, "DEF": difAtkFlat, "CRIT Rate_": critRate,
                                   "CRIT DMG_": dmg, "SPD": spd, "HP_": effectHpAtk, "ATK_": effectHpAtk, "DEF_": dif,
                                   "Break Effect_": dmg, "Effect Hit Rate_": effectHpAtk, "Effect RES_": effectHpAtk, }





                    task = asyncio.to_thread(strategy.parse, stats_dict, item_id)
                    relic = await task

                    print(relic["level"])


                    pos = self._nav.get_mouse_position()

                    if relic["level"] == 15:
                        substats = relic["substats"]
                        print(substats)
                        for i in range(len(substats)):
                            level = subsatlevel[substats[i]["key"]]
                            for k in range(1, 7):
                                for j in range(len(level[k])):
                                    if abs(level[k][j] - substats[i]["value"]) < 0.1:
                                        print(substats[i]["key"], substats[i]["value"], k)
                                        break
                        print("-------------")
                    # self._nav.move_cursor_to(0.945, 0.29)
                    # time.sleep(0.05)
                    # self._nav.click()
                    # self._scan_sleep(0.1)
                    # self._nav.move_cursor_to(*pos)



                tasks.add(task)

                # Next row
                x = nav_data["row_start_top"][0]
                y += nav_data["offset_y"]

            if should_stop():
                break

            self._nav.scroll_page_down(num_times_scrolled)
            num_times_scrolled += 1
            self._log(
                f"Scrolling inventory, page {num_times_scrolled + 1}.", LogLevel.TRACE
            )

            self._scan_sleep(0.5)

        self._nav.key_tap(Key.esc)
        self._nav_sleep(2)
        self._nav.key_tap(Key.esc)
        self._nav_sleep(1)
        return tasks

    def scan_characters(self) -> set[asyncio.Task]:
        """Scans the characters

        :raises InterruptedScanException: Thrown if the scan is interrupted
        :raises ValueError: Thrown if the character count could not be parsed
        :return: The tasks to await
        """
        char_parser = CharacterParser(
            self._game_data,
            self.log_signal,
            self.update_signal,
            self._interrupt_event,
            self._config["debug"],
        )
        nav_data = CHARACTER_NAV_DATA[self._aspect_ratio]

        # Assume ESC menu is open
        bring_window_to_foreground(self._hwnd)
        self._nav_sleep(1)

        # Locate and click databank button
        self._log("Locating Data Bank button...", LogLevel.DEBUG)
        haystack = self._screenshot.screenshot_screen()
        needle = self._databank_img.resize(
            # Scale image to match capture size
            (
                int(haystack.size[0] * 0.0296875),
                int(haystack.size[1] * 0.05625),
            )
        )
        self._nav.move_cursor_to_image(haystack, needle)
        self._log(
            f"Data Bank button found at {self._nav.get_mouse_position()}.",
            LogLevel.DEBUG,
        )
        time.sleep(0.05)
        self._nav.click()
        self._nav_sleep(1)

        # Get character count
        max_retry = 5
        retry = 0
        while True:
            character_total = self._screenshot.screenshot_character_count()
            character_total = image_to_string(
                character_total, "0123456789/", 7, True, preprocess_char_count_img
            )
            try:
                self._log(f"Character total: {character_total}.")
                character_total = character_total.split("/")[0]
                character_count = character_total = int(character_total)
                break
            except ValueError:
                retry += 1
                if retry > max_retry:
                    raise ValueError(
                        "Failed to parse character count from Data Bank screen."
                        + (
                            f' Got "{character_total}" instead.'
                            if character_total
                            else ""
                        )
                    )
                else:
                    self._log(
                        f"Failed to parse character count. Retrying... ({retry}/{max_retry})",
                        LogLevel.WARNING,
                    )
                self._nav_sleep(1)

        # Navigate to characters menu
        self._nav.key_tap(Key.esc)
        self._nav_sleep(1)
        self._nav.key_tap(Key.esc)
        self._nav_sleep(1.5)
        self._nav.key_tap("1")
        self._nav_sleep(0.2)
        self._nav.key_tap(self._config["characters_key"])
        self._nav_sleep(1)

        tasks = set()
        characters_seen = set()
        while character_count > 0:
            if character_count > nav_data["chars_per_scan"]:
                character_x, character_y = nav_data["char_start"]
            else:
                character_x, character_y = nav_data["char_end"]
                character_x -= nav_data["offset_x"] * (character_count - 1)

            i_stop = min(character_count, nav_data["chars_per_scan"])
            curr_page_res = [{} for _ in range(i_stop)]

            # Details tab
            i = 0
            self._nav.move_cursor_to(*nav_data["details_button"])
            time.sleep(0.05)
            self._nav.click()
            self._nav_sleep(0.5)
            prev_trailblazer = False  # https://github.com/kel-z/HSR-Scanner/issues/49#issuecomment-1936613741
            while i < i_stop:
                self._nav.move_cursor_to(
                    character_x + i * nav_data["offset_x"], character_y
                )
                time.sleep(0.05)
                self._nav.click()
                self._scan_sleep(0.3)

                # Get name and path
                character_name = ""
                max_retry = 5
                retry = 0
                while retry < max_retry and (
                    not character_name or character_name in characters_seen
                ):
                    try:
                        (self._scan_sleep(0.7) if prev_trailblazer else None)
                        character_name = (
                            # this has a small delay, can basically be treated as a sleep
                            self._get_character_name()
                        )
                        character_img = self._screenshot.screenshot_character()

                        # Trailblazer is the most prone to errors, need to ensure
                        # that all the elements have loaded before taking screenshots
                        # at the cost of small delay on Trailblazer
                        is_trailblazer = char_parser.is_trailblazer(character_img)
                        if is_trailblazer:
                            self._scan_sleep(0.7)
                            character_name = self._get_character_name()

                        path, character_name = map(
                            str.strip, character_name.split("/")[:2]
                        )
                        character_name, path = char_parser.get_closest_name_and_path(
                            character_name, path, is_trailblazer
                        )

                        if character_name in characters_seen:
                            self._log(
                                f"Parsed duplicate character '{character_name}'. Retrying... ({retry + 1}/{max_retry})",
                                LogLevel.WARNING,
                            )
                            self._scan_sleep(1)
                    except Exception as e:
                        self._log(
                            f"Failed to parse character name. Got error: {e}. Retrying... ({retry + 1}/{max_retry})",
                            LogLevel.WARNING,
                        )
                        character_name = ""
                        self._scan_sleep(1)
                    retry += 1

                if not character_name:
                    self._log(
                        f"Failed to parse character name. Got '{character_name}' instead. Ending scan early.",
                        LogLevel.ERROR,
                    )
                    return tasks

                if character_name in characters_seen:
                    self._log(
                        f"Duplicate character '{path} / {character_name}' scanned. Continuing scan anyway.",
                        LogLevel.ERROR,
                    )
                else:
                    characters_seen.add(character_name)
                    self._log(
                        f"Character {i + 1}: {path} / {character_name}", LogLevel.TRACE
                    )
                prev_trailblazer = character_name.startswith("Trailblazer")

                # Get ascension by counting ascension stars
                ascension_pos = nav_data["ascension_start"]
                ascension = 0
                for _ in range(6):
                    pixel = pyautogui.pixel(
                        *self._nav.translate_percent_to_coords(*ascension_pos)
                    )
                    dist = sum([(a - b) ** 2 for a, b in zip(pixel, (255, 222, 152))])
                    if dist > 100:
                        break

                    ascension += 1
                    ascension_pos = (
                        ascension_pos[0] + nav_data["ascension_offset_x"],
                        ascension_pos[1],
                    )

                curr_page_res[i] = {
                    "name": character_name,
                    "ascension": ascension,
                    "path": path,
                    "level": self._screenshot.screenshot_character_level(),
                }

                # Check if character satisfies level filter
                min_level = self._config["filters"]["character"].get("min_level", 1)
                if min_level > 1:
                    curr_page_res[i]["level"] = character_level = char_parser.get_level(
                        curr_page_res[i]["level"]
                    )
                    if (
                        character_level < min_level
                        and character_total - character_count < 4
                    ):
                        self._log(
                            f"{character_name} is below minimum level filter (got level {character_level}). Skipping...",
                            LogLevel.TRACE,
                        )
                        curr_page_res[i] = {}
                        i += 1
                        continue
                    elif character_level < min_level:
                        self._log(
                            f"Reached minimum level filter (got level {character_level} for {character_name}).",
                        )
                        character_count = 0
                        i_stop = i
                        curr_page_res = curr_page_res[:i]
                        break

                # Update UI count
                self.update_signal.emit(IncrementType.CHARACTER_ADD.value)
                i += 1

            self._log(
                f"Page {self._ceildiv(len(characters_seen), nav_data['chars_per_scan'])}: {', '.join([c['name'] for c in curr_page_res if c])}",
                LogLevel.TRACE,
            )

            # Traces tab
            i = 0
            self._nav.move_cursor_to(*nav_data["traces_button"])
            time.sleep(0.05)
            self._nav.click()
            self._nav_sleep(0.4)
            while i < i_stop:
                if not curr_page_res[i]:
                    i += 1
                    continue
                self._nav.move_cursor_to(
                    character_x + i * nav_data["offset_x"], character_y
                )
                time.sleep(0.05)
                self._nav.click()
                self._scan_sleep(0.6)
                path_key = curr_page_res[i]["path"].split(" ")[-1].lower()
                traces_dict = self._screenshot.screenshot_character_traces(path_key)
                curr_page_res[i]["traces"] = {
                    "levels": traces_dict,
                    "unlocks": {},
                }
                for k, v in nav_data["traces"][path_key].items():
                    # Trace is unlocked if pixel is white
                    pixel = pyautogui.pixel(*self._nav.translate_percent_to_coords(*v))
                    dist = min(
                        sum([(a - b) ** 2 for a, b in zip(pixel, (255, 255, 255))]),
                        sum([(a - b) ** 2 for a, b in zip(pixel, (178, 200, 255))]),
                    )
                    curr_page_res[i]["traces"]["unlocks"][k] = dist < 3000
                i += 1

            # Eidolons tab
            i = 0
            self._nav.move_cursor_to(*nav_data["eidolons_button"])
            time.sleep(0.05)
            self._nav.click()
            self._nav_sleep(1.5 if character_total == character_count else 0.9)
            while i < i_stop:
                if not curr_page_res[i]:
                    i += 1
                    continue
                self._nav.move_cursor_to(
                    character_x + i * nav_data["offset_x"], character_y
                )
                time.sleep(0.05)
                self._nav.click()
                self._scan_sleep(0.5)
                curr_page_res[i][
                    "eidolon_images"
                ] = self._screenshot.screenshot_character_eidolons()
                i += 1

            for stats_dict in curr_page_res:
                character_count -= 1
                if not stats_dict:
                    continue
                task = asyncio.to_thread(char_parser.parse, stats_dict)
                tasks.add(task)

            # Drag to next page
            if character_count > 0:
                character_x, character_y = nav_data["char_start"]
                character_x += nav_data["offset_x"] * nav_data["chars_per_scan"]
                self._nav.move_cursor_to(character_x, character_y)
                time.sleep(0.05)
                self._nav.click()
                time.sleep(0.05)
                self._nav.drag_scroll(
                    character_x,
                    character_y,
                    nav_data["char_start"][0] - 0.031,
                    character_y,
                )

        self._nav_sleep(1)
        self._nav.key_tap(Key.esc)
        self._nav_sleep(2)
        self._nav.key_tap(Key.esc)
        self._nav_sleep(1)
        return tasks

    def _log(self, msg: str, level: LogLevel = LogLevel.INFO) -> None:
        """Logs a message

        :param msg: The message to log
        :param level: The log level
        """
        if self._config["debug"] or level in [
            LogLevel.INFO,
            LogLevel.WARNING,
            LogLevel.ERROR,
        ]:
            self.log_signal.emit((msg, level))

    def _get_character_name(self) -> str:
        """Gets the character name

        :return: The character name
        """
        character_name_img = self._screenshot.screenshot_character_name()
        return image_to_string(
            character_name_img,
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz/7&",
            7,
        )

    def _nav_sleep(self, seconds: float) -> None:
        """Sleeps for the specified amount of time with navigation delay

        :param seconds: The amount of time to sleep
        :raises InterruptedScanException: Thrown if the scan is interrupted
        """
        time.sleep(seconds + self._config["nav_delay"])
        if self._interrupt_event.is_set():
            raise InterruptedScanException()

    def _scan_sleep(self, seconds: float) -> None:
        """Sleeps for the specified amount of time with scan delay

        :param seconds: The amount of time to sleep
        :raises InterruptedScanException: Thrown if the scan is interrupted
        """
        time.sleep(seconds + self._config["scan_delay"])
        if self._interrupt_event.is_set():
            raise InterruptedScanException()

    def _ceildiv(self, a, b) -> int:
        """Divides a by b and rounds up

        :param a: The dividend
        :param b: The divisor
        :return: The quotient
        """
        return -(a // -b)
