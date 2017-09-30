# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Ue_MainWindow import Ue_MainWindow
from MyMainWindow import MyMainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow() # Uberschreiben um alle Threads beim Schliesen noch killen zu koennen.
    ui = Ue_MainWindow()
    ui.setupUi(MainWindow)
    ui.connect_user_events()
    MainWindow.setThreadList(ui.threadList)
    MainWindow.show()
    app.aboutToQuit.connect(ui.closeMainWindow)
    sys.exit(app.exec_())


