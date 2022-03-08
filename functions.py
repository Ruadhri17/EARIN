# import numpy as np

def f_original(x, a, b, c, d):
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d

# derivative of original function - used for Newton's method
def f(x, a, b, c):
    return 3 * a * pow(x, 2) + 2 * b * x + c

# second derivative of original function - used for Newton's method    
def f_prime(x, a, b):
    return 6 * a * x + 2 * b

def g(x, A, b, c, d):
    return #write function

def g_prime(x, a, b, c):
    return #write function