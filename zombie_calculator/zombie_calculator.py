from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtCore import pyqtSignal as Signal, QObject, Qt, QCoreApplication, QTranslator, QEvent, QLocale
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QCheckBox, QDialog, QHeaderView, QTableWidgetItem, QStatusBar, QGraphicsOpacityEffect, QLabel, QActionGroup, QAction
from PyQt5.QtWinExtras import QWinTaskbarButton
from qt_material import build_stylesheet, QtStyleTools

from bidict import bidict
from dataclasses import dataclass
from enum import Enum, unique
from typing import List
import os
import sys
import time
import threading
import seedFinder
import asmInject
import webbrowser
import copy
import pyperclip

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cwd)

from gui.introduction import Ui_introductionWindow
from gui.main import Ui_mainWindow
from gui.mode1 import Ui_mode1Window
from gui.mode2 import Ui_mode2Window
from gui.msg import Ui_msgWindow
from gui.modify import Ui_modifyWindow

from config import Config

_translate = QCoreApplication.translate

def apply_stylesheet(
    app,
    theme='',
    style=None,
    save_as=None,
    invert_secondary=False,
    extra={},
    parent='theme',
):

    if style:
        try:
            try:
                app.setStyle(style)
            except:  # snake_case, true_property
                app.style = style
        except:
            #logging.error(f"The style '{style}' does not exist.")
            pass

    if extra.get("QMenu") != True and "QMenu" in extra:
        for k in extra['QMenu']:
            extra[f'qmenu_{k}'] = extra['QMenu'][k]
        extra['QMenu'] = True

    stylesheet = build_stylesheet(theme, invert_secondary, extra, parent, os.path.join(cwd, "pack_resources/material.css.template"))
    if stylesheet is None:
        return

    if save_as:
        with open(save_as, 'w') as file:
            file.writelines(stylesheet)

    try:
        app.setStyleSheet(stylesheet)
    except:
        app.style_sheet = stylesheet

class introductionWindow(QMainWindow, Ui_introductionWindow, QtStyleTools):
    def __init__(self, config, parent=None):
        super(introductionWindow, self).__init__(parent)

        self.configManager = config

        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(cwd, "pack_resources/icon.ico")))
    def apply_stylesheet(
        self, parent, theme, invert_secondary=False, extra={}, callable_=None
    ):
        if theme == 'default':
            try:
                parent.setStyleSheet('')
            except:
                parent.style_sheet = ''
            return

        apply_stylesheet(
            parent,
            theme=theme,
            invert_secondary=invert_secondary,
            extra=extra,
        )

        if callable_:
            callable_()

    def update_theme_event(self, parent):
        density = [
            action.text()
            for action in self.menu_density_.actions()
            if action.isChecked()
        ][0]
        theme = [
            action.text()
            for action in self.menu_theme_.actions()
            if action.isChecked()
        ][0]

        if theme == "default":
            theme = self.configManager.config["defaultTheme"]
        else:
            self.configManager.config["defaultTheme"] = theme 
        self.configManager.config["defaultDensity"] = density
        self.configManager.config["extra"]["density_scale"] = density
        self.configManager.updateConfig(self.configManager.config)

        self.extra_values['density_scale'] = density
        
        self.apply_stylesheet(
            parent,
            theme=theme,
            invert_secondary=theme.startswith('light'),
            extra=self.extra_values,
            callable_=self.update_buttons,
        )
    def add_menu_density(self, parent, menu):
        self.menu_density_ = menu
        action_group = QActionGroup(menu)
        action_group.setExclusive(True)

        for density in map(str, range(-3, 4)):
            action = QAction(parent)
            action.triggered.connect(lambda: self.update_theme_event(parent))
            action.setText(density)
            action.setCheckable(True)
            action.setChecked(density == self.configManager.config["defaultDensity"])
            action.setActionGroup(action_group)
            menu.addAction(action)
            action_group.addAction(action)
    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange:
            self.retranslateUi(self)
