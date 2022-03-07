import functions
import menu

def execute_fx(x0: float, a: float, b: float, c: float, d: float, stopping_condition: int, stopping_value):
    xn = x0
    if stopping_condition == 1: 
        for _ in range(stopping_value):
            xn = xn - functions.f(xn, a, b, c, d) / functions.f_prime(xn, a, b, c)
    elif stopping_condition == 2:
        while abs(xn) > stopping_value:
            xn = xn - functions.f(xn, a, b, c, d) / functions.f_prime(xn, a, b, c)             
    return (xn, functions.f(xn, a, b, c, d))

# def execute_gx():