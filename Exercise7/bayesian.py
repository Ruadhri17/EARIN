import json
import numpy as np

class Node(object):
    def __init__(self, json_data):
        self.name = json.loads(json_data)
        self.parents = json.loads(json_data)
        self.probabilities = json.loads(json_data)

class Bayesian:
    def __init__(self):
        self.nodes = []
        self.read_json()

    def read_json(self):
        f = open('flu.json', 'r')
        nodes = json.load(f)
        for node in nodes:
            add_node = Node(node)
            self.nodes.append(add_node)
    def print(self):
        pass


def gibbs_sampler(initial_point, num_of_samples, mean, cov):
    point = np.array(initial_point)
    samples = np.empty([num_of_samples+1, 2])
    samples[0] = point
    tmp_points = np.empty([num_of_samples, 2])

    for i in range(num_of_samples):
        point = conditional_sampler(0, point, mean, cov)
        tmp_points = point

        point = conditional_sampler(1, point, mean, cov)


        samples[i+1] = point

    return samples, tmp_points

def conditional_sampler(sampling_index, current_x, mean, cov):
    conditioned_index = 1 - sampling_index
    
    a = cov[sampling_index, sampling_index]
    b = cov[sampling_index, conditioned_index]
    c = cov[conditioned_index, conditioned_index]

    mu = mean[sampling_index] + (b * (current_x[conditioned_index] - mean[conditioned_index])) / c
    sigma = np.sqrt(a - pow(b, 2) / c)
    
    new_x = np.copy(current_x)
    new_x[sampling_index] = np.random.randn() * sigma + mu
    
    return new_x

def mcmc():
    pass
