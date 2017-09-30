# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_MainWindow import Ui_MainWindow
from EventCommunicator import EventCommunicator
from PyQt5.QtCore import pyqtSlot
from Ue_ThreadGuiNumber import Ue_ThreadGuiNumber
from Ue_ThreadGuiText import Ue_ThreadGuiText

class Ue_MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.threadList = []
        self.threadIndexText = 0
        self.threadIndexNumber = 0
        self.threadTextText = "Tread_Text_GUI_{index}"
        self.threadTextNumber = "Tread_Number_GUI_{index}"


    def connect_user_events(self):
        self.event_comm = EventCommunicator()
        self.pushButtonStartNumberGui.clicked.connect(self.__startThreadNumber)
        self.pushButtonStartTextGui.clicked.connect(self.__startThreadText)
        self.pushButtonConnectLog0.clicked.connect(self.__connectLog0)
        self.pushButtonDisconnectLog0.clicked.connect(self.__disconnectLog0)
        self.pushButtonConnectLog1.clicked.connect(self.__connectLog1)
        self.pushButtonDisconnectLog1.clicked.connect(self.__disconnectLog1)
        self.event_comm.write_log_event.connect(self.__writeLogEvent)
        self.event_comm.stop_thread.connect(self.__stopThread)
        self.__refreshThreadText()


    @pyqtSlot()
    def __startThreadNumber(self):
        threadWindowNumber = QtWidgets.QDialog()
        numberWindow = Ue_ThreadGuiNumber(event_comm=self.event_comm, identification=self.threadTextNumber)
        numberWindow.setupUi(threadWindowNumber)
        numberWindow.connect_user_events()
        self.threadList.append([self.threadTextNumber, threadWindowNumber, numberWindow, False, False])
        self.threadIndexNumber += 1
        threadWindowNumber.show()
        self.__refreshThreadText()


    @pyqtSlot()
    def __startThreadText(self):
        threadWindowText = QtWidgets.QDialog()
        textWindow = Ue_ThreadGuiText(event_comm=self.event_comm, identification=self.threadTextText)
        textWindow.setupUi(threadWindowText)
        textWindow.connect_user_events()
        self.threadList.append([self.threadTextText, threadWindowText, textWindow, False, False])
        self.threadIndexText += 1
        threadWindowText.show()
        self.__refreshThreadText()


    @pyqtSlot()
    def __connectLog0(self):
        for i in range(len(self.threadList)):
            if self.threadList[i][0] == self.comboBoxThreads.currentText():
                self.threadList[i][3] = True
                return

    @pyqtSlot()
    def __disconnectLog0(self):
        for i in range(len(self.threadList)):
            if self.threadList[i][0] == self.comboBoxThreads.currentText():
                self.threadList[i][3] = False
                return

    @pyqtSlot()
    def __connectLog1(self):
        for i in range(len(self.threadList)):
            if self.threadList[i][0] == self.comboBoxThreads.currentText():
                self.threadList[i][4] = True
                return

    @pyqtSlot()
    def __disconnectLog1(self):
        for i in range(len(self.threadList)):
            if self.threadList[i][0] == self.comboBoxThreads.currentText():
                self.threadList[i][4] = False
                return

    @pyqtSlot()
    def __writeLogEvent(self, identification, text):
        for threadIdent, threadWindow, threadGui, writeLog0, writeLog1 in self.threadList:
            if identification == threadIdent:
                if writeLog0:
                    self.textEditLog0.append("{identification}: {text}".format(identification=identification, text=text))
                if writeLog1:
                    self.textEditLog1.append("{identification}: {text}".format(identification=identification, text=text))
                return



    @pyqtSlot()
    def __stopThread(self, identification):
        print("__stopThread {identification}".format(identification=identification))
        for threadIdent, threadWindow, threadGui, writeLog0, writeLog1 in self.threadList:
            if identification == threadIdent:
                threadWindow.close()
                self.threadList.remove([threadIdent, threadWindow, threadGui, writeLog0, writeLog1])
                break
        self.__refreshThreadText()


    def __refreshThreadText(self):
        self.threadTextText = "Tread_Text_GUI_{index}".format(index=self.threadIndexText)
        self.threadTextNumber = "Tread_Number_GUI_{index}".format(index=self.threadIndexNumber)
        self.lineEditThreadIdentificationText.setText(self.threadTextText)
        self.lineEditThreadIdentificationNumber.setText(self.threadTextNumber)
        self.comboBoxThreads.clear()
        comboList = [item[0] for item in self.threadList]
        comboList.sort()
        for element in comboList:
           self.comboBoxThreads.addItem(element)



    def closeMainWindow(self):
        print("CloseMainwindow")


