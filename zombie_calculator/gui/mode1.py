# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mode1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mode1Window(object):
    def setupUi(self, mode1Window):
        mode1Window.setObjectName("mode1Window")
        mode1Window.setWindowModality(QtCore.Qt.ApplicationModal)
        mode1Window.resize(661, 336)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mode1Window.sizePolicy().hasHeightForWidth())
        mode1Window.setSizePolicy(sizePolicy)
        mode1Window.setMinimumSize(QtCore.QSize(0, 0))
        mode1Window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(mode1Window)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(mode1Window)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(9, -1, 9, 9)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uid = QtWidgets.QLabel(self.groupBox)
        self.uid.setObjectName("uid")
        self.horizontalLayout.addWidget(self.uid)
        self.uid_Input = QtWidgets.QSpinBox(self.groupBox)
        self.uid_Input.setWrapping(False)
        self.uid_Input.setFrame(True)
        self.uid_Input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uid_Input.setMaximum(2147483646)
        self.uid_Input.setDisplayIntegerBase(10)
        self.uid_Input.setObjectName("uid_Input")
        self.horizontalLayout.addWidget(self.uid_Input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mode = QtWidgets.QLabel(self.groupBox)
        self.mode.setObjectName("mode")
        self.horizontalLayout_2.addWidget(self.mode)
        self.mode_Input = QtWidgets.QSpinBox(self.groupBox)
        self.mode_Input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mode_Input.setMaximum(2147483646)
        self.mode_Input.setDisplayIntegerBase(10)
        self.mode_Input.setObjectName("mode_Input")
        self.horizontalLayout_2.addWidget(self.mode_Input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(mode1Window)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startFlag = QtWidgets.QLabel(self.groupBox_3)
        self.startFlag.setObjectName("startFlag")
        self.horizontalLayout_3.addWidget(self.startFlag)
        self.startFlag_Input = QtWidgets.QSpinBox(self.groupBox_3)
        self.startFlag_Input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startFlag_Input.setMaximum(2147483646)
        self.startFlag_Input.setDisplayIntegerBase(10)
        self.startFlag_Input.setObjectName("startFlag_Input")
        self.horizontalLayout_3.addWidget(self.startFlag_Input)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.endFlag = QtWidgets.QLabel(self.groupBox_3)
        self.endFlag.setObjectName("endFlag")
        self.horizontalLayout_4.addWidget(self.endFlag)
        self.endFlag_Input = QtWidgets.QSpinBox(self.groupBox_3)
        self.endFlag_Input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endFlag_Input.setMaximum(2147483646)
        self.endFlag_Input.setDisplayIntegerBase(10)
        self.endFlag_Input.setObjectName("endFlag_Input")
        self.horizontalLayout_4.addWidget(self.endFlag_Input)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.seed = QtWidgets.QLabel(self.groupBox_3)
        self.seed.setObjectName("seed")
        self.horizontalLayout_5.addWidget(self.seed)
        self.seed_Input = QtWidgets.QSpinBox(self.groupBox_3)
        self.seed_Input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.seed_Input.setMaximum(2147483646)
        self.seed_Input.setDisplayIntegerBase(16)
        self.seed_Input.setObjectName("seed_Input")
        self.horizontalLayout_5.addWidget(self.seed_Input)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(mode1Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DAY_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.DAY_rBtn.setObjectName("DAY_rBtn")
        self.sceneGroup = QtWidgets.QButtonGroup(mode1Window)
        self.sceneGroup.setObjectName("sceneGroup")
        self.sceneGroup.addButton(self.DAY_rBtn)
        self.verticalLayout_2.addWidget(self.DAY_rBtn)
        self.NIGHT_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.NIGHT_rBtn.setObjectName("NIGHT_rBtn")
        self.sceneGroup.addButton(self.NIGHT_rBtn)
        self.verticalLayout_2.addWidget(self.NIGHT_rBtn)
        self.POOL_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.POOL_rBtn.setObjectName("POOL_rBtn")
        self.sceneGroup.addButton(self.POOL_rBtn)
        self.verticalLayout_2.addWidget(self.POOL_rBtn)
        self.FOG_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.FOG_rBtn.setObjectName("FOG_rBtn")
        self.sceneGroup.addButton(self.FOG_rBtn)
        self.verticalLayout_2.addWidget(self.FOG_rBtn)
        self.ROOF_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.ROOF_rBtn.setObjectName("ROOF_rBtn")
        self.sceneGroup.addButton(self.ROOF_rBtn)
        self.verticalLayout_2.addWidget(self.ROOF_rBtn)
        self.MOON_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.MOON_rBtn.setObjectName("MOON_rBtn")
        self.sceneGroup.addButton(self.MOON_rBtn)
        self.verticalLayout_2.addWidget(self.MOON_rBtn)
        self.MG_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.MG_rBtn.setObjectName("MG_rBtn")
        self.sceneGroup.addButton(self.MG_rBtn)
        self.verticalLayout_2.addWidget(self.MG_rBtn)
        self.AQ_rBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.AQ_rBtn.setObjectName("AQ_rBtn")
        self.sceneGroup.addButton(self.AQ_rBtn)
        self.verticalLayout_2.addWidget(self.AQ_rBtn)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.help_btn = QtWidgets.QPushButton(mode1Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy)
        self.help_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout_8.addWidget(self.help_btn)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.calc_btn = QtWidgets.QPushButton(mode1Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.calc_btn.sizePolicy().hasHeightForWidth())
        self.calc_btn.setSizePolicy(sizePolicy)
        self.calc_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.calc_btn.setObjectName("calc_btn")
        self.horizontalLayout_8.addWidget(self.calc_btn)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.return_btn = QtWidgets.QPushButton(mode1Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_btn.sizePolicy().hasHeightForWidth())
        self.return_btn.setSizePolicy(sizePolicy)
        self.return_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.return_btn.setObjectName("return_btn")
        self.horizontalLayout_8.addWidget(self.return_btn)
        spacerItem3 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.retranslateUi(mode1Window)
        QtCore.QMetaObject.connectSlotsByName(mode1Window)

    def retranslateUi(self, mode1Window):
        _translate = QtCore.QCoreApplication.translate
        mode1Window.setWindowTitle(_translate("mode1Window", "mode1"))
        self.uid.setText(_translate("mode1Window", "Uid:"))
        self.mode.setText(_translate("mode1Window", "Mode:"))
        self.startFlag.setText(_translate("mode1Window", "StartingFlag:"))
        self.endFlag.setText(_translate("mode1Window", "EndingFlag:"))
        self.seed.setText(_translate("mode1Window", "Seed:"))
        self.groupBox_2.setTitle(_translate("mode1Window", "Select Scene:"))
        self.DAY_rBtn.setText(_translate("mode1Window", "Day Endless"))
        self.NIGHT_rBtn.setText(_translate("mode1Window", "Night Endless"))
        self.POOL_rBtn.setText(_translate("mode1Window", "Pool Endless"))
        self.FOG_rBtn.setText(_translate("mode1Window", "Fog Endless"))
        self.ROOF_rBtn.setText(_translate("mode1Window", "Roof Endless"))
        self.MOON_rBtn.setText(_translate("mode1Window", "Moon Endless"))
        self.MG_rBtn.setText(_translate("mode1Window", "Mushroom Garden Endless"))
        self.AQ_rBtn.setText(_translate("mode1Window", "Aquarium Endless"))
        self.help_btn.setText(_translate("mode1Window", "Help"))
        self.calc_btn.setText(_translate("mode1Window", "Calculate"))
        self.return_btn.setText(_translate("mode1Window", "Back"))
