import string
import numpy as np
from random import uniform, randint

def fx(x, A, b, c):
    return np.dot(np.dot(np.transpose(x), A), x)  + np.dot(np.transpose(b), x) + c


def convert_binary_to_int(genome):
    number_vector = []
    for binary_number in genome:
        most_significant_bit = binary_number[0]
        if most_significant_bit == 0:
            decimal_representation = binary_number.dot(2**np.arange(binary_number.size)[::-1])
        else:
            size_without_msb = binary_number.size - 1
            binary_number_without_msb = binary_number[-size_without_msb:]
            inverted_binary = np.logical_not(binary_number_without_msb).astype(int)
            decimal_representation = (-1) * (inverted_binary.dot(2**np.arange(inverted_binary.size)[::-1]) + 1)
        number_vector.append(decimal_representation)
    return number_vector 

def create_genome(n, d):
    vector_list = []
    for _ in range(n):
        vector_list.append(np.random.randint(2, size=d+1))
    return vector_list
    
def create_population(population_size, n, d):
    return [create_genome(n, d) for _ in range(population_size)]

def fitness(genome, A, b, c):
    return fx(convert_binary_to_int(genome), A, b, c)

def roulette_wheel_selection(population, A, b, c):
    sum_of_fitnesses = 0
    partial_sum = 0
    # Sort by fitness value (descending)
    population.sort(reverse=True, key= lambda g: fitness(g, A, b, c))
    # Sum fitnesses
    for genome in population:
        sum_of_fitnesses += fitness(genome, A, b, c)
    
    desired_value = uniform(0, sum_of_fitnesses)
    # Find parent
    for genome in population:
        partial_sum += fitness(genome, A, b, c)
        if partial_sum > desired_value:
            return genome
            
def crossover(first_parent, second_parent, crossover_probability):
    # Check vector size
    parent_dimension = len(first_parent)
    # Choose randomly crossover point
    crossover_point = randint(0, first_parent[0].size)
    # Determine if crossover will happen
    if uniform(0.0 , 1.0) > crossover_probability:
        return (first_parent, second_parent)
    # prepare children 
    first_child = []
    second_child = []
    # exchange genomes of both parents in crossover point
    first_child = first_parent[:crossover_point] + second_parent[crossover_point:]
    second_child= second_parent[:crossover_point] + first_parent[crossover_point:]
    print("Crossover point" + str(crossover_point))
    return (first_child, second_child)

def genetic_algorithm(A, b, c, d, n, population_size, mutation_probability, crossover_probability, number_of_iterations):
    population = create_population(population_size, n, d)
    next_generation = []
    print(len(population))
    for _ in range(number_of_iterations):
        for _ in range(int(len(population)/2) - 1):
            # Choose parent (roulette wheel selection) 
            first_parent = roulette_wheel_selection(population, A, b, c)
            second_parent = roulette_wheel_selection(population, A, b, c)
            # Cross parents
            (first_child, second_child) = crossover(first_parent, second_parent, crossover_probability)
            # After Crossing preserve child for next generations
            next_generation.append(first_child)
            next_generation.append(second_child)
            print(first_parent)
            print(second_parent)
            print(first_child)
            print(second_child)
            print("\n\n\n")
    return next_generation

# [[array(1,0,1), array(1,1,0)], [array(1,1,1), array(0,1,0)]]