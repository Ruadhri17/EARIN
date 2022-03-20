import numpy as np

def fx(x, A, b, c):
    return np.dot(np.dot(np.transpose(x), A), x)  + np.dot(np.transpose(b), x) + c

def create_genome(n, d):
    vector_list = []
    for _ in range(n):
        vector_list.append(np.random.randint(2, size=d+1))
    return vector_list
    
def create_population(population_size, n, d):
    return [create_genome(n, d) for _ in range(population_size)]

def roulette_wheel_selection(genome, A, b, c):
    
    return fx (genome, A, b, c)

def crossover():
    return
def selection():
    return
def mutation():
    return
def genetic_algorithm(A, b, c, d, n, population_size, mutation_probability, crossover_probability, number_of_iterations):
    population = create_population(population_size, n, d)
    for i in range(number_of_iterations):
        population.sort(reverse=True, key= lambda g: roulette_wheel_selection(g, A, b, c))
    return population
