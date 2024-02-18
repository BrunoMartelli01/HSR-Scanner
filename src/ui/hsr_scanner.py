# Form implementation generated from reading ui file 'hsr_scanner.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 450))
        MainWindow.setMaximumSize(QtCore.QSize(700, 450))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 431))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Scan = QtWidgets.QWidget()
        self.Scan.setObjectName("Scan")
        self.formGroupBox = QtWidgets.QGroupBox(parent=self.Scan)
        self.formGroupBox.setGeometry(QtCore.QRect(10, 10, 151, 101))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxScanLightCones = QtWidgets.QCheckBox(parent=self.formGroupBox)
        self.checkBoxScanLightCones.setObjectName("checkBoxScanLightCones")
        self.verticalLayout.addWidget(self.checkBoxScanLightCones)
        self.checkBoxScanRelics = QtWidgets.QCheckBox(parent=self.formGroupBox)
        self.checkBoxScanRelics.setObjectName("checkBoxScanRelics")
        self.verticalLayout.addWidget(self.checkBoxScanRelics)
        self.checkBoxScanChars = QtWidgets.QCheckBox(parent=self.formGroupBox)
        self.checkBoxScanChars.setEnabled(True)
        self.checkBoxScanChars.setObjectName("checkBoxScanChars")
        self.verticalLayout.addWidget(self.checkBoxScanChars)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verticalLayout)
        self.pushButtonStartScan = QtWidgets.QPushButton(parent=self.Scan)
        self.pushButtonStartScan.setEnabled(False)
        self.pushButtonStartScan.setGeometry(QtCore.QRect(10, 350, 111, 41))
        self.pushButtonStartScan.setObjectName("pushButtonStartScan")
        self.groupBox = QtWidgets.QGroupBox(parent=self.Scan)
        self.groupBox.setGeometry(QtCore.QRect(270, 210, 151, 91))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_23 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_24)
        self.label_25 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_25)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLightConeProcessed = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelLightConeProcessed.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelLightConeProcessed.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelLightConeProcessed.setObjectName("labelLightConeProcessed")
        self.horizontalLayout_2.addWidget(self.labelLightConeProcessed)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.labelLightConeCount = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelLightConeCount.setObjectName("labelLightConeCount")
        self.horizontalLayout_2.addWidget(self.labelLightConeCount)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelRelicProcessed = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelRelicProcessed.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelRelicProcessed.setObjectName("labelRelicProcessed")
        self.horizontalLayout_3.addWidget(self.labelRelicProcessed)
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.labelRelicCount = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelRelicCount.setObjectName("labelRelicCount")
        self.horizontalLayout_3.addWidget(self.labelRelicCount)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelCharacterProcessed = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelCharacterProcessed.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelCharacterProcessed.setObjectName("labelCharacterProcessed")
        self.horizontalLayout_4.addWidget(self.labelCharacterProcessed)
        self.label_14 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.labelCharacterCount = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelCharacterCount.setObjectName("labelCharacterCount")
        self.horizontalLayout_4.addWidget(self.labelCharacterCount)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.Scan)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 10, 251, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 111, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.spinBoxLightConeMinRarity = QtWidgets.QSpinBox(parent=self.formLayoutWidget_2)
        self.spinBoxLightConeMinRarity.setEnabled(True)
        self.spinBoxLightConeMinRarity.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxLightConeMinRarity.setMinimum(3)
        self.spinBoxLightConeMinRarity.setMaximum(5)
        self.spinBoxLightConeMinRarity.setProperty("value", 3)
        self.spinBoxLightConeMinRarity.setObjectName("spinBoxLightConeMinRarity")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBoxLightConeMinRarity)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.spinBoxLightConeMinLevel = QtWidgets.QSpinBox(parent=self.formLayoutWidget_2)
        self.spinBoxLightConeMinLevel.setEnabled(True)
        self.spinBoxLightConeMinLevel.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxLightConeMinLevel.setMinimum(1)
        self.spinBoxLightConeMinLevel.setMaximum(80)
        self.spinBoxLightConeMinLevel.setObjectName("spinBoxLightConeMinLevel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBoxLightConeMinLevel)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(130, 20, 111, 71))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.spinBoxRelicMinRarity = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBoxRelicMinRarity.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxRelicMinRarity.setMinimum(2)
        self.spinBoxRelicMinRarity.setMaximum(5)
        self.spinBoxRelicMinRarity.setProperty("value", 2)
        self.spinBoxRelicMinRarity.setObjectName("spinBoxRelicMinRarity")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBoxRelicMinRarity)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_8)
        self.spinBoxRelicMinLevel = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBoxRelicMinLevel.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxRelicMinLevel.setMinimum(0)
        self.spinBoxRelicMinLevel.setMaximum(15)
        self.spinBoxRelicMinLevel.setProperty("value", 0)
        self.spinBoxRelicMinLevel.setObjectName("spinBoxRelicMinLevel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBoxRelicMinLevel)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.Scan)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 411, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 391, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonOpenLocation = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonOpenLocation.setObjectName("pushButtonOpenLocation")
        self.gridLayout.addWidget(self.pushButtonOpenLocation, 1, 1, 1, 1)
        self.pushButtonChangeLocation = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonChangeLocation.setObjectName("pushButtonChangeLocation")
        self.gridLayout.addWidget(self.pushButtonChangeLocation, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.lineEditOutputLocation = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditOutputLocation.setObjectName("lineEditOutputLocation")
        self.gridLayout.addWidget(self.lineEditOutputLocation, 0, 0, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.Scan)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 10, 231, 381))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 211, 351))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.Scan)
        self.label.setGeometry(QtCore.QRect(140, 360, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.Scan)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 210, 251, 131))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEditLog = QtWidgets.QPlainTextEdit(parent=self.groupBox_5)
        self.textEditLog.setGeometry(QtCore.QRect(10, 20, 231, 101))
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        self.tabWidget.addTab(self.Scan, "")
        self.Advanced = QtWidgets.QWidget()
        self.Advanced.setEnabled(True)
        self.Advanced.setObjectName("Advanced")
        self.formGroupBox_2 = QtWidgets.QGroupBox(parent=self.Advanced)
        self.formGroupBox_2.setGeometry(QtCore.QRect(10, 10, 171, 111))
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formGroupBox_2)
        self.formLayout_6.setObjectName("formLayout_6")
        self.checkBoxRecentRelicsFiveStar = QtWidgets.QCheckBox(parent=self.formGroupBox_2)
        self.checkBoxRecentRelicsFiveStar.setChecked(True)
        self.checkBoxRecentRelicsFiveStar.setObjectName("checkBoxRecentRelicsFiveStar")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBoxRecentRelicsFiveStar)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_15 = QtWidgets.QLabel(parent=self.formGroupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.spinBoxRecentRelics = QtWidgets.QSpinBox(parent=self.formGroupBox_2)
        self.spinBoxRecentRelics.setMinimum(1)
        self.spinBoxRecentRelics.setMaximum(1500)
        self.spinBoxRecentRelics.setProperty("value", 8)
        self.spinBoxRecentRelics.setObjectName("spinBoxRecentRelics")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBoxRecentRelics)
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.formLayout_9)
        self.pushButtonStartScanRecentRelics = QtWidgets.QPushButton(parent=self.formGroupBox_2)
        self.pushButtonStartScanRecentRelics.setEnabled(False)
        self.pushButtonStartScanRecentRelics.setObjectName("pushButtonStartScanRecentRelics")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButtonStartScanRecentRelics)
        self.groupBox_10 = QtWidgets.QGroupBox(parent=self.Advanced)
        self.groupBox_10.setGeometry(QtCore.QRect(430, 10, 231, 381))
        self.groupBox_10.setObjectName("groupBox_10")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.groupBox_10)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 211, 351))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.Advanced, "")
        self.Configure = QtWidgets.QWidget()
        self.Configure.setObjectName("Configure")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 90, 171, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.groupBox_6)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 151, 51))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.lineEditCharactersKey = KeyCaptureLineEdit(parent=self.formLayoutWidget_4)
        self.lineEditCharactersKey.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEditCharactersKey.setMaxLength(999)
        self.lineEditCharactersKey.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditCharactersKey.setObjectName("lineEditCharactersKey")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditCharactersKey)
        self.lineEditInventoryKey = KeyCaptureLineEdit(parent=self.formLayoutWidget_4)
        self.lineEditInventoryKey.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEditInventoryKey.setMaxLength(999)
        self.lineEditInventoryKey.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditInventoryKey.setClearButtonEnabled(False)
        self.lineEditInventoryKey.setObjectName("lineEditInventoryKey")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditInventoryKey)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 181, 71))
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_7)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 160, 42))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBoxIncludeUid = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        self.checkBoxIncludeUid.setObjectName("checkBoxIncludeUid")
        self.verticalLayout_4.addWidget(self.checkBoxIncludeUid)
        self.checkBoxSroFormat = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_2)
        self.checkBoxSroFormat.setObjectName("checkBoxSroFormat")
        self.verticalLayout_4.addWidget(self.checkBoxSroFormat)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 280, 201, 51))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_8)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxDebugMode = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBoxDebugMode.setObjectName("checkBoxDebugMode")
        self.verticalLayout_2.addWidget(self.checkBoxDebugMode)
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 180, 411, 91))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_9)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 391, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalScrollBarScanDelay = QtWidgets.QScrollBar(parent=self.gridLayoutWidget_2)
        self.horizontalScrollBarScanDelay.setMaximum(5000)
        self.horizontalScrollBarScanDelay.setSingleStep(100)
        self.horizontalScrollBarScanDelay.setPageStep(1000)
        self.horizontalScrollBarScanDelay.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBarScanDelay.setObjectName("horizontalScrollBarScanDelay")
        self.gridLayout_2.addWidget(self.horizontalScrollBarScanDelay, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.spinBoxNavDelay = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_2)
        self.spinBoxNavDelay.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spinBoxNavDelay.setWrapping(False)
        self.spinBoxNavDelay.setFrame(True)
        self.spinBoxNavDelay.setReadOnly(False)
        self.spinBoxNavDelay.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBoxNavDelay.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxNavDelay.setProperty("showGroupSeparator", False)
        self.spinBoxNavDelay.setSuffix("")
        self.spinBoxNavDelay.setMinimum(0)
        self.spinBoxNavDelay.setMaximum(100000)
        self.spinBoxNavDelay.setSingleStep(100)
        self.spinBoxNavDelay.setProperty("value", 0)
        self.spinBoxNavDelay.setObjectName("spinBoxNavDelay")
        self.gridLayout_2.addWidget(self.spinBoxNavDelay, 0, 2, 1, 1)
        self.spinBoxScanDelay = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_2)
        self.spinBoxScanDelay.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxScanDelay.setMaximum(100000)
        self.spinBoxScanDelay.setSingleStep(100)
        self.spinBoxScanDelay.setProperty("value", 0)
        self.spinBoxScanDelay.setObjectName("spinBoxScanDelay")
        self.gridLayout_2.addWidget(self.spinBoxScanDelay, 1, 2, 1, 1)
        self.horizontalScrollBarNavDelay = QtWidgets.QScrollBar(parent=self.gridLayoutWidget_2)
        self.horizontalScrollBarNavDelay.setSizeIncrement(QtCore.QSize(0, 0))
        self.horizontalScrollBarNavDelay.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.horizontalScrollBarNavDelay.setMaximum(5000)
        self.horizontalScrollBarNavDelay.setSingleStep(100)
        self.horizontalScrollBarNavDelay.setPageStep(1000)
        self.horizontalScrollBarNavDelay.setProperty("value", 0)
        self.horizontalScrollBarNavDelay.setSliderPosition(0)
        self.horizontalScrollBarNavDelay.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBarNavDelay.setInvertedAppearance(False)
        self.horizontalScrollBarNavDelay.setObjectName("horizontalScrollBarNavDelay")
        self.gridLayout_2.addWidget(self.horizontalScrollBarNavDelay, 0, 1, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_11.setGeometry(QtCore.QRect(430, 10, 231, 381))
        self.groupBox_11.setObjectName("groupBox_11")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.groupBox_11)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 20, 211, 351))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButtonRestoreDefaults = QtWidgets.QPushButton(parent=self.Configure)
        self.pushButtonRestoreDefaults.setGeometry(QtCore.QRect(10, 350, 111, 41))
        self.pushButtonRestoreDefaults.setObjectName("pushButtonRestoreDefaults")
        self.tabWidget.addTab(self.Configure, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalScrollBarNavDelay.valueChanged['int'].connect(self.spinBoxNavDelay.setValue) # type: ignore
        self.spinBoxNavDelay.valueChanged['int'].connect(self.horizontalScrollBarNavDelay.setValue) # type: ignore
        self.horizontalScrollBarScanDelay.valueChanged['int'].connect(self.spinBoxScanDelay.setValue) # type: ignore
        self.spinBoxScanDelay.valueChanged['int'].connect(self.horizontalScrollBarScanDelay.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HSR Scanner beta v0.6.2"))
        self.formGroupBox.setTitle(_translate("MainWindow", "Items to scan"))
        self.checkBoxScanLightCones.setText(_translate("MainWindow", "Light Cones"))
        self.checkBoxScanRelics.setText(_translate("MainWindow", "Relics"))
        self.checkBoxScanChars.setText(_translate("MainWindow", "Characters"))
        self.pushButtonStartScan.setText(_translate("MainWindow", "Start Scan"))
        self.groupBox.setTitle(_translate("MainWindow", "Item count"))
        self.label_23.setText(_translate("MainWindow", "Light Cones:"))
        self.label_24.setText(_translate("MainWindow", "Relics:"))
        self.label_25.setText(_translate("MainWindow", "Characters:"))
        self.labelLightConeProcessed.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "/"))
        self.labelLightConeCount.setText(_translate("MainWindow", "0"))
        self.labelRelicProcessed.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "/"))
        self.labelRelicCount.setText(_translate("MainWindow", "0"))
        self.labelCharacterProcessed.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.labelCharacterCount.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scan options"))
        self.label_3.setText(_translate("MainWindow", "Min Rarity:"))
        self.label_4.setText(_translate("MainWindow", "Min Level:"))
        self.label_2.setText(_translate("MainWindow", "Light Cone options"))
        self.label_6.setText(_translate("MainWindow", "Min Rarity:"))
        self.label_7.setText(_translate("MainWindow", "Min Level:"))
        self.label_8.setText(_translate("MainWindow", "Relic options"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output location"))
        self.pushButtonOpenLocation.setText(_translate("MainWindow", "Open Folder"))
        self.pushButtonChangeLocation.setText(_translate("MainWindow", "Change"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Info"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">HSR SCANNER v0.6.2</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">HOW TO RUN</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Set text language to English</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2. Set resolution with aspect ratio 16:9 (such as 1920x1080)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3. Open cellphone menu (ESC)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4. Press the start scan button</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5. Don\'t move mouse during the scan process</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">NOTES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">- </span><span style=\" font-size:8pt; color:#ff0000;\">The inventory screen is translucent and overall accuracy can be influenced by poor text contrast. </span><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">Make sure the item details and quantity number have a dark background before starting the scan.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Database is updated separately from this app. If the database version doesn\'t match the latest game version, then the database hasn\'t been updated yet. You will need to check again later.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HSR-Scanner is not affiliated with, endorsed, sponsored, or approved by HoYoverse.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Press ENTER to cancel"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scan), _translate("MainWindow", "Scan"))
        self.formGroupBox_2.setTitle(_translate("MainWindow", "Scan most recent relics"))
        self.checkBoxRecentRelicsFiveStar.setText(_translate("MainWindow", "Only count 5-star relics"))
        self.label_15.setText(_translate("MainWindow", "Number of relics:"))
        self.pushButtonStartScanRecentRelics.setText(_translate("MainWindow", "Scan"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Info"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tab will contain partial scan options for cases where scanning the entire account again isn\'t ideal.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">SCAN MOST RECENT RELICS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Useful for exporting only newly acquired relics without needing to do a full relic scan.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Advanced), _translate("MainWindow", "Advanced"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Hotkeys"))
        self.label_9.setText(_translate("MainWindow", "Inventory key:"))
        self.label_10.setText(_translate("MainWindow", "Characters key:"))
        self.lineEditCharactersKey.setText(_translate("MainWindow", "C"))
        self.lineEditInventoryKey.setText(_translate("MainWindow", "B"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Output"))
        self.checkBoxIncludeUid.setText(_translate("MainWindow", "Include UID"))
        self.checkBoxSroFormat.setToolTip(_translate("MainWindow", "Star Rail Optimizer"))
        self.checkBoxSroFormat.setText(_translate("MainWindow", "Also export in SRO format"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Developer"))
        self.checkBoxDebugMode.setToolTip(_translate("MainWindow", "Saves ALL screenshots"))
        self.checkBoxDebugMode.setText(_translate("MainWindow", "Debug mode"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Additional Delay (for slow computers)"))
        self.label_11.setToolTip(_translate("MainWindow", "Navigating between different pages (inventory, character details, etc.)"))
        self.label_11.setText(_translate("MainWindow", "Navigation speed (ms):"))
        self.label_13.setToolTip(_translate("MainWindow", "Clicking between each individual item (relics, light cones, and characters)"))
        self.label_13.setText(_translate("MainWindow", "Scan speed (ms):"))
        self.spinBoxNavDelay.setPrefix(_translate("MainWindow", "+"))
        self.spinBoxScanDelay.setPrefix(_translate("MainWindow", "+"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Info"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">ADDITIONAL DELAY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If Star Rail lags during the scan process, the scanner might produce inaccurate output or fail entirely. To compensate, there are two types of delay that can be increased accordingly to your system:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Navigation delay for navigating between different pages (inventory, character details, etc.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Scan delay for clicking between individual items (relics, light cones, and characters).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">DEBUG MODE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enabling this option will export ALL screenshots taken during a scan. The screenshots will be saved to a debug folder in the same directory as the JSON output.</p></body></html>"))
        self.pushButtonRestoreDefaults.setText(_translate("MainWindow", "Restore Defaults"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configure), _translate("MainWindow", "Configure"))
from ui.key_capture_line_edit import KeyCaptureLineEdit
