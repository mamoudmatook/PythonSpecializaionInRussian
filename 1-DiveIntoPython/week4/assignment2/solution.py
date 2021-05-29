class Value():
    def __init__(self):
        self._value = None

    def __set__(self, obj, value):
        self._value = value
    
    def __get__(self, obj, obj_type):
        return self._value - obj.commission * self._value 