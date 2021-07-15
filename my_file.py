import sys
import codecs


class MyFile:
    def __init__(self, filename, encoding=None):
        self.filename = filename
        self.encoding = encoding
        self.file = None

    def read_file(self):
        with open(self.filename, encoding=self.encoding) as file:
            return file.read()

    def read_line(self, n):
        s = ''
        with open(self.filename, encoding=self.encoding) as file:
            for i in range(n):
                s += file.readline()
        return s

    @staticmethod
    def redirect_stdout(file):
        original = sys.stdout
        sys.stdout = file
        return original

    def print_to_file(self, data, mode='w'):
        file = open(self.filename, mode, encoding=self.encoding)
        temp = sys.stdout
        MyFile.redirect_stdout(file)
        print(data)
        MyFile.redirect_stdout(temp)
        file.close()

    def write_file_with_codecs(self, data, mode="w"):
        with codecs.open(self.filename, mode, self.encoding) as temp:
            temp.write(data)

    def write_file(self, data):
        with open(self.filename, "w") as file:
            file.write(data)

    def open(self, mode, encoding='utf-8'):
        self.file = open(self.filename, mode, encoding=encoding)
        return self.file

    def close(self):
        self.file.close()

    @staticmethod
    def debug_print(data, encoding, mode="w"):
        file = open("debug_print.txt", mode, encoding=encoding)
        original_out = MyFile.redirect_stdout(file)
        print(data)
        MyFile.redirect_stdout(original_out)
        file.close()
