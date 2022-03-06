import numpy as np
import menu
import newton
import gradient_descent

def main():
    #(a, b) = newton_method(5, 3, 4, 6, 2)
    # print(a, b)
    method_choice = 0
    stopping_condition = 0
    show_main_menu = True
    while True:
        if show_main_menu :
            menu.print_main_menu()
            method_choice = menu.choose_method()

        if method_choice == 1 or method_choice == 2 :
            menu.print_stopping_condtions_options()
            stopping_condition = menu.choose_stopping_condition()
        
        menu.print_functions_options()
        
        
            
if __name__ == '__main__':
    main()