class mode1Window(QWidget, Ui_mode1Window):
    def __init__(self, config, parent=None):
        super(mode1Window, self).__init__(parent)

        self.configManager = config

        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(cwd, "pack_resources/icon.ico")))
        self.setAttribute(Qt.WA_DeleteOnClose)
class mode2Window(QWidget, Ui_mode2Window):
    def __init__(self, config, parent=None):
        super(mode2Window, self).__init__(parent)

        self.configManager = config

        self.setupUi(self) 
        self.setWindowIcon(QIcon(os.path.join(cwd, "pack_resources/icon.ico")))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.waveTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.waveTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.waveTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
class msgWindow(QDialog, Ui_msgWindow):
    def __init__(self, config, parent=None):
        super(msgWindow, self).__init__(parent)

        self.configManager = config

        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(cwd, "pack_resources/icon.ico")))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint)
class modifyWindow(QWidget, Ui_modifyWindow):
    def __init__(self, config, parent=None):
        super(modifyWindow, self).__init__(parent)

        self.configManager = config

        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(cwd, "pack_resources/icon.ico")))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.statusBar = QStatusBar()
        self.statusLabel = QLabel()
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.setSizeGripEnabled(False)
        opacityEffect = QGraphicsOpacityEffect()
        self.statusBar.setGraphicsEffect(opacityEffect)
        opacityEffect.setOpacity(0.7)
        self.layout().addWidget(self.statusBar)

        self.getInitSeed()
    def getInitSeed(self):
        self.injecter = asmInject.seedInject()
        self.seed_Input.setValue(self.injecter.getRandomSeed())
        self.compareResult(self.injecter.findResult)
    def compareResult(self, res):
        if res == self.injecter.OK:
            color = self.configManager.config["alertColor"]["ok"]
            info = _translate("calculator", "Successfully found game.")
            self.statusLabel.setText(f"<font color=\"{color}\" style=\"font-style: italic;\">{info}</font>")
            return True
        elif res == self.injecter.WrongVersion:
            color = self.configManager.config["alertColor"]["warning"]
            info = _translate("calculator", "No support versions.")
            self.statusLabel.setText(f"<font color=\"{color}\" style=\"font-style: italic;\">{info}</font>")
            return False
        elif res == self.injecter.NotFound:
            color = self.configManager.config["alertColor"]["error"]
            info = _translate("calculator", "Game not found.")
            self.statusLabel.setText(f"<font color=\"{color}\" style=\"font-style: italic;\">{info}</font>")
            return False
        elif res == self.injecter.OpenError:
            color = self.configManager.config["alertColor"]["error"]
            info = _translate("calculator", "Process open error")
            self.statusLabel.setText(f"<font color=\"{color}\" style=\"font-style: italic;\">{info}</font>")
            return False
