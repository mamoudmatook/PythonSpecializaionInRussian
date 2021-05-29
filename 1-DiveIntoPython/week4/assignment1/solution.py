import os
import tempfile
import uuid
class File:
    def __init__(self, file_path):
        self._file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as fo:
                fo.write('')

    def read(self):
        with open(self._file_path, 'r') as fo:
            return fo.read()

    def write(self, new_str):
        with open(self._file_path, 'w') as fo:
            fo.write(new_str)

    def __add__(self, other):
        new_file = File(os.path.join(tempfile.gettempdir() , str(uuid.uuid1())))
        new_file.write(self.read() + other.read())
        return new_file

    def __str__(self):
        return self._file_path
    
    def __iter__(self):
        self._iter = 0
        with open(self._file_path) as fo:
            self._lines = fo.readlines()
        return self
    
    def __next__(self):
        if self._iter >= len(self._lines):
            raise StopIteration
        line = self._lines[self._iter]
        self._iter += 1
        return line
        
        
        
