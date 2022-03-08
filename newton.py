import functions
import time
import numpy as np

def execute_fx(a: float, b: float, c: float, d: float, x0: float, stopping_condition: int, stopping_value):
    xn = x0
    if stopping_condition == 1: 
        for _ in range(stopping_value):
            if functions.f_second_derivative(xn, a, b) == 0:
                break
            xn = xn - functions.f_first_derivative(xn, a, b, c) / functions.f_second_derivative(xn, a, b)
    elif stopping_condition == 2:
        while functions.f(xn, a, b, c, d) >= stopping_value:
            if functions.f_second_derivative(xn, a, b) == 0:
                break
            xn = xn - functions.f_first_derivative(xn, a, b, c) / functions.f_second_derivative(xn, a, b)   
    elif stopping_condition == 3:
        t_end = time.time() + stopping_value
        print("Please wait for a while...")
        while time.time() < t_end:
            if functions.f_second_derivative(xn, a, b) == 0:
                break
            xn = xn - functions.f_first_derivative(xn, a, b, c) / functions.f_second_derivative(xn, a, b)   
    return (xn, functions.f(xn, a, b, c, d))

def execute_gx(A, b, c: float, x0, stopping_condition: int, stopping_value):
    xn = x0
    if stopping_condition == 1:
        for _ in range(stopping_value):
            if np.any(functions.g_second_gradient(A)) == 0:
                break
            xn = xn - np.dot(np.linalg.inv(functions.g_second_gradient(A)), functions.g_first_gradient(xn, A, b))
    elif stopping_condition == 2:
        while functions.g(xn, A, b, c) >= stopping_value:
            if np.any(functions.g_second_gradient(A)) == 0:
                break 
            xn = xn - np.dot(np.linalg.inv(functions.g_second_gradient(A)), functions.g_first_gradient(xn, A, b))
    elif stopping_condition == 3:
         t_end = time.time() + stopping_value
         print("Please wait for a while...")
         while time.time() < t_end:
             if np.any(functions.g_second_gradient(A)) == 0:
                break
             xn = xn - np.dot(np.linalg.inv(functions.g_second_gradient(A)), functions.g_first_gradient(xn, A, b))
    return (xn, functions.g(xn, A, b, c))