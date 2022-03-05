import numpy as np

def gradient_descent_method():
    np 
    print("gradient descent")

def newton_method_fx(x0: float, a: float, b: float, c: float, d: float):
    xn = x0
    (stopping_condition, stopping_value) = choose_stopping_conditions
    if stopping_condition == 1: 
        for _ in range(stopping_value):
            xn = xn - f(xn, a, b, c, d) / f_prime(xn, a, b, c)
    elif stopping_condition == 2:
        while abs(xn) > stopping_value:
            xn = xn - f(xn, a, b, c, d) / f_prime(xn, a, b, c)             
    return (xn, f(xn, a, b, c, d))

def f(x, a, b, c, d):
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d
    
def f_prime(x, a, b, c):
    return 3 * a * pow(x, 2) + 2 * b * x + c
    
def print_welcoming_messages():
    print("--------------------------------------------------------------------------------")
    print("Hello user! Please choose the method you want to use by providing the number.")
    print("1. Gradient descent method")
    print("2. Newton's method") 
    print("3. Exit")
    print("--------------------------------------------------------------------------------")

def choose_method():  
    try:
        user_choice = int(input("Provide your choice: "))
        if choice_value == 1: 
            gradient_descent_method()
        elif choice_value == 2:
            newton_method()
        elif choice_value == 3:
            exit(0)
        else:
            print("You provided wrong number!")
    except ValueError:
        print("You did not provide integer!")

def print_stopping_condtions_messages():
    print("--------------------------------------------------------------------------------")
    print("Please choose the stopping condition you want to use by providing the number.")
    print("1. Maximum number of iterations.")
    print("2. Desired value.") 
    print("3. Maximum computation time.")
    print("4. Exit")
    print("--------------------------------------------------------------------------------")

def choose_stopping_conditions():
    try:
        user_choice = int(input("Provide your choice: "))
        if choice_value == 1 or choice_value == 2 or choice_value == 3 
            return choice_value
        elif choice_value == 4:
            print_welcoming_messages()
        else:
            print("You provided wrong number!")
    except ValueError:
        print("You did not provide integer!")

def main():
    #(a, b) = newton_method(5, 3, 4, 6, 2)
    print(a, b)
    # while(True):
    #     print_welcoming_messages()
    #     choose_method()
    
if __name__ == '__main__':
    main()