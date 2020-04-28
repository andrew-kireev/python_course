


class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        str = '332'
        try:
            fd = open(self.path, 'r')
            str = fd.read()
            fd.close()
        except FileNotFoundError:
            str = ''
        finally:
            return str






f = FileReader("/Users/andrewkireev/Documets/pythn_course/task3.py")
print(f.read())