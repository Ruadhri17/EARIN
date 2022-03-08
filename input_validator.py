from xml.dom.minidom import Element
import numpy as np

def validate_number_input(input_msg):
    try:
        choice_value = float(input(input_msg))
        return choice_value
    except ValueError:
        print("You did not provide number!")

def validate_integer_input(input_msg):
    try:
        choice_value = int(input(input_msg))
        return choice_value
    except ValueError:
        print("You did not provide integer!")

def validate_positive_integer_input(input_msg):
    try:
        choice_value = int(input(input_msg))
        if (choice_value > 0):
            return choice_value
        else:
            print("It is not positive integer, try again!")
    except ValueError:
        print("You did not provide positive integer!")

def validate_boolean_choice_input(input_msg):
    choice_value = input(input_msg)
    if choice_value.lower() == "y" or choice_value.lower() == "yes" or choice_value.lower() == "n" or choice_value.lower() == "no":
        return choice_value.lower()
    else:
        print("You provided wrong input! Please use y/n option.")    

def validate_vector_input(input_msg, vector_size):
    while True:
        vector_input = list(map(float, input(input_msg).strip().split()))[:vector_size]
        if len(vector_input) == vector_size:
            return vector_input
        elif len(vector_input) < vector_size:
            print("You gave not enough elements, try again!")
        else:
            print("You gave too much elements, try again!")

def validate_positive_definite_matrix_input(input_msg, matrix_size):
    matrix_input = list(map(float, input(input_msg).strip().split()))[:matrix_size**2]
    matrix = np.array(matrix_input)
    if len(matrix_input) / matrix_size == matrix_size and np.any(matrix >= 0):
        return matrix.reshape(matrix_size, matrix_size)
    elif not np.any(matrix >= 0):
        print("All values should be positive, try again!")
    else:
        print("You did not give sufficient amount of values, try again!")