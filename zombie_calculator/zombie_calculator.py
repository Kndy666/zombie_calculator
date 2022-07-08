from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal as Signal, QObject, Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QCheckBox, QDialog, QHeaderView, QTableWidgetItem
from qt_material import apply_stylesheet

from bidict import bidict
from pathlib import Path
import sys
import time
import threading
import seedFinder
import webbrowser
import pyperclip

from gui.introduction import Ui_introductionWindow
from gui.main import mainWindow
from gui.mode1 import Ui_mode1Window
from gui.mode2 import Ui_mode2Window
from gui.msg import Ui_msgWindow

class introductionWindow(QMainWindow, Ui_introductionWindow):
    def __init__(self, parent=None):
        super(introductionWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))
class mode1Window(QWidget, Ui_mode1Window):
    def __init__(self, parent=None):
        super(mode1Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setAttribute(Qt.WA_DeleteOnClose)
class mode2Window(QWidget, Ui_mode2Window):
    def __init__(self, parent=None):
        super(mode2Window, self).__init__(parent)
        self.setupUi(self) 
        self.setWindowIcon(QIcon("icon.ico"))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.waveTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.waveTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.waveTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
class msgWindow(QDialog, Ui_msgWindow):
    def __init__(self, parent=None):
        super(msgWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint)

class signalStore(QObject):
    textUpdate = Signal(str)

class waveRequire:
    def __init__(self, level_beginning, level_ending, idNeeded, idRefused):
        self.level_beginning = level_beginning
        self.level_ending = level_ending
        self.idNeeded = idNeeded
        self.idRefused = idRefused
    def __eq__(self, other):
        return self.level_beginning == other.level_beginning and self.level_ending == other.level_ending and self.idNeeded == other.idNeeded and self.idRefused == other.idRefused

class calculator:
    #工具类&初始化
    def __init__(self):
        extra = {'density_scale': '-1'}
        self.sceneName = {
            "DE(白天无尽,Day Endless)" : "DAY",
            "NE(夜晚无尽,Night Endless)" : "NIGHT",
            "PE(泳池无尽,Pool Endless)" : "POOL",
            "FE(雾夜无尽,Fog Endless)" : "FOG",
            "RE(屋顶无尽,Roof Endless)" : "ROOF",
            "ME(月夜无尽,Moon Endless)" : "MOON",
            "MGE(蘑菇园无尽,Mushroom Garden Endless)" : "MG",
            "AQE(水族馆无尽,Aquarium Endless)" : "AQ"
            }
        self.typeName = bidict({'普通' : 0, '旗帜' : 1, '路障' : 2, '撑杆' : 3, '铁桶' : 4, '读报' : 5, '铁门' : 6, '橄榄' : 7, '舞王' : 8, '伴舞' : 9, '鸭子' : 10, '潜水' : 11, '冰车' : 12, '雪橇' : 13, '海豚' : 14, '小丑' : 15, '气球' : 16, '矿工' : 17, '跳跳' : 18, '雪人' : 19, '蹦极' : 20, '扶梯' : 21, '投篮' : 22, '白眼' : 23, '小鬼' : 24, '僵王' : 25, '豌豆' : 26, '坚果' : 27, '辣椒' : 28, '机枪' : 29, '窝瓜' : 30, '高坚果' : 31, '红眼' : 32})
        self.app = QApplication(sys.argv)
               
        apply_stylesheet(self.app, 'dark_lightgreen.xml', invert_secondary=False, extra=extra)
        self.store = signalStore()
        self.store.textUpdate.connect(self.msgUpdate)
        self.introWindowInit()

    def start(self):
        self.introW.show()
        sys.exit(self.app.exec_())

    def rBtnGroupClicked(self, sender):
        if sender == "mode1":
            btn = self.mode1W.sceneGroup.checkedButton()            
            self.scene = self.sceneName[btn.text()]
        elif sender == "mode2":
            btn = self.mode2W.sceneGroup.checkedButton()            
            self.scene = self.sceneName[btn.text()]
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
        self.introW = introductionWindow()
        self.introW.start_btn.clicked.connect(self.showMainWindow)
        self.introW.exit_btn.clicked.connect(lambda : self.app.quit())
        self.introW.help_btn.clicked.connect(lambda : webbrowser.open(Path.cwd() / "help" / "help.html"))

    #主窗口
    def mainWindowInit(self):
        self.mainW = mainWindow()
        self.mode1WindowInit()
        self.mode2WindowInit()  
        
        self.mainW.tabWidget.addTab(self.mode1W, "模式1")
        self.mainW.tabWidget.addTab(self.mode2W, "模式2")
    def showMainWindow(self):
        self.mainWindowInit()
        self.mainW.show()

    #模式1
    def mode1WindowInit(self):
        self.mode1W = mode1Window()
        self.mode1W.calc_btn.clicked.connect(self.mode1Calc)
        self.mode1W.sceneGroup.buttonClicked.connect(lambda : self.rBtnGroupClicked("mode1"))
        self.mode1W.return_btn.clicked.connect(lambda : self.mainW.close())
        self.mode1W.help_btn.clicked.connect(lambda : webbrowser.open(Path.cwd() / "help" / "help.html"))
    def mode1Calc(self):
        try:
            uid = self.mode1W.uid_Input.value()
            mode = self.mode1W.mode_Input.value()

            flags_beginning = self.mode1W.startFlag_Input.value()
            flags_ending = self.mode1W.endFlag_Input.value()

            level_beginning = (flags_beginning - 1) // 2
            level_ending = flags_ending // 2

            seed = self.mode1W.seed_Input.value()

            if not flags_beginning % 2 or flags_ending % 2:
                QMessageBox.critical(self.mode1W, "错误", "上半轮旗数为奇数，下半轮旗数为偶数！") 
                return
            if level_ending - level_beginning >= 20:
                QMessageBox.critical(self.mode1W, "错误", "请不要一次计算过大的范围！")
                return
            if hasattr(self, "scene") == False:
                QMessageBox.critical(self.mode1W, "错误", "请选择场景！")
                return
        except ValueError:
            QMessageBox.critical(self.mode1W, "错误", "请按要求输入！") 
        except SyntaxError:
            QMessageBox.critical(self.mode1W, "错误", "请按要求输入！") 
        except:
            QMessageBox.critical(self.mode1W, "错误", "出现意外的异常！")
        else:
            try:
                rst = ""
                for lvl in range(level_beginning, level_ending):
                    zombies = seedFinder.appear(uid, mode, self.scene, lvl, seed)
                    rst += "%d旗到%d旗的出怪为：" % (lvl * 2 + 1, lvl * 2 + 2)
                    amount = 0
                    for i in range(len(zombies)):
                        if zombies[i]:
                            amount += 1
                            rst += self.typeName.inverse[i] + " "
                    rst += "共%d种\n\n" % amount
                pyperclip.copy(rst)
                QMessageBox.information(self.mode1W, "计算结果", rst)
            except:
                QMessageBox.critical(self.mode1W, "错误", "出现意外的异常！")

    #模式2
    def mode2WindowInit(self):
        self.mode2W = mode2Window()
        self.mode2W.calc_btn.clicked.connect(self.mode2Calc)
        self.mode2W.join_btn.clicked.connect(self.joinTable)
        self.mode2W.del_btn.clicked.connect(self.delTable)
        self.mode2W.return_btn.clicked.connect(lambda : self.mainW.close())
        self.mode2W.help_btn.clicked.connect(lambda : webbrowser.open(Path.cwd() / "help" / "help.html"))
        self.mode2W.sceneGroup.buttonClicked.connect(lambda : self.rBtnGroupClicked("mode2"))
        for box in self.mode2W.needGroup.findChildren(QCheckBox):
            box.stateChanged.connect(self.nCheckBoxClicked)
        for box in self.mode2W.refuseGroup.findChildren(QCheckBox):
            box.stateChanged.connect(self.rCheckBoxClicked)
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
                QMessageBox.critical(self.mode2W, "错误", "请至少添加一条要求！")
                return

            waveBeginning = sorted([i.level_beginning for i in self.wave])
            waveEnding = sorted([i.level_ending for i in self.wave])
            for i in range(1, len(waveBeginning)):
                if waveBeginning[i] < waveEnding[i - 1]:
                    QMessageBox.critical(self.mode2W, "错误", "请检查要求的波数区间有重叠！")
                    return
            
            self.wave.sort(key=lambda x : x.level_ending)
            maxWave = self.wave[-1].level_ending - 1
            idNeeded = [[] for i in range(maxWave)]
            idRefused = [[] for i in range(maxWave)]

            for eachWave in self.wave:
                for i in range(eachWave.level_beginning - 1, eachWave.level_ending - 1):
                    idNeeded[i] = eachWave.idNeeded
                    idRefused[i] = eachWave.idRefused

        except ValueError:
            QMessageBox.critical(self.mode2W, "错误", "请按要求输入！") 
        except SyntaxError:
            QMessageBox.critical(self.mode2W, "错误", "请按要求输入！") 
        except:
            QMessageBox.critical(self.mode2W, "错误", "出现意外的异常！")
        else:
            self.finder = seedFinder.requestToSeed(uid, mode, self.scene, self.wave[0].level_beginning, self.wave[-1].level_ending, seed)
            self.thdList = (threading.Thread(target=self.mode2CalcThread, args=(idNeeded, idRefused)), 
                            threading.Thread(target=self.seedLogger))
            for thd in self.thdList:
                thd.start()
            self.msgWindowInit()   
    def mode2CalcThread(self, idNeeded, idRefused):
        self.result = self.finder.calc(idNeeded, idRefused)
        if self.finder.overflow:
            self.store.textUpdate.emit("没有找到满足条件的种子！")
        else:
            self.calcDone = True
    def seedLogger(self):
        while self.calcDone == False and self.finder.overflow == False:
            self.store.textUpdate.emit("正在计算，请稍候……\n当前已检索至种子0x%x" % (
                self.finder.seed))
            time.sleep(0.2)
        if not self.finder.overflow:
            pyperclip.copy(self.result)
            self.store.textUpdate.emit("出怪满足要求的种子为：%x" % (self.result))           
    def joinTable(self):
        flags_beginning = self.mode2W.startFlag_Input.value()
        flags_ending = self.mode2W.endFlag_Input.value()
        level_beginning = (flags_beginning - 1) // 2
        level_ending = flags_ending // 2

        if hasattr(self, "scene") == False:
            QMessageBox.critical(self.mode2W, "错误", "请选择场景！")
            return
        for i in self.idNeeded:
            if i in self.idRefused:
                QMessageBox.critical(self.mode2W, "错误", "需要与不需要的种类有冲突！")
                return
        if not flags_beginning % 2 or flags_ending % 2:
            QMessageBox.critical(self.mode2W, "错误", "上半轮旗数为奇数，下半轮旗数为偶数！")
            return
        if level_ending - level_beginning >= 20:
                QMessageBox.critical(self.mode2W, "错误", "所求关数过多，过于掉节操！")
                raise
        if len(self.idNeeded) > 11:
            QMessageBox.critical(self.mode2W, "错误", "需求僵尸过多！")
            return
        if len(self.idRefused) > 10:
            QMessageBox.critical(self.mode2W, "错误", "不想要的僵尸过多！")
            return
        if 2 in self.idRefused and 5 in self.idRefused:
            QMessageBox.critical(self.mode2W, "错误", "路障报纸必出其一！")
            return

        idNeededShow = [self.typeName.inverse[i] for i in self.idNeeded]
        idRefusedShow = [self.typeName.inverse[i] for i in self.idRefused]
    
        waveShow = ((flags_beginning, flags_ending), idNeededShow, idRefusedShow)

        waveInstance = waveRequire(level_beginning, level_ending, list(self.idNeeded), list(self.idRefused))
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
            for i in range(len(idNeeded)):
                idNeeded[i] = self.typeName[idNeeded[i]]
            for i in range(len(idRefused)):
                idRefused[i] = self.typeName[idRefused[i]]
            waveInstance = waveRequire(level_beginning, level_ending, idNeeded, idRefused)
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
    def msgWindowInit(self):
        self.msgW = msgWindow()    
        self.msgW.return_btn.clicked.connect(self.msgExit)
        self.msgW.show()
    def msgExit(self):
        self.finder.stopThread = True
        isExit = False
        while isExit == False:
            isExit = not(self.thdList[0].is_alive()) and not(self.thdList[1].is_alive())
        self.msgW.close()

if __name__ == "__main__":
    calculator().start()