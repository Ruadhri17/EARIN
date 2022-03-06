import newton
import gradient_descent
import input_validator
import numpy as np

PROVIDE_CHOICE_MSG = "Provide your choice: \n"
MAX_NUMBER_OF_ITERATIONS_MSG = "Provide maximum number of iterations: \n"
DESIRED_VALUE_MSG = "Provide desired value: \n"
MAX_COMPUTATION_TIME_MSG = "Provide maximum computation time: \n"
WRONG_OPTION_CHOICE_MSG = "The provided option does not exist!"
RESTART_MODE_MSG = "Do you want to use restart mode? Provide option in y/n format: \n"
RESTART_MODE_REPETITIONS_MSG = "How many times do you want to repeat calculations?  \n"
PROVIDE_FUNCTION_CHOICE_MSG = "Provide number representing which function you choose: \n"
PROVIDE_COEFFICIENT_A_MSG_FOR_FX = "Provide coefficient a for F(x) function: \n"
PROVIDE_COEFFICIENT_B_MSG_FOR_FX = "Provide coefficient b for F(x) function: \n"
PROVIDE_COEFFICIENT_C_MSG_FOR_FX = "Provide coefficient c for F(x) function: \n"
PROVIDE_COEFFICIENT_D_MSG_FOR_FX = "Provide coefficient d for F(x) function: \n"
PROVIDE_X_FOR_FX_MSG = "Provide x value for F(x) function: \n"

PROVIDE_COEFFICIENT_A_MSG_FOR_GX = "Provide element of matrix A: \n"
PROVIDE_COEFFICIENT_B_MSG_FOR_GX = "Provide element of vector b: \n"
PROVIDE_COEFFICIENT_C_MSG_FOR_GX = "Provide scalar c: \n"
PROVIDE_COEFFICIENT_D_MSG_FOR_GX = "Provide size of vector b: \n"
PROVIDE_X_FOR_GX_MSG = "Provide initial vector x: \n"

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
    print("4. Return to previous menu.")
    print("--------------------------------------------------------------------------------")

def print_functions_options():
    print("--------------------------------------------------------------------------------")
    print("Please choose the function you want to optimize.")
    print("1. F(x) = ax^3 + bx^2 + cx + d")
    print("2. G(x) = c + b'x + x'Ax") 
    print("3. Return to previous menu.")
    print("--------------------------------------------------------------------------------")

def choose_restart_method():
    return input_validator.validate_boolean_choice_input(RESTART_MODE_MSG)

def provide_restart_repetitions(restart_method):
    if restart_method == "y" or restart_method == "yes":
        input_validator.validate_integer_input(RESTART_MODE_REPETITIONS_MSG)

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
    choice_value = input_validator.validate_integer_input(PROVIDE_CHOICE_MSG) 
    if choice_value == 1 or choice_value == 2 or choice_value == 3 :
        return choice_value
    elif choice_value == 4:
        print_main_menu()
    else:
        print(WRONG_OPTION_CHOICE_MSG)

def provide_max_number_of_iterations():
    while True:
        max_iterations = input_validator.validate_integer_input(MAX_NUMBER_OF_ITERATIONS_MSG)
        if max_iterations:
            break
    return max_iterations

def provide_desired_value():
    while True:
        desired_value = input_validator.validate_number_input(DESIRED_VALUE_MSG)
        if desired_value:
            break
    return desired_value

def provide_max_computation_time():
    while True:
        max_computation_time = input_validator.validate_number_input(MAX_COMPUTATION_TIME_MSG)
        if max_computation_time:
            break
    return max_computation_time

def choose_function():
    while True:
        function_choice = input_validator.validate_integer_input(PROVIDE_FUNCTION_CHOICE_MSG)
        if function_choice == 1 or function_choice == 2:
            break
        elif function_choice == 3:
            print_main_menu()
            break
        else:
            print(WRONG_OPTION_CHOICE_MSG)
    return function_choice

def provide_coefficients_fx():   
    while True: 
        a = input_validator.validate_number_input(PROVIDE_COEFFICIENT_A_MSG_FOR_FX)
        if a:
            break
    
    while True:
        b = input_validator.validate_number_input(PROVIDE_COEFFICIENT_B_MSG_FOR_FX)
        if b:
            break
    
    while True:
        c = input_validator.validate_number_input(PROVIDE_COEFFICIENT_C_MSG_FOR_FX)
        if c:
            break
    
    while True:
        d = input_validator.validate_number_input(PROVIDE_COEFFICIENT_D_MSG_FOR_FX)
        if d:
            break
    
    while True:
        x = input_validator.validate_number_input(PROVIDE_X_FOR_FX_MSG)
        if x:
            break

    return (a, b, c, d, x)

def provide_coefficients_gx():
    while True:
        x = input_validator.validate_vector_input(PROVIDE_X_FOR_GX_MSG, 0)
        if x:
            break
    while True:
        d = input_validator.validate_integer_input(PROVIDE_COEFFICIENT_D_MSG_FOR_GX)
        if d:
            break
    while True:
        b = np.array(input_validator.validate_vector_input(PROVIDE_COEFFICIENT_B_MSG_FOR_GX, d))
        if b:
            break
    while True:
        c = input_validator.validate_number_input(PROVIDE_COEFFICIENT_C_MSG_FOR_GX)
        if c:
            break
    while True:
        A = input_validator.validate_matrix_input(PROVIDE_COEFFICIENT_A_MSG_FOR_GX, x.count())
        if A:
            break
    
    return (A, b, c, d, x)