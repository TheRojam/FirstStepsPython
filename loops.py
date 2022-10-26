"""
# first steps for python scripting
# Author: Anton Mueller <anton.mueller@deutschebahn.com>
"""

count = 10
while(count > 0):
    print("*" * count)
    count -= 1

for i in range(1, 11):
    print("*" * i)

myStr = "test"
for c in myStr:
    print(c)

for i in range(0, 10):
    if i == 8:
        continue 
        print("In IF:", i)
    print(i)

for i in range (0, 10):
    pass
