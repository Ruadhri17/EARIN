import numpy as np
import time
import functions


# a: float, b: float, c: float, d: float, x0: float,
def execute_fx(a: float, b: float, c: float, d: float, x0: float, stopping_condition, stopping_value):
    learn_rate = 0.05
    tolerance = 1e-06
    xn = x0
    if stopping_condition == 1: 
        for _ in range(stopping_value):
            diff = -learn_rate * functions.f_first_derivative(xn, a, b, c)
            if abs(diff) <= tolerance:
                break
            xn += diff
    elif stopping_condition == 2:
        while functions.f(xn, a, b, c, d) >= stopping_value:
            diff = -learn_rate * functions.f_first_derivative(xn, a, b, c)
            if abs(diff) <= tolerance:
                break
            xn += diff
    elif stopping_condition == 3:
        t_end = time.time() + stopping_value
        print("Please wait for a while...")
        while time.time() < t_end:
            diff = -learn_rate * functions.f_first_derivative(xn, a, b, c)
            if abs(diff <= tolerance):
                break
            xn += diff
    return (xn, functions.f(xn, a, b, c, d))

def execute_gx(A, b, c: float, x0, stopping_condition, stopping_value):
    learn_rate = 0.2
    tolerance = 1e-06
    xn = x0
    if stopping_condition == 1: 
        for _ in range(stopping_value):
            diff = np.multiply(-learn_rate, functions.g_first_gradient(xn, A, b))
            if np.all(np.abs(diff) <= tolerance):
                break
            xn += diff
    elif stopping_condition == 2:
        while functions.g(xn, A, b, c) > stopping_value:
            diff = np.multiply(-learn_rate, functions.g_first_gradient(xn, A, b))
            if np.all(np.abs(diff) <= tolerance):
                break
            xn += diff
    elif stopping_condition == 3:
        t_end = time.time() + stopping_value
        print("Please wait for a while...")
        while time.time() < t_end:
            diff = np.multiply(-learn_rate, functions.g_first_gradient(xn, A, b))
            if np.all(np.abs(diff) <= tolerance):
                break
    return (xn, functions.g(xn, A, b, c))
