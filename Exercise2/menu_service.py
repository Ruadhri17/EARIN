import menu
import genetic_algorithm

def run_fx():
    while True:
        menu.clear_screen()
        (searched_integers_range_power, population_size, crossover_probability, mutation_probability, algorithm_iterations) = menu.provide_algorithm_parameters()
        (A, b, c, problem_dimensionality) = menu.provide_coefficients_fx()
        genetic_algorithm.genetic_algorithm(A, b, c, searched_integers_range_power, problem_dimensionality, population_size, mutation_probability, crossover_probability, algorithm_iterations)
        if menu.finish_program():
            exit(0)