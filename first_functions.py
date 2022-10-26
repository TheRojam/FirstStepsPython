"""
# first functions in python
# Author: Anton Mueller <anton.mueller@deutschebahn.com>
"""

"""
def name_of_function(param)
    your code
    return == display/print your result
"""


def addition(num1, num2, num3):
    return num1, num2, num3

def division(num1, num2):
    if num2 == 0:
        return "ERROR: Cannot devide by ZERO!"
    else:
        return num1/num2

var1 = 10
var2 = 13
var3 = 352

result = addition(var1, var2, var3)
print("Result of addition:", result)

result = division(var3, var2)
print("Result of division", result)
