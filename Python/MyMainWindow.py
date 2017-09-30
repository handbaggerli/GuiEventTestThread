# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadList = []

    def closeEvent(self, event):
        print("Close Event was ich hunder Jahre gesucht habe")
        while len(self.threadList) > 0:
            threadGui = self.threadList[0][2]
            threadGui.stopThread()



    def setThreadList(self, threadList):
        self.threadList = threadList