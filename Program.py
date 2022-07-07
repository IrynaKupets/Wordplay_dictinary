# -*- coding: utf-8 -*-
#======================================================================================================
#                             МАГІСТЕРСЬКА КВАЛІФІКАЦІЙНА РОБОТА
#           
#           Виконала студентка групи ФЛПЛ-22:
#                       Купець Ірина
#      Головний модуль словника гри слів: Program.py
#
#=======================================================================================================

import sys,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from FrmMainProgram import *
from DictionaryAbr import *


class MyWinDic(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('dictionary.png'))

        list = DictionaryWords().DictionaryWord()
        item = []
        for i in list:
            item = QtWidgets.QListWidgetItem(i["Word"])
            self.ui.listWidget.addItem(item)
        self.ui.statusbar.showMessage("Number of entries : "+str(len(list)))

        self.ui.listWidget.itemClicked.connect(self.Clicked)
        self.ui.pushButton.clicked.connect(self.Search)
        self.ui.actionExit.triggered.connect(self.Exit)
        self.ui.actionHelp.triggered.connect(self.openHelp)
        self.ui.actionAbout_program.triggered.connect(self.AboutWindow)

    def Clicked(self, selectText):
        self.ui.textEdit_2.clear()
        self.ui.textEdit_3.clear()
        list = DictionaryWords().DictionaryWord()
        for item in list:
            if selectText.text() == item["Word"]:
                self.ui.textEdit.setText("")
                textTextEdit = "<span style=\" font-size:10pt;\" >" + item["Wordplay_Example"] + "</span>"
                self.ui.textEdit_3.append(textTextEdit)
                textTextEdit = "<span style=\" font-size:10pt;  color:#0000ff;\" >" +  item["UkrainianTranslation"] +"</span>"
                self.ui.textEdit_2.append(textTextEdit)

    def Exit(self, setMenu):
        buttonReply = QtWidgets.QMessageBox.question(self, 'Confirm Main Window', "Do you want to quit?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            sys.exit(app.exec_())


    def Search(self):
        list = []
        self.ui.listWidget.clear()
        text = self.ui.textEdit.toPlainText()
        list = DictionaryWords().DictionaryWord()
        for item in list:
            if text in item["Word"]:
                elem = QtWidgets.QListWidgetItem(item["Word"])
                self.ui.listWidget.addItem(elem)
        x = 0.0
        while x < 100:
            x += 0.0001
        self.ui.progressBar.setValue(x)


    def AboutWindow(self):
        QtWidgets.QMessageBox.about(self, "About program",
                                "\t“Peculiarities of Ukrainian Translation of Wordplay \n\tin the Death Series Books of Terry Pratchett’s Discworld Saga”\n\tRuntime version : 1.1\n\t"
                                "Kupets Iryna\n\t"
                                "email: iryna.yu.kupets@gmail.com\n\t"
                                    "Copyright ©  2020 ")

# ====================  Help =======================================================================================
    def openHelp(self):
        if os.name == 'nt':
            os.popen('hh.exe "paper.chm"')
        if os.name == 'posix':
            os.popen("open -a 'CHM Reader' help.chm")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("#centralwidget { background-color: qlineargradient(spread:pad, x1:0.683, y1:1, x2:1, y2:0, stop:0 rgba(255,222,173,255), stop:1 rgba(230,230,250, 255)); }")
    app.setStyleSheet("#centralwidget { background-color: qlineargradient(spread:pad, x1:0.683, y1:1, x2:1, y2:0, stop:0 rgba(255,222,173,255), stop:1 rgba(230,230,250, 255)); }")
    ex = MyWinDic()
    ex.show()
    sys.exit(app.exec_())