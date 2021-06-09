class MyRangeIterator:
    def __init__(self, top):
        self._top = top
        self._current = 0

    def __iter__(self):
        return self

    def __next__():
        if self._current >= self._top:
            raise StopIteration
        current = self._current
        self._current += 1
        return current
