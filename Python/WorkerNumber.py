# -*- coding: utf-8 -*-

from threading import Thread, Condition
import time
import operator

class WorkerNumber(Thread):
    def __init__(self, event_comm, identification):
        Thread.__init__(self)
        self.deamon = True
        self.paused = True
        self.stopped = False
        self.state = Condition()
        self.event_comm = event_comm
        self.identification = identification
        self.numberList = [2, 3]

    def run(self):
        self.resume()
        aktNumber = 5
        for number in self.numberList:
            self.event_comm.write_log_event.emit(self.identification, str(number))
            time.sleep(.5)
        while True:
            with self.state:
                if self.paused:
                    self.state.wait()
                if self.stopped:
                    return
            if self.__calcNext(aktNumber):
                self.numberList.append(aktNumber)
                self.event_comm.write_log_event.emit(self.identification, str(aktNumber))
                time.sleep(.5)
            aktNumber += 2

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

    def __calcNext(self, aktNumber):
        for number in self.numberList:
            if operator.mod(aktNumber, number) == 0:
                return False
        return True

