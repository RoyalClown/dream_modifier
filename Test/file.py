import re

with open('model.txt', "r+", encoding='utf-8') as f:
    lines = f.readlines()

line_list = lines[1].split()
line_list[1] = '1'
str_line = ' '.join(line_list)
lines[1] = str_line + '\n'
print(lines)

with open('model.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)