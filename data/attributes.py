from interaction.fileReader import FileReader
from Constant.Filedata import *

file_reader = FileReader()
Attack_Qualification = file_reader.get_attributes(*Attack_Qualification)
Defense_Qualification = file_reader.get_attributes(*Defense_Qualification)
