import input_validator
import numpy as np
from sys import platform
import os

PROVIDE_COEFFICIENT_A_MSG_FOR_FX = "Provide values for matrix A of "
PROVIDE_COEFFICIENT_B_MSG_FOR_FX = "Provide values for vector b of "
PROVIDE_COEFFICIENT_C_MSG_FOR_FX = "Provide scalar c: "
PROVIDE_PROBLEM_DIMENSIONALITY_MSG_FOR_FX = "Provide size of vectors / matrices: "
PROVIDE_X_FOR_FX_MSG = "Provide values for vector x: "

PROVIDE_POPULATION_SIZE_MSG = "Provide population size: "
PROVIDE_CROSSOVER_PROBABILITY_MSG = "Provide crossover probability: "
PROVIDE_MUTATION_PROBABILITY_MSG = "Provide mutation probability: "
PROVIDE_ALGORITHM_ITERATIONS_NUMBER_MSG = "Provide number of algorithm iterations: "
PROVIDE_SEARCHED_INTEGERS_RANGE_POWER_MSG = "Provide number d >= 1 which will contribute to calculating searched integers range <-2^d, 2^d>: "

FINISH_PROGRAM_MSG = "Do you want to finish program(y/n)?: "

def provide_coefficients_fx():
    problem_dimensionality = input_validator.validate_integer_input(PROVIDE_PROBLEM_DIMENSIONALITY_MSG_FOR_FX)
    # while True:
    #     x = np.array(input_validator.validate_vector_input(PROVIDE_X_FOR_FX_MSG, problem_dimensionality))
    #     if x.any():
    #         break
    while True:
        b = np.array(input_validator.validate_vector_input(PROVIDE_COEFFICIENT_B_MSG_FOR_FX, problem_dimensionality))
        if b.any():
            break
    c = input_validator.validate_number_input(PROVIDE_COEFFICIENT_C_MSG_FOR_FX)

    while True:
        A = input_validator.validate_matrix_input(PROVIDE_COEFFICIENT_A_MSG_FOR_FX, problem_dimensionality)
        if A.any():
            break
    
    return (A, b, c, problem_dimensionality)

def provide_algorithm_parameters():
    searched_integers_range_power = input_validator.validate_positive_integer_input(PROVIDE_SEARCHED_INTEGERS_RANGE_POWER_MSG)
    population_size = input_validator.validate_positive_integer_input(PROVIDE_POPULATION_SIZE_MSG)
    crossover_probability = input_validator.validate_probability(PROVIDE_CROSSOVER_PROBABILITY_MSG)
    mutation_probability = input_validator.validate_probability(PROVIDE_MUTATION_PROBABILITY_MSG)
    algorithm_iterations = input_validator.validate_positive_integer_input(PROVIDE_ALGORITHM_ITERATIONS_NUMBER_MSG)

    return (searched_integers_range_power, population_size, crossover_probability, mutation_probability, algorithm_iterations)

def finish_program():
    while True:
        user_choice = input_validator.validate_boolean_choice_input(FINISH_PROGRAM_MSG)
        if user_choice:
            break
    return user_choice

def clear_screen():
    if platform == "linux" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system('cls')