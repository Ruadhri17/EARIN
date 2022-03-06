def f(x, a, b, c, d):
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d
    
def f_prime(x, a, b, c):
    return 3 * a * pow(x, 2) + 2 * b * x + c
