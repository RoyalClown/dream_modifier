from interaction.fileReader import FileReader
from data.attributes import *


class Console:
    def __init__(self):
        self.file_reader = FileReader()

    def role(self):
        choices = {'1': self.file_reader.set_attributes()}
        text = input("1.Attack Qualification:{}\n"
                     "2.Defense Qualification:{}\n".format(Attack_Qualification, Defense_Qualification))
        input_text = text.split()

    def main(self):
        choices = {'1': self.role, }
        choice = input("1.Role Information\n"
                       "2.Pet Information\n"
                       "3.Goods Information\n"
                       "0.Exit\n")
        choices[choice]()


if __name__ == "__main__":
    console = Console()
    console.main()
