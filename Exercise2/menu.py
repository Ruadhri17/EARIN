import input_validator
import numpy as np
from sys import platform
import os

PROVIDE_COEFFICIENT_A_MSG_FOR_FX = "Provide values for matrix A of "
PROVIDE_COEFFICIENT_B_MSG_FOR_FX = "Provide values for vector b of "
PROVIDE_COEFFICIENT_C_MSG_FOR_FX = "Provide scalar c: "
PROVIDE_COEFFICIENT_D_MSG_FOR_FX = "Provide size of vectors / matrices: "
PROVIDE_X_FOR_FX_MSG = "Provide values for vector x of "

# def print_main_menu():
#     print("--------------------------------------------------------------------------------")
#     print("Please choose the method you want to use by providing the number.")
#     print("1. Gradient descent method")
#     print("2. Newton's method") 
#     print("3. Exit")
#     print("--------------------------------------------------------------------------------")


# def choose_restart_method():
#     while True:
#         user_choice = input_validator.validate_boolean_choice_input(RESTART_MODE_MSG)
#         if user_choice:
#             break
#     return user_choice

def provide_coefficients_fx():
    problem_dimensionality = input_validator.validate_integer_input(PROVIDE_COEFFICIENT_D_MSG_FOR_FX)
    while True:
        x = np.array(input_validator.validate_vector_input(PROVIDE_X_FOR_FX_MSG, problem_dimensionality))
        if x.any():
            break
    while True:
        b = np.array(input_validator.validate_vector_input(PROVIDE_COEFFICIENT_B_MSG_FOR_FX, problem_dimensionality))
        if b.any():
            break
    c = input_validator.validate_number_input(PROVIDE_COEFFICIENT_C_MSG_FOR_FX)

    while True:
        A = input_validator.validate_positive_definite_matrix_input(PROVIDE_COEFFICIENT_A_MSG_FOR_FX, problem_dimensionality)
        if A.any():
            break
    
    return (A, b, c, problem_dimensionality, x)

def clear_screen():
    if platform == "linux" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system('cls')