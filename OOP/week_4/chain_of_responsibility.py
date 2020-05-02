class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

def EventGet(obj):
    if issubclass(obj, int):
        return 'get_int'
    elif issubclass(obj, float):
        return 'get_float'
    elif issubclass(obj, str):
        return 'get_str'


def EventSet(obj):
    if isinstance(obj, int):
        return str(obj) + ' set_int'
    elif isinstance(obj, float):
        return str(obj) + ' set_float'
    elif isinstance(obj, str):
        return obj + ' set_str'

class NullHandler:
    def __init__(self, successor=None):
    # передаём следующее звено
        self.__successor = successor

    def handle(self, obj, event):  # обработчик
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event == 'get_int':
            return obj.integer_field
        elif event.find('set_int') > 0:
            obj.integer_field = int(event.split(' ')[0])
        else:
            return super().handle(obj, event)

class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event == 'get_float':
            return obj.float_field
        elif event.find('set_float') > 0:
            obj.float_field = float(event.split(' ')[0])
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event == 'get_str':
            return obj.string_field
        elif event.find('set_str') > 0:
            obj.string_field = event.split(' ')[0]
        else:
            return super().handle(obj, event)


obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
chain.handle(obj, EventGet(int))

chain.handle(obj, EventSet(2.2))
print(chain.handle(obj, EventGet(float)))
