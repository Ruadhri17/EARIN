from constants import LINE, MCMC, MARKOV_BLANKET, YES, PROVIDE_NODE, INCORRECT_DEFINED_DATA, NEW_VARIABLES
from mcmc import set_parameters
from text_handler import print_error
from bayesian_network import BayesianNetwork
import sys

def run_menu():
    print(LINE)
    while True:
        try:
            evidence = ''
            query = ''
            steps = ''

            option_enum = [MCMC, MARKOV_BLANKET]
            option = int(input('- Choose the method by typing 0 ({}) or 1 ({})  : '.format(option_enum[0], option_enum[1])))

            if option == 0:
                evidence, query, steps = set_parameters()
            elif option == 1:
                evidence = input(PROVIDE_NODE)
            else:
                raise ValueError

            print(LINE)
            execute_method(evidence, query, steps, option_enum[option])

            if option == 0:
                ans = 'y'
                while ans in YES:
                    print(LINE)
                    ans = input('- Do you want to run {} method once again (y/n): '.format(option_enum[option]))
                    if ans in YES:
                        print(LINE)
                        execute_method(evidence, query, steps, option_enum[option])

            ans = input(NEW_VARIABLES)
            print(LINE)
            if ans not in YES:
                sys.exit()

        except ValueError:
            print_error(INCORRECT_DEFINED_DATA)
        except AttributeError:
            print_error(INCORRECT_DEFINED_DATA)

def execute_method(evidence, query, steps, option):
    bayes_net = BayesianNetwork()

    if option == MCMC:
        res = bayes_net.mcmc(evidence=evidence, query=query, step=steps)
    elif option == MARKOV_BLANKET:
        bayes_net.markov_blanket(evidence)