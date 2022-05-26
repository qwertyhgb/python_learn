# 逐行显示文件
from numpy import number


with open('message.txt', 'r') as file:
    number = 0
    while True:
        number += 1
        line = file.readline()
        if line == '':
            break
        print(number, line, end=' ')
