# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_msgWindow(object):
    def setupUi(self, msgWindow):
        msgWindow.setObjectName("msgWindow")
        msgWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        msgWindow.resize(231, 134)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(msgWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.msgLabal = QtWidgets.QLabel(msgWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.msgLabal.setFont(font)
        self.msgLabal.setText("")
        self.msgLabal.setAlignment(QtCore.Qt.AlignCenter)
        self.msgLabal.setObjectName("msgLabal")
        self.verticalLayout.addWidget(self.msgLabal)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.return_btn = QtWidgets.QPushButton(msgWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_btn.sizePolicy().hasHeightForWidth())
        self.return_btn.setSizePolicy(sizePolicy)
        self.return_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.return_btn.setObjectName("return_btn")
        self.horizontalLayout.addWidget(self.return_btn)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copy_btn = QtWidgets.QPushButton(msgWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_btn.sizePolicy().hasHeightForWidth())
        self.copy_btn.setSizePolicy(sizePolicy)
        self.copy_btn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.copy_btn.setObjectName("copy_btn")
        self.horizontalLayout.addWidget(self.copy_btn)
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(msgWindow)
        QtCore.QMetaObject.connectSlotsByName(msgWindow)

    def retranslateUi(self, msgWindow):
        _translate = QtCore.QCoreApplication.translate
        msgWindow.setWindowTitle(_translate("msgWindow", "正在计算中..."))
        self.return_btn.setText(_translate("msgWindow", "返回"))
        self.copy_btn.setText(_translate("msgWindow", "复制种子"))
