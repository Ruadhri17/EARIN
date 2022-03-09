import numpy as np

def f(x, a, b, c, d):
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d

# derivative of original function - used for Newton's method
def f_first_derivative(x, a, b, c):
    return 3 * a * pow(x, 2) + 2 * b * x + c

# second derivative of original function - used for Newton's method    
def f_second_derivative(x, a, b):
    return 6 * a * x + 2 * b

# c + b'x + x'Ax
def g(x, A, b, c):
    return c + np.dot(np.transpose(b), x) + np.dot(np.dot(np.transpose(x), A), x)
# 
def g_first_gradient(x, A, b):
    #b+A*x+A'*x
    return b + np.dot(A, x) + np.dot(np.transpose(A), x)

def g_second_gradient(A):
    #A'+A
    return np.transpose(A) + A
