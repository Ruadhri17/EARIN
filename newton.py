import functions
import time
import numpy as np

def execute_fx(a: float, b: float, c: float, d: float, x0: float, stopping_condition: int, stopping_value):
    xn = x0
    if stopping_condition == 1: 
        for _ in range(stopping_value):
            xn = xn - functions.f_first_gradient(xn, a, b, c) / functions.f_second_gradient(xn, a, b)
    elif stopping_condition == 2:
        while abs(xn) > stopping_value:
            xn = xn - functions.f_first_gradient(xn, a, b, c) / functions.f_second_gradient(xn, a, b)   
    elif stopping_condition == 3:
        t_end = time.time() + stopping_value
        print("Please wait for a while...")
        while time.time() < t_end:
            xn = xn - functions.f_first_gradient(xn, a, b, c) / functions.f_second_gradient(xn, a, b)   
    return (xn, functions.f(xn, a, b, c, d))

def execute_gx(A, b: float, c: float, d: float, x0: float, stopping_condition: int, stopping_value):
    xn = x0
    if stopping_condition == 1:
        for _ in range(stopping_value):
            xn = xn - functions.g_first_gradient(xn, A, b, c) / functions.g_second_gradient(xn, A, b, c)
    elif stopping_condition == 2:
        while abs(xn) > stopping_value:
            xn = xn - functions.g_first_gradient(xn, A, b, c) / functions.g_second_gradient(xn, A, b, c)
    elif stopping_condition == 3:
         t_end = time.time() + stopping_value
         print("Please wait for a while...")
         while time.time() < t_end:
             xn = xn - functions.g_first_gradient(xn, A, b, c) / functions.g_second_gradient(xn, A, b, c)
    return (xn, functions.g(xn, A, b, c))