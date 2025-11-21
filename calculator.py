"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0: raise ValueError("Cannot pass a negative number...")
        return math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a,b): return math.hypot(a,b)
# First example
def add(a, b): return a + b

def mul(a,b): return a**b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0!")
    return b/a
def exp(a,b): return a**b


def subtract(a, b): return a - b

def logarithm(a, b):
    if b <=0 or a == 1 or a == 0:
        raise ValueError("Illegal argument given...")
    return math.log(b,a)# use math library/raise ValueError


