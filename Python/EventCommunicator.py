# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal, QObject
from typing import Any, TypeVar, Generic

class EventCommunicator(QObject):

    write_log_event = pyqtSignal(str, str)
    stop_thread = pyqtSignal(str)
