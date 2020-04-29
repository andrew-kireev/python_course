import os.path
from tempfile import gettempdir
import tempfile


class File:
    def __init__(self, path):
        if not os.path.exists(path):
            self.path_ = path
            with open(self.path_, 'w') as f:
                pass
        else:
            self.path_ = path

    def read(self):
        with open(self.path_, 'r') as f:
            return f.read()

    def write(self, msg):
        with open(self.path_, 'w') as f:
            f.write(msg)

    def __str__(self):
        return self.path_

    def __add__(self, other):
        assert isinstance(other, File)

        temp_dir = gettempdir()
        temp_path = os.path.join(temp_dir, "temp.txt")

        file = File(temp_path)
        file.write(self.read() + other.read())
        return file

    def __iter__(self):
        self.cur_byte = 0
        self.num_bytes = os.path.getsize(self.path_)
        return self

    def __next__(self):
        if self.cur_byte >= self.num_bytes:
            raise StopIteration("EOF")

        with open(self.path_, "r") as f:
            f.seek(self.cur_byte)
            row = f.readline()
            self.cur_byte = f.tell()
        return row

file = File('/Users/@@@@@/cars/venv/op.txt')


