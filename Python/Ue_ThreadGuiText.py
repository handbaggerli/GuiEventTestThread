# -*- coding: utf-8 -*-

from Ui_ThreadGui import Ui_ThreadGui
from WorkerText import WorkerText
from PyQt5.QtCore import pyqtSlot


class Ue_ThreadGuiText(Ui_ThreadGui):
    def __init__(self, event_comm, identification):
        super().__init__()
        self.event_comm = event_comm
        self.identification = identification
        self.worker_paused = False

    def connect_user_events(self):
        self.pushButtonStop.clicked.connect(self.stopThread)
        self.pushButtonPause.clicked.connect(self.__pauseThread)
        self.lineEditIdentification.setText(self.identification)
        self.event_comm.write_log_event.connect(self.__writeLog)
        self.worker = WorkerText(event_comm=self.event_comm, identification=self.identification)
        self.worker.start()

    @pyqtSlot()
    def stopThread(self):
        self.worker.stop()
        self.event_comm.stop_thread.emit(self.identification)

    @pyqtSlot()
    def __pauseThread(self):
        if self.worker_paused:
            self.worker.resume()
            self.worker_paused = False
            self.pushButtonPause.setText("Pause")
        else:
            self.worker.pause()
            self.worker_paused = True
            self.pushButtonPause.setText("Resume")


    @pyqtSlot()
    def __writeLog(self, identification, data):
        if self.identification == identification:
            self.textEditLog.append(data)