import numpy as np
import functions

def execute_fx(gradient, x, y, start, learn_rate=0.1, n_iter=50, tolerance=1e-06):
    vector = start
    for _ in range(n_iter):
        diff = -learn_rate * np.array(functions.f(x, y, vector))
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff
    return vector

def execute_gx():
    print("gradient descent")