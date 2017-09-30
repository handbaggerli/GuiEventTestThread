# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitRepos\GuiEventTestThread\GuiBuilder\GuiEventTestThread\threadgui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThreadGui(object):
    def setupUi(self, ThreadGui):
        ThreadGui.setObjectName("ThreadGui")
        ThreadGui.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ThreadGui)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ThreadGui)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditIdentification = QtWidgets.QLineEdit(ThreadGui)
        self.lineEditIdentification.setEnabled(False)
        self.lineEditIdentification.setObjectName("lineEditIdentification")
        self.horizontalLayout.addWidget(self.lineEditIdentification)
        self.pushButtonPause = QtWidgets.QPushButton(ThreadGui)
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.horizontalLayout.addWidget(self.pushButtonPause)
        self.pushButtonStop = QtWidgets.QPushButton(ThreadGui)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.horizontalLayout.addWidget(self.pushButtonStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEditLog = QtWidgets.QTextEdit(ThreadGui)
        self.textEditLog.setEnabled(False)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout.addWidget(self.textEditLog)

        self.retranslateUi(ThreadGui)
        QtCore.QMetaObject.connectSlotsByName(ThreadGui)

    def retranslateUi(self, ThreadGui):
        _translate = QtCore.QCoreApplication.translate
        ThreadGui.setWindowTitle(_translate("ThreadGui", "Thread Gui"))
        self.label.setText(_translate("ThreadGui", "Identification:"))
        self.pushButtonPause.setText(_translate("ThreadGui", "Pause"))
        self.pushButtonStop.setText(_translate("ThreadGui", "Stop"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThreadGui = QtWidgets.QWidget()
    ui = Ui_ThreadGui()
    ui.setupUi(ThreadGui)
    ThreadGui.show()
    sys.exit(app.exec_())

