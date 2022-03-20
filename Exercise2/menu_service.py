import menu
import genetic_algorithm

def run_fx():
    (A, b, c, problem_dimensionality, x) = menu.provide_coefficients_fx()
    # (xn, gx) = genetic_algorithm(A, b, c, x)
    # print("Found solution of x: ", xn)
    # print("Function value: ", fx)