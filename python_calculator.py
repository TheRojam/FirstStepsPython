#!/usr/bin/python3
"""
# Hands on Lab 2 // Aritmethic operations
# functions for arithmetic operations in python
# Author: Anton Mueller <anton.mueller@deutschebahn.com>
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def devide(num1, num2):
    if num2 == 0:
        return "ERROR: Cannot devide by ZERO!"
    else:
        return num1/num2

var1 = 352
var2 = 13

result = add(var1, var2)
print("Result of addition:", result)

result = subtract(var1, var2) 
print("Result of subtract:", result)

result = multiply(var1, var2)
print("Result of multiplication:", result)

result = devide(var1, var2)
print("Result of devide:", result)

var2 = 0
print("Result of second devide", devide(var1, var2))
