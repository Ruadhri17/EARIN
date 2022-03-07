# import numpy as np

# derivative of original function - used for Newton's method
def f(x, a, b, c, d):
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d

# second derivative of original function - used for Newton's method    
def f_prime(x, a, b, c):
    return 3 * a * pow(x, 2) + 2 * b * x + c

def g(x, A, b, c, d):
    return 

# def g_prime(x, a, b, c):
