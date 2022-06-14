import json
import numpy as np
from node import Node, get_node
from constants import FILENAME
import random

class BayesianNetwork:

    def __init__(self):
        self.json = {}
        self.nodes = []

        self.read_file()
        if self.json:
            self._parse_nodes()
            self._match_children()
    
    def read_file(self):
        with open(FILENAME, "r") as file:
            self.json = json.load(file)
    # Read information about nodes (relations and probabilities)
    def _parse_nodes(self):
        for node in self.json["nodes"]:
            prob = self.json["relations"][node]["probabilities"]
            vals = []
            for el in list(prob.keys()):
                probs = el.split(",")
                vals.append(probs[-1])

            self.nodes.append(Node(
                node, self.json["relations"][node]["parents"], self.json["relations"][node]["probabilities"], vals))
        self._validate_probabilities()
    # Fill extra info about children, created for markov_blanket
    def _match_children(self):
        for node in self.nodes:
            for parent in node.parents:
                parent_node = get_node(self.nodes, parent)
                parent_node.add_child(node.node_name)
    # Store information about children and parents of given node
    def create_markov_blanket(self, name):
        node = get_node(self.nodes, name)
        markov_out = {}
        markov_out["parents"] = node.parents
        markov_out["children"] = node.children

        children_parents = {}
        for child in node.children:
            child_node = get_node(self.nodes, child)
            children_parents[child] = child_node.parents
        markov_out["children parents"] = children_parents
        return markov_out

    def markov_blanket(self, name):
        mb = self.create_markov_blanket(name)
        mb_display = []
        for child in mb['children']:
            mb_display.append(child)

        mb_parents = mb['children parents']
        for parent in mb_parents:
            for child in mb_parents[parent]:
                mb_display.append(child)

        mb_display.remove(name)
        mb_display = list(set(mb_display))
        print("Markov Blanket for node " + name)
        print(mb_display)


    def _validate_probabilities(self):
        for node in self.nodes:
            probabilities = list(node.probabilities.values())
            parents = node.parents

            try:
                # check if keys in probabilities dictionary contains proper amount of parameters.
                for el in list(node.probabilities.keys()):
                    probs = el.split(",")
                    if len(probs) != len(parents) + 1:
                        raise ValueError('[{}] Number of parents is not valid for given probabilities'.format(node.node_name))

                # checks if each probability value is between 0 and 1.
                for el in probabilities:
                    if el > 1 or el < 0:
                        raise ValueError('[{}] Probability must be in interval [0, 1]'.format(node.node_name))

                # if node has no parents then all of it's probabilities must sum up to 1.
                if parents == []:
                    s = 0
                    for el in probabilities:
                        s += el

                    if float(s) != 1.0:
                        raise ValueError('[{}] Probability must sum up to 1.'.format(node.node_name))
                # if node has parents, each two probabilites sums up to 1.
                else:
                    for iter in range(0, len(probabilities), 2):
                        if probabilities[iter] + probabilities[iter+1] != 1:
                            raise ValueError('[{}] Probabilities has to be equal to 1'.format(node.node_name))

                if self.check_cyclic() == False:
                    raise ValueError('[{}] Network contains cycles.'.format(node.node_name))

            except ValueError:
                raise
    # Check if graph is cyclic
    def check_cyclic(self):
        for node in self.nodes:
            if node.node_name in node.parents:
                return False
            if node.node_name in node.children:
                return False
    
    # MCMC with Gibbs sampling           
    # Method takes as an arguments evidence dictionary, query array and number of steps as a number
    def mcmc(self, evidence, query, step):
        #   asigning values for all nodes
        #   Those that in evidence dictionary are set to the provided value. 
        #   Non-evidence nodes are set randomly.
        #   Counter stores values for evidence nodes
        non_evidence = []
        
        for node in self.nodes:
            if not node.node_name in evidence.keys():
                non_evidence.append(node)
            else:
                node.value = evidence[node.node_name]

        # Assign random value from all possible values to each non-evidence node.
        for ev in non_evidence:
            ev.value = np.random.choice(ev.probabilities_values)

        counter = {}
        for ev in query:
            node = get_node(self.nodes, ev)
            values = {}
            for p in node.probabilities_values:
                values[p] = 0
            counter[ev] = values

        s = 0
        # Randomly select non_evidence node 
        for _ in range(step):
            if len(non_evidence) != 0:
                selected_variable = random.choice(non_evidence)
                
                # Calculate probabilities
                # Draw one sample using roulete wheel and assign it to the value
                selected_variable.value = self.sample(selected_variable)
            # Increase counter
            for ev in query:
                counter[ev][get_node(self.nodes, ev).value] += 1.0

        for res in counter:
            s = sum(list(counter[res].values()))
        # Normalize counter values
        for res in counter:
            for ev in counter[res].keys():
                counter[res][ev] /= s
        # Print result
        for res in counter:
            print("Query:  " + res)
            print(counter[res])

    # Probabilities calculation for given node 
    def sample(self, selected_variable):
        # use Markov Blanket for the given node 
        mb = self.create_markov_blanket(selected_variable.node_name)
        probabilities_dict = {}
        #P(X = xj | Parents(X))
        for var in selected_variable.probabilities_values:
            selected_variable.value = var

            selected_variable_parent = ""
            for parent in mb["parents"]:
                parent_node = get_node(self.nodes, parent)
                selected_variable_parent += str(parent_node.value) + ','
            selected_variable_parent += selected_variable.value

            prob_parent = selected_variable.probabilities[selected_variable_parent]

            selected_variable_children = ""
            prob = 1
            # For each children Zi, find: P( Zi = zi | Parents(Zi)
            for children in mb["children"]:
                child_node = get_node(self.nodes, children)
                parent_node_val = []
                for parent in mb["children parents"][children]:
                    parent_node = get_node(self.nodes, parent)
                    parent_node_val.append(str(parent_node.value))
                parent_node_val.append(str(child_node.value))

                selected_variable_children = ','.join(parent_node_val)
                # Multiply all probabilites from step 2 by probability from step 1
                prob *= child_node.probabilities[selected_variable_children]
  
            final_prob = prob_parent * prob
            probabilities_dict[var] = final_prob

        return self.roulette_selection(probabilities_dict)

    # Takes all calculated probabilites as a vector and normalize it so as all values sumes up to 1
    def roulette_selection(self, probabilities_dict):
        # We normalize vector in order to create roulette wheel.
        s = sum(list(probabilities_dict.values()))
        normal_prob = [el / s for el in list(probabilities_dict.values())]

        wheel = []
        prev = 0
        for el in normal_prob:
            curr = prev + el
            wheel.append(curr)
            prev = curr

        roulette_pick = np.random.uniform(0, 1)
        i = 0
        while i in range(len(wheel)) and wheel[i] < roulette_pick:
            i += 1

        if i > len(wheel) - 1:
            i =- 1

        res = (list(probabilities_dict.items())[i])
        return res[0]