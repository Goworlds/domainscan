# coding=utf-8
import os
import sys

if len(sys.argv) <= 1:
    print('usage: main.py file.txt')
    sys.exit()
path = sys.argv[1]
f = open(path,'r')
line = f.readline()
while line:
    print(line)
    #print(a)
    #a += 1
    line = f.readline()
    os.system('aquatone-discover -domain ' + line)
f.close()
