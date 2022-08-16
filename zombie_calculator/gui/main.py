from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QLocale
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStyleOptionTabWidgetFrame, QStyle

class TabWidget(QTabWidget):
    def minimumSizeHint(self):
        if self.count() < 0:
            return super().sizeHint()

        baseSize = self.currentWidget().sizeHint().expandedTo(
            self.currentWidget().minimumSize())
        if not self.tabBar().isHidden():
            tabHint = self.tabBar().sizeHint()
            if self.tabPosition() in (self.North, self.South):
                baseSize.setHeight(baseSize.height()
                    + tabHint.height())
            else:
                baseSize.setWidth(baseSize.width()
                    + tabHint.width())

        opt = QStyleOptionTabWidgetFrame()
        self.initStyleOption(opt)
        return self.style().sizeFromContents(
            QStyle.CT_TabWidget, opt, baseSize, self)

    def sizeHint(self):
        return self.minimumSizeHint()

class Ui_mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_mainWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.tabWidget = TabWidget()
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.currentChanged.connect(self.updateSize)
        self.retranslateUi()

    def updateSize(self):
        self.tabWidget.updateGeometry()
        super().updateGeometry()
        self.adjustSize()
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("mainWindow", "Zombie_calculator"))