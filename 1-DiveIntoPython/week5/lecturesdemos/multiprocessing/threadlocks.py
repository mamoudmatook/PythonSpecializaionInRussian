from threading import Thread
from threading import RLock
class Point:
    def __init__(self):
        self._mutex = RLock()
        self._x = 0
        self._y = 0
    def get(self):
        with self._mutex:
            return (self._x, self._y)
    def set(self, x , y):
        with self._mutex:
            self._x = x
            self._y = y

            