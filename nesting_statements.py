"""
# first nested statements in python
# Author: Anton Mueller <anton.mueller@deutschebahn.com>
"""

test = 11

if test > 0:
    if test > 10  and test < 15:
        print(" Positive in range: 10-15")
    else:
        print("Positive")
elif test < 0:
    print("Negative")
else:
    print("ZERO")

test2 = 0
if test2 == 0: print("One line!")
