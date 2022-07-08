# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'introduction.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_introductionWindow(object):
    def setupUi(self, introductionWindow):
        introductionWindow.setObjectName("introductionWindow")
        introductionWindow.resize(545, 210)
        introductionWindow.setMinimumSize(QtCore.QSize(0, 210))
        introductionWindow.setMaximumSize(QtCore.QSize(545, 210))
        self.centralwidget = QtWidgets.QWidget(introductionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.introduction = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.introduction.setFont(font)
        self.introduction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.introduction.setWordWrap(False)
        self.introduction.setObjectName("introduction")
        self.verticalLayout.addWidget(self.introduction)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.help_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy)
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setCheckable(False)
        self.exit_btn.setAutoDefault(False)
        self.exit_btn.setFlat(False)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        introductionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(introductionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 23))
        self.menubar.setObjectName("menubar")
        introductionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(introductionWindow)
        self.statusbar.setObjectName("statusbar")
        introductionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(introductionWindow)
        QtCore.QMetaObject.connectSlotsByName(introductionWindow)

    def retranslateUi(self, introductionWindow):
        _translate = QtCore.QCoreApplication.translate
        introductionWindow.setWindowTitle(_translate("introductionWindow", "出怪计算器"))
        self.introduction.setText(_translate("introductionWindow", "欢迎使用出怪计算器！"))
        self.start_btn.setText(_translate("introductionWindow", "开始计算"))
        self.help_btn.setText(_translate("introductionWindow", "查看帮助"))
        self.exit_btn.setText(_translate("introductionWindow", "退出程序"))
