"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0!")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if b <=0 or a == 1 or a == 0:
        raise ZeroDivisionError("Illegal argument given...")
    return math.log(b,a)# use math library/raise ValueError

def exponent(a, b): return a**b

