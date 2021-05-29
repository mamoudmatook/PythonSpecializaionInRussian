class FileReader:
    def __init__(self, path):
        self.path = path
    
    def read(self):
        try:
            fo = open(self.path, 'r')
            return fo.read()
        except FileNotFoundError:
            return ''

        