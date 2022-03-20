import numpy as np

def validate_number_input(input_msg):
    while True:
        try:
            choice_value = float(input(input_msg))
            return choice_value
        except ValueError:
            print("You did not provide number!")
 
def validate_integer_input(input_msg):
    while True:
        try:
            choice_value = int(input(input_msg))
            return choice_value
        except ValueError:
            print("You did not provide integer!")

def validate_positive_integer_input(input_msg):
    while True:
        try:
            choice_value = int(input(input_msg))
            if (choice_value > 0):
                return choice_value
            else:
                print("It is not positive integer, try again!")
        except ValueError:
            print("You did not provide positive integer!")

def validate_boolean_choice_input(input_msg):
    while True:
        choice_value = input(input_msg)
        if choice_value.lower() == "y" or choice_value.lower() == "yes" or choice_value.lower() == "n" or choice_value.lower() == "no":
            return choice_value.lower()
        else:
            print("You provided wrong input! Please use y/n option.")    

def validate_vector_input(input_msg, vector_size):
    while True:
        try:
            vector_input = list(map(float, input(input_msg + str(vector_size) + " elements: ").strip().split()))
            if len(vector_input) == vector_size:
                return vector_input
            elif len(vector_input) < vector_size:
                print("You gave not enough elements, try again!")
            else:
                print("You gave too much elements, try again!")
        except ValueError:
            print("You did not give sufficient amount of values or your input is not a number, try again!")

def validate_matrix_input(input_msg, matrix_size):
    while True:
        try:
            matrix_input = list(map(float, input(input_msg + str(matrix_size**2) + " elements: ").strip().split()))
            matrix = np.array(matrix_input)
            if matrix.size == matrix_size**2:
                return matrix.reshape(matrix_size, matrix_size)
            elif matrix.size < matrix_size**2:
                print("You did not provide sufficient amount of numbers, try again!")
            else:
                print("You provided too much numbers, try again!")
        except ValueError:
            print("Your input is not a matrix of numbers, try again!")


def validate_probability(input_msg):
    while True:
        try:
            choice_value = float(input(input_msg))
            if choice_value >= 0.0 and choice_value <= 1.0:
                return choice_value
            else:
                print("It is not valid value for probability! Probability should belong to the range <0, 1>, try again!")
        except ValueError:
            print("It is not valid value for probability! Probability should belong to the range <0, 1>, try again!")
