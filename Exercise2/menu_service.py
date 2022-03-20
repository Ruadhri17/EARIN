import menu
# import genetic_algorithm

def run_fx():
    while True:
        menu.clear_screen()
        (searched_integers_range_power, population_size, crossover_probability, mutation_probability, algorithm_iterations) = menu.provide_algorithm_parameters()
        (A, b, c, problem_dimensionality, x) = menu.provide_coefficients_fx()
        if menu.finish_program():
            exit(0)