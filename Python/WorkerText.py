# -*- coding: utf-8 -*-

from threading import Thread, Condition
import time
import codecs


class WorkerText(Thread):
    def __init__(self, event_comm, identification):
        Thread.__init__(self)
        self.deamon = True
        self.paused = True
        self.stopped = False
        self.state = Condition()
        self.event_comm = event_comm
        self.identification = identification
        self.words = self.__loadText()

    def run(self):
        self.resume()
        while True:
            for word in self.words:
                with self.state:
                    if self.paused:
                        self.state.wait()
                    if self.stopped:
                        return
                self.event_comm.write_log_event.emit(self.identification, word)
                time.sleep(.5)

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # unblock self if waiting

    def pause(self):
        with self.state:
            self.paused = True  # make self block and wait

    def stop(self):
        with self.state:
            self.stopped = True

    def __loadText(self):
        with codecs.open(filename="BlindText.txt", mode="r", encoding="utf-8") as fRead:
            text = fRead.read()
        return text.split()