class mainWindow(Ui_mainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowIcon(QIcon(os.path.join(cwd, "pack_resources/icon.ico")))

class calculator:
    class signalStore(QObject):
        msgUpdate = Signal(str)
        titleUpdate = Signal(str)
        processUpdate = Signal(int)
        alert = Signal()

    @dataclass
    class waveRequire:
        level_beginning : int
        level_ending : int
        idNeeded : List[int]
        idRefused : List[int]

    @unique
    class taskBarUpdateSignal(Enum):
        init = -1
        stop = -2

    #工具方法&初始化
    def __init__(self):
        self.configManager = Config()
        self.configManager.updateConfig(self.configManager.readConfig())
        self.logInterval = self.configManager.config["logInterval"]
        
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        self.app = QApplication(sys.argv)
        apply_stylesheet(self.app, self.configManager.config["defaultTheme"], invert_secondary="light_" in self.configManager.config["defaultTheme"], extra=copy.deepcopy(self.configManager.config["extra"]))
        
        language = QLocale().language()
        self.trans = QTranslator()
        if language == QLocale.Chinese:
            self.trans.load(os.path.join(cwd, "pack_resources/language/zh_CN.qm"))
        self.app.installTranslator(self.trans)

        self.store = self.signalStore()
        self.store.msgUpdate.connect(self.msgUpdate)
        self.store.titleUpdate.connect(self.titleUpdate)
        self.store.processUpdate.connect(self.updateTaskBar)
        self.store.alert.connect(self.completeAlert)
        self.introWindowInit()

    def changeLanguage(self):
        language = self.introW.sender().text()
        if language == "English":
            self.app.removeTranslator(self.trans)
        elif language == "中文":
            self.trans.load(os.path.join(cwd, "pack_resources/language/zh_CN.qm"))
            self.app.installTranslator(self.trans)

    def start(self):
        self.introW.show()
        sys.exit(self.app.exec_())

    def rBtnGroupClicked(self, sender):
        if sender == "mode1":
            btn = self.mode1W.sceneGroup.checkedButton()
            self.scene = btn.objectName()[:-5]
        elif sender == "mode2":
            btn = self.mode2W.sceneGroup.checkedButton()
            self.scene = btn.objectName()[:-5]
    def nCheckBoxClicked(self):
        box = self.mode2W.sender()
        id = self.typeName[box.text()]
        if box.isChecked():
            self.idNeeded.add(id)
        else:
            self.idNeeded.remove(id)
    def rCheckBoxClicked(self):
        box = self.mode2W.sender()
        id = self.typeName[box.text()]
        if box.isChecked():
            self.idRefused.add(id)
        else:
            self.idRefused.remove(id)

    #开始窗口
    def introWindowInit(self):
        self.introW = introductionWindow(self.configManager)

        self.introW.set_extra(copy.deepcopy(self.configManager.config["extra"]))
        self.introW.add_menu_density(self.app, self.introW.menuDensity)
        self.introW.add_menu_theme(self.app, self.introW.menuStyle)

        self.introW.start_btn.clicked.connect(self.showMainWindow)
        self.introW.inject_btn.clicked.connect(self.modifyWindowInit)
        self.introW.exit_btn.clicked.connect(self.app.quit)
        self.introW.help_btn.clicked.connect(lambda : webbrowser.open(os.path.join(cwd, "pack_resources/help/help.html")))
        for action in self.introW.menuLanguage.actions():
            action.triggered.connect(self.changeLanguage)

    #主窗口
    def mainWindowInit(self):
        self.mainW = mainWindow()
        self.mode2WindowInit() 
        self.mode1WindowInit()      
        
        self.mainW.tabWidget.addTab(self.mode1W, _translate("calculator", "Mode1"))
        self.mainW.tabWidget.addTab(self.mode2W, _translate("calculator", "Mode2"))
    def showMainWindow(self):
        self.mainWindowInit()
        self.mainW.show()

    def borderCheck(self, parent, flags_beginning, flags_ending):
        if not flags_beginning % 2 or flags_ending % 2:
            QMessageBox.critical(parent, _translate("calculator", "Error"), _translate("calculator", "startingFlag should be odds, endingFlags should be even."))
            return False
        if hasattr(self, "scene") == False:
            QMessageBox.critical(parent, _translate("calculator", "Error"), _translate("calculator", "Please select scene."))
            return False
        return True
    #模式1
    def mode1WindowInit(self):
        self.mode1W = mode1Window(self.configManager)
        self.mode1W.calc_btn.clicked.connect(self.mode1Calc)
        self.mode1W.sceneGroup.buttonClicked.connect(lambda : self.rBtnGroupClicked("mode1"))
        self.mode1W.return_btn.clicked.connect(self.mainW.close)
        self.mode1W.help_btn.clicked.connect(lambda : webbrowser.open(os.path.join(cwd, "pack_resources/help/help.html")))

        additional = bidict({_translate("calculator", "Normal") : 0, _translate("calculator", "Flag") : 1})
        self.typeName.update(additional)
    def mode1Calc(self):
        try:
            uid = self.mode1W.uid_Input.value()
            mode = self.mode1W.mode_Input.value()

            flags_beginning = self.mode1W.startFlag_Input.value()
            flags_ending = self.mode1W.endFlag_Input.value()

            level_beginning = (flags_beginning - 1) // 2
            level_ending = flags_ending // 2

            seed = self.mode1W.seed_Input.value()
            
            if not self.borderCheck(self.mode1W, flags_beginning, flags_ending):
                return
        except:
            QMessageBox.critical(self.mode1W, _translate("calculator", "Error"), _translate("calculator", "Unexpected exceptions happened!"))
        else:
            try:
                self.result = ""
                for lvl in range(level_beginning, level_ending):
                    zombies = seedFinder.appear(uid, mode, self.scene, lvl, seed)
                    self.result += "{} {} {} {}".format(lvl * 2 + 1, _translate("calculator", "to"), lvl * 2 + 2, _translate("calculator", "flags spawn zombies:"))
                    amount = 0
                    for i in range(len(zombies)):
                        if zombies[i]:
                            amount += 1
                            self.result += self.typeName.inverse[i] + " "
                    self.result += "{} {} {}\n\n".format(_translate("calculator", "Total"), amount, _translate("calculator", "zombies"))
                self.msgWindowInit()
                self.store.msgUpdate.emit(self.result)
                self.store.titleUpdate.emit(_translate("calculator", "Calculation completed."))
                self.store.alert.emit()
            except:
                QMessageBox.critical(self.mode1W, _translate("calculator", "Error"), _translate("calculator", "Unexpected exceptions happened!"))

    #模式2
    def mode2WindowInit(self):
        self.mode2W = mode2Window(self.configManager)
        self.mode2W.calc_btn.clicked.connect(self.mode2Calc)
        self.mode2W.join_btn.clicked.connect(self.joinTable)
        self.mode2W.del_btn.clicked.connect(self.delTable)
        self.mode2W.return_btn.clicked.connect(self.mainW.close)
        self.mode2W.help_btn.clicked.connect(lambda : webbrowser.open(os.path.join(cwd, "pack_resources/help/help.html")))
        self.mode2W.sceneGroup.buttonClicked.connect(lambda : self.rBtnGroupClicked("mode2"))
        self.typeName = bidict()

        for box in self.mode2W.needGroup.findChildren(QCheckBox):
            box.stateChanged.connect(self.nCheckBoxClicked)
        for box in self.mode2W.refuseGroup.findChildren(QCheckBox):
            box.stateChanged.connect(self.rCheckBoxClicked)
        for box in self.mode2W.needGroup.findChildren(QCheckBox):
            id = int(box.objectName()[8:])
            text = box.text()
            self.typeName.put(key=text, val=id)
        
        self.windowsTaskbarButton = QWinTaskbarButton()
        self.windowsTaskbarButton.setWindow(self.introW.windowHandle())
        self.windowsTaskbarProcess = self.windowsTaskbarButton.progress()
        self.windowsTaskbarProcess.setRange(0, 10000)

        self.idNeeded = set()
        self.idRefused = set()
        self.wave = []
    def mode2Calc(self):
        try:
            self.calcDone = False
            uid = self.mode2W.uid_Input.value()
            mode = self.mode2W.mode_Input.value()
            seed = self.mode2W.seed_Input.value()

            if not self.wave:
                QMessageBox.critical(self.mode2W, _translate("calculator", "Error"), _translate("calculator", "At least one requirement."))
                return

            waveBeginning = sorted([i.level_beginning for i in self.wave])
            waveEnding = sorted([i.level_ending for i in self.wave])
            for i in range(1, len(waveBeginning)):
                if waveBeginning[i] < waveEnding[i - 1]:
                    QMessageBox.critical(self.mode2W, _translate("calculator", "Error"), _translate("calculator", "Please check the entered sections have overlapping borders."))
                    return
            
            self.wave.sort(key=lambda x : x.level_ending)
            maxWave = self.wave[-1].level_ending - 1
            idNeeded = [[] for i in range(maxWave)]
            idRefused = [[] for i in range(maxWave)]

            for eachWave in self.wave:
                for i in range(eachWave.level_beginning - 1, eachWave.level_ending - 1):
                    idNeeded[i] = eachWave.idNeeded
                    idRefused[i] = eachWave.idRefused
        except:
            QMessageBox.critical(self.mode2W, _translate("calculator", "Error"), _translate("calculator", "Unexpected exceptions happened!"))
        else:
            self.finder = seedFinder.requestToSeed(uid, mode, self.scene, self.wave[0].level_beginning, self.wave[-1].level_ending, seed)
            self.thdList = (threading.Thread(target=self.mode2CalcThread, args=(idNeeded, idRefused)), 
                            threading.Thread(target=self.seedLogger))
            for thd in self.thdList:
                thd.start()
            self.msgWindowInit()
    def mode2CalcThread(self, idNeeded, idRefused):
        self.result = self.finder.calc(idNeeded, idRefused)
        self.calcDone = True
    def seedLogger(self):
        self.store.processUpdate.emit(self.taskBarUpdateSignal.init.value)
        while self.calcDone == False and self.finder.seed >= 0:
            try:
                lastSeed = self.finder.seed
                time.sleep(self.logInterval)
                remainTime = self.logInterval * (0x7FFFFFFF - self.finder.seed) / (self.finder.seed - lastSeed) / 60
                self.store.msgUpdate.emit("{}\n{}{:#x}\n{}{:.2%} {}{:.2f}mins".format(
                    _translate("calculator", "Calculating... Please wait."), _translate("calculator", "Current seachered seed is "), self.finder.seed, _translate("calculator", "Processing:"),
                    self.finder.seed / 0x7FFFFFFF, _translate("calculator", "Remainning time:"), remainTime))
                self.store.titleUpdate.emit("{}{:.2%}".format(_translate("calculator", "Calculating... Processing:"), self.finder.seed / 0x7FFFFFFF))
                self.store.processUpdate.emit(int(self.finder.seed / 0x7FFFFFFF * 10000))
            except ZeroDivisionError:
                self.store.titleUpdate.emit(_translate("calculator", "Calculation completed."))
                self.store.processUpdate.emit(self.taskBarUpdateSignal.stop.value)
        if self.finder.seed >= 0:
            self.store.msgUpdate.emit("{}{:#x}".format(_translate("calculator", "Found satisfying seed:"), self.result))
            self.store.titleUpdate.emit(_translate("calculator", "Calculation completed."))
        else:
            self.finder.stopThread = True
            self.store.msgUpdate.emit(_translate("calculator", "No satisfying seed found."))
            self.store.titleUpdate.emit(_translate("calculator", "No satisfying seed found."))
        if not self.finder.stopThread:
            self.store.alert.emit()
    def updateTaskBar(self, process):
        if process == self.taskBarUpdateSignal.stop.value:
            self.windowsTaskbarProcess.setValue(0)
            self.windowsTaskbarProcess.setVisible(False)
        elif process == self.taskBarUpdateSignal.init.value:
            self.windowsTaskbarProcess.show()
        else:
            self.windowsTaskbarProcess.setValue(process)            
    def joinTable(self):
        flags_beginning = self.mode2W.startFlag_Input.value()
        flags_ending = self.mode2W.endFlag_Input.value()
        level_beginning = (flags_beginning - 1) // 2
        level_ending = flags_ending // 2

        if not self.borderCheck(self.mode2W, flags_beginning, flags_ending):
            return
        for i in self.idNeeded:
            if i in self.idRefused:
                QMessageBox.critical(self.mode2W, _translate("calculator", "Error"), _translate("calculator", "Requirements conflicts with exceptions."))
                return
        if 2 in self.idRefused and 5 in self.idRefused:
            QMessageBox.critical(self.mode2W, _translate("calculator", "Error"), _translate("calculator", "Either conehead or newspaper should spawn."))
            return

        idNeededShow = [self.typeName.inverse[i] for i in self.idNeeded]
        idRefusedShow = [self.typeName.inverse[i] for i in self.idRefused]
    
        waveShow = ((flags_beginning, flags_ending), idNeededShow, idRefusedShow)

        waveInstance = self.waveRequire(level_beginning, level_ending, list(self.idNeeded), list(self.idRefused))
        if self.wave.count(waveInstance):
            return
        self.wave.append(waveInstance)
        row = self.mode2W.waveTable.rowCount()
        self.mode2W.waveTable.insertRow(row)
        for i in range(len(waveShow)):
            item = QTableWidgetItem(str(waveShow[i]))
            self.mode2W.waveTable.setItem(row, i, item)

        if self.wave:
            self.mode2W.uidGroupBox.setEnabled(False)
            self.mode2W.sceneGroupBox.setEnabled(False)
    def delTable(self):
        try:
            row = self.mode2W.waveTable.currentRow()
        
            flags_beginning = eval(self.mode2W.waveTable.item(row, 0).text())[0]
            flags_ending = eval(self.mode2W.waveTable.item(row, 0).text())[1]
            level_beginning = (flags_beginning - 1) // 2
            level_ending = flags_ending // 2
            idNeeded = eval(self.mode2W.waveTable.item(row, 1).text())
            idRefused = eval(self.mode2W.waveTable.item(row, 2).text())
            idNeeded = list(map(lambda x : self.typeName[x], idNeeded))
            idRefused = list(map(lambda x : self.typeName[x], idRefused))
            waveInstance = self.waveRequire(level_beginning, level_ending, idNeeded, idRefused)
            self.wave.remove(waveInstance)
            if not self.wave:
                self.mode2W.uidGroupBox.setEnabled(True)
                self.mode2W.sceneGroupBox.setEnabled(True)

            self.mode2W.waveTable.removeRow(row)
        except AttributeError:
            return

    #消息展示窗口
    def msgUpdate(self, msg):
        self.msgW.msgLabal.setText(msg)
    def titleUpdate(self, title):
        self.msgW.setWindowTitle(title)
    def completeAlert(self):
        self.app.alert(self.mainW)
        self.app.beep()
        self.msgW.copy_btn.setEnabled(True)
    def msgWindowInit(self):
        self.msgW = msgWindow(self.configManager)
        self.msgW.return_btn.clicked.connect(self.msgExit)
        self.msgW.copy_btn.clicked.connect(self.msgCopy)
        self.msgW.show()
    def msgExit(self):
        if self.mainW.tabWidget.currentIndex():
            self.finder.stopThread = True
            self.store.processUpdate.emit(self.taskBarUpdateSignal.stop.value)
            isExit = False
            while isExit == False:
                isExit = not(self.thdList[0].is_alive()) and not(self.thdList[1].is_alive())
        self.msgW.close()
    def msgCopy(self):
        if self.mainW.tabWidget.currentIndex():
            if self.calcDone and self.finder.seed >= 0:
                pyperclip.copy(f"{self.result:x}")
                QMessageBox.information(self.mode2W, _translate("calculator", "Successfully"), "{}{:#x}{}".format(_translate("calculator", "Seed: "), self.result, _translate("calculator", " has copied.")))
                self.msgExit()
        else:
            pyperclip.copy(self.result)
            QMessageBox.information(self.mode1W, _translate("calculator", "Successfully"), _translate("calculator", "Spawn zombies have copied."))
            self.msgExit()

    #种子修改窗口
    def modifyWindowInit(self):
        self.modifyW = modifyWindow(self.configManager)
        self.modifyW.getSeed_btn.clicked.connect(lambda : self.modifyW.seed_Input.setValue(self.modifyW.injecter.getRandomSeed()))
        self.modifyW.modifySeed_btn.clicked.connect(lambda : self.modifySeed(self.modifyW.seed_Input.value()))
        self.modifyW.findGame_btn.clicked.connect(self.reFindGame)
        self.modifyW.show()
    def reFindGame(self):
        self.modifyW.injecter.findGame()
        self.modifyW.compareResult(self.modifyW.injecter.findResult)
    def modifySeed(self, seed):
        if self.modifyW.compareResult(self.modifyW.injecter.findResult):
            self.modifyW.injecter.setRandomSeed(seed)
            self.modifyW.injecter.internalSpawn()

if __name__ == "__main__":
    calculator().start()