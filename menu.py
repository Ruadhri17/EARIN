from secrets import choice
import newton
import gradient_descent
import input_validator


PROVIDE_CHOICE_MSG = "Provide your choice: \n"
MAX_NUMBER_OF_ITERATIONS_MSG = "Provide maximum number of iterations: \n"
DESIRED_VALUE_MSG = "Provide desired value: \n"
MAX_COMPUTATION_TIME_MSG = "Provide maximum computation time: \n"
WRONG_OPTION_CHOICE_MSG = "The provided option does not exist!"
RESTART_MODE_MSG = "Do you want to use restart mode? Provide option in y/n format: \n"
RESTART_MODE_REPETITIONS_MSG = "How many times do you want to repeat calculations?  \n"



def print_main_menu():
    print("--------------------------------------------------------------------------------")
    print("Hello user! Please choose the method you want to use by providing the number.")
    print("1. Gradient descent method")
    print("2. Newton's method") 
    print("3. Exit")
    print("--------------------------------------------------------------------------------")

def print_stopping_condtions_options():
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
    print("2. G(x) = c + [b^T]x + [x^T]Ax") 
    print("3. Return to previous menu.")
    print("--------------------------------------------------------------------------------")

def choose_restart_method():
    return input_validator.validate_boolean_choice_input(RESTART_MODE_MSG)

def provide_restart_repetitions(restart_method):
    if restart_method == "y" or restart_method == "yes":
        input_validator.validate_integer_input(RESTART_MODE_REPETITIONS_MSG)

def choose_method():  
    choice_value = input_validator.validate_integer_input(PROVIDE_CHOICE_MSG)
    
    if choice_value == 1 or choice_value == 2: 
        return choice_value
    elif choice_value == 3:
        exit(0)
    else:
        print(WRONG_OPTION_CHOICE_MSG)

def choose_stopping_condition():
    choice_value = input_validator.validate_integer_input(PROVIDE_CHOICE_MSG) 
    if choice_value == 1 or choice_value == 2 or choice_value == 3 :
        return choice_value
    elif choice_value == 4:
        print_main_menu()
    else:
        print(WRONG_OPTION_CHOICE_MSG)

def provide_max_number_of_iterations():
    input_validator.validate_integer_input(MAX_NUMBER_OF_ITERATIONS_MSG)

def provide_desired_value():
    input_validator.validate_number_input(DESIRED_VALUE_MSG)

def provide_max_computation_time():
    input_validator.validate_number_input(MAX_COMPUTATION_TIME_MSG)

