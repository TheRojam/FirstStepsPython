#!/usr/bin/python3
"""
# Hand on Lab 1  – Drawing a ASCII Shape // Loops and Co
# Author: Anton Mueller <anton.mueller@deutschebahn.com>
"""

length = 10
astr = "*"

for i in range(length):
    for j in range(length-i):
        print(" ", end='')
    print(astr)
    astr += "**"

length -= 1
space = 1
astrNum = ((length*2)-1)
astr = "*" * astrNum
for i in range(length):
    print(" " + space * " " + astr)
    astrNum -= 2
    astr = "*" * astrNum
    space += 1
