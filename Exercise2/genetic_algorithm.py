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
        edited_fitness = fitness(genome, A, b, c) + 2*abs(fitness(population[-1], A, b, c)) 
        sum_of_fitnesses += edited_fitness
    
    desired_value = uniform(0.0, 1.0)
    population.sort(reverse=False, key= lambda g: fitness(g, A, b, c))
    # Find parent
    for genome in population:
        edited_fitness = (fitness(genome, A, b, c) + 2*abs(fitness(population[0], A, b, c))) / sum_of_fitnesses
        partial_sum += edited_fitness
        if partial_sum > desired_value:
            return genome
            
def crossover(first_parent, second_parent, crossover_probability):
    # Check vector size
    parent_dimension = len(first_parent)
    # Choose randomly crossover point
    crossover_point = randint(1, first_parent[0].size)
    # Determine if crossover will happen
    if uniform(0.0, 1.0) > crossover_probability:
        return (first_parent, second_parent)
    # prepare children 
    first_child = []
    second_child = []
    # exchange genomes of both parents in crossover point
    for i in range(parent_dimension):
        first_child.append(np.append(first_parent[i][:crossover_point].copy(), [second_parent[i][crossover_point:].copy()]))
        second_child.append(np.append(second_parent[i][:crossover_point].copy(), [first_parent[i][crossover_point:].copy()]))

    return (first_child, second_child)

def mutation(child, mutation_probability):
    for binary_number in child:
         with np.nditer(binary_number, op_flags=['readwrite']) as itr:
            for digit in itr:
                if uniform(0.0, 1.0) < mutation_probability:
                    digit[...] = 1 if digit == 0 else 0
    return child

def print_results(population, A, b, c, gen_nr):
    population.sort(reverse=True, key= lambda g: fitness(g, A, b, c))
    achieved_x = convert_binary_to_int(population[0])
    achieved_fx = fx(achieved_x, A, b, c)
    d = {}
    d[str(achieved_x)] = achieved_fx
    for v in d.items():
        x_value, fun_value = v
        print("{:<6} {:<10} {:<6}".format(gen_nr, x_value, fun_value))

def genetic_algorithm(A, b, c, d, n, population_size, mutation_probability, crossover_probability, number_of_iterations):
    population = create_population(population_size, n, d)
    print("{:<6} {:<10} {:<6}".format('Gen.', 'X value', 'Fun. value'))
    for gen_nr in range(number_of_iterations):
        # Choose parent (roulette wheel selection) 
        first_parent = roulette_wheel_selection(population, A, b, c)
        second_parent = roulette_wheel_selection(population, A, b, c)
        
        # Cross parents
        (first_child, second_child) = crossover(first_parent, second_parent, crossover_probability)
        
        # Mutation 
        first_child_after_mutation = mutation(first_child, mutation_probability)
        second_child_after_mutation = mutation(second_child, mutation_probability)
        
        # FIFO Replacement
        population.pop(0)
        population.pop(0)
        population.append(first_child_after_mutation)
        population.append(second_child_after_mutation)
        if gen_nr == 0:
            print_results(population, A, b, c, gen_nr+1)
        elif gen_nr % 10 == 9:
            print_results(population, A, b, c, gen_nr+1)

    print("--------------------------------------------------------------")
    print_results(population, A, b, c, gen_nr+1)   
    
    return population
