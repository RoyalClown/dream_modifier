from Constant.Filedata import *


class FileReader:
    def __init__(self):
        self.path = 'I:\PythonPrj\dream_modifier\Source\\example.txt'

    def open_file(self):
        with open(self.path, 'r+', encoding='utf-8') as f:
            self.lines = f.readlines()
        return self.lines

    def save_file(self, lines):
        with open(self.path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    def get_attributes(self, row_num, col_num):
        lines = self.open_file()
        line_list = lines[row_num].split()
        return line_list[col_num]

    def set_attributes(self):
        pass


if __name__ == "__main__":
    filereader = FileReader()
    attribute = filereader.get_attributes(*Attack_Qualification)
    print(attribute)