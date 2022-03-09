import input_validator
import numpy as np
from sys import platform
import os

PROVIDE_CHOICE_MSG = "Provide your choice: "
MAX_NUMBER_OF_ITERATIONS_MSG = "Provide maximum number of iterations: "
DESIRED_VALUE_MSG = "Provide desired value: "
MAX_COMPUTATION_TIME_MSG = "Provide maximum computation time (seconds): "
WRONG_OPTION_CHOICE_MSG = "The provided option does not exist!"
RESTART_MODE_MSG = "Do you want to use restart mode? Provide option in y/n format: "
RESTART_MODE_REPETITIONS_MSG = "How many times do you want to repeat calculations?  "

PROVIDE_FUNCTION_CHOICE_MSG = "Provide number representing which function you choose: "
PROVIDE_COEFFICIENT_A_MSG_FOR_FX = "Provide coefficient a for F(x) function: "
PROVIDE_COEFFICIENT_B_MSG_FOR_FX = "Provide coefficient b for F(x) function: "
PROVIDE_COEFFICIENT_C_MSG_FOR_FX = "Provide coefficient c for F(x) function: "
PROVIDE_COEFFICIENT_D_MSG_FOR_FX = "Provide coefficient d for F(x) function: "
PROVIDE_X_FOR_FX_MSG = "Provide x value for F(x) function: "

PROVIDE_COEFFICIENT_A_MSG_FOR_GX = "Provide values for matrix A of "
PROVIDE_COEFFICIENT_B_MSG_FOR_GX = "Provide values for vector b of "
PROVIDE_COEFFICIENT_C_MSG_FOR_GX = "Provide scalar c: "
PROVIDE_COEFFICIENT_D_MSG_FOR_GX = "Provide size of vectors / matrices: "
PROVIDE_X_FOR_GX_MSG = "Provide values for vector x of "

def print_main_menu():
    print("--------------------------------------------------------------------------------")
    print("Please choose the method you want to use by providing the number.")
    print("1. Gradient descent method")
    print("2. Newton's method") 
    print("3. Exit")
    print("--------------------------------------------------------------------------------")

def print_stopping_conditions_options():
    print("--------------------------------------------------------------------------------")
    print("Please choose the stopping condition you want to use by providing the number.")
    print("1. Maximum number of iterations.")
    print("2. Desired value.") 
    print("3. Maximum computation time.")
    print("4. Exit.")
    print("--------------------------------------------------------------------------------")

def print_functions_options():
    print("--------------------------------------------------------------------------------")
    print("Please choose the function you want to optimize.")
    print("1. F(x) = ax^3 + bx^2 + cx + d")
    print("2. G(x) = c + b'x + x'Ax") 
    print("3. Exit.")
    print("--------------------------------------------------------------------------------")

def choose_restart_method():
    while True:
        user_choice = input_validator.validate_boolean_choice_input(RESTART_MODE_MSG)
        if user_choice:
            break
    return user_choice

def provide_restart_repetitions(restart_method):
    repetitions = 1
    if restart_method == "y" or restart_method == "yes":
        while True:
            additional_repetitions = input_validator.validate_integer_input(RESTART_MODE_REPETITIONS_MSG)
            if additional_repetitions:
                repetitions += additional_repetitions
                break;
    return repetitions

def choose_method(): 
    while True:
        choice_value = input_validator.validate_integer_input(PROVIDE_CHOICE_MSG)
        if choice_value == 1 or choice_value == 2: 
            break
        elif choice_value == 3:
            exit(0)
        else:
            print(WRONG_OPTION_CHOICE_MSG)
    return choice_value

def choose_stopping_condition():
    stopping_condition = 0
    while True:
        choice_value = input_validator.validate_integer_input(PROVIDE_CHOICE_MSG) 
        if choice_value == 1 or choice_value == 2 or choice_value == 3 :
            stopping_condition = choice_value
            break
        elif choice_value == 4:
            exit(0)
        else:
            print(WRONG_OPTION_CHOICE_MSG)
    return stopping_condition

def choose_stopping_value(stopping_condition_choice):
    stopping_value = 0
    while True:
        if stopping_condition_choice == 1:
            choice_value = input_validator.validate_positive_integer_input(MAX_NUMBER_OF_ITERATIONS_MSG)
            if choice_value:
                stopping_value = choice_value
                break 
        elif stopping_condition_choice == 2:
            choice_value = input_validator.validate_number_input(DESIRED_VALUE_MSG)
            if choice_value:
                stopping_value = choice_value
                break 
        elif stopping_condition_choice == 3:
            choice_value = input_validator.validate_positive_integer_input(MAX_COMPUTATION_TIME_MSG)
            if choice_value:
                stopping_value = choice_value
                break 
        else:
            print(WRONG_OPTION_CHOICE_MSG)
    return stopping_value

def choose_function():
    while True:
        function_choice = input_validator.validate_integer_input(PROVIDE_FUNCTION_CHOICE_MSG)
        if function_choice == 1 or function_choice == 2:
            break
        elif function_choice == 3:
            exit(0)
        else:
            print(WRONG_OPTION_CHOICE_MSG)
    return function_choice

def provide_coefficients_fx():   
    a = input_validator.validate_number_input(PROVIDE_COEFFICIENT_A_MSG_FOR_FX)     
    b = input_validator.validate_number_input(PROVIDE_COEFFICIENT_B_MSG_FOR_FX)
    c = input_validator.validate_number_input(PROVIDE_COEFFICIENT_C_MSG_FOR_FX)
    d = input_validator.validate_number_input(PROVIDE_COEFFICIENT_D_MSG_FOR_FX)
    x = input_validator.validate_number_input(PROVIDE_X_FOR_FX_MSG)
    return (a, b, c, d, x)

def provide_coefficients_gx():
    d = input_validator.validate_integer_input(PROVIDE_COEFFICIENT_D_MSG_FOR_GX)
    while True:
        x = np.array(input_validator.validate_vector_input(PROVIDE_X_FOR_GX_MSG, d))
        if x.any():
            break
    while True:
        b = np.array(input_validator.validate_vector_input(PROVIDE_COEFFICIENT_B_MSG_FOR_GX, d))
        if b.any():
            break
    c = input_validator.validate_number_input(PROVIDE_COEFFICIENT_C_MSG_FOR_GX)

    while True:
        A = input_validator.validate_positive_definite_matrix_input(PROVIDE_COEFFICIENT_A_MSG_FOR_GX, d)
        if A.any():
            break
    
    return (A, b, c, d, x)

def clear_screen():
    if platform == "linux" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system('cls')
