# import numpy as np
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
        menu.print_main_menu()
        method_choice = menu.choose_method()

        menu.print_stopping_conditions_options()
        stopping_condition = menu.choose_stopping_condition()
        
        menu.print_functions_options()
        function_choice = menu.choose_function()
        if function_choice == 1:
            menu.provide_coefficients_gx()
        elif function_choice == 2:
            (a, b, c, d) = menu.provide_coefficients_fx()
            if method_choice == 1:
                gradient_descent.execute_fx(a, b, c, d)
            elif method_choice == 2:
                newton.execute_fx(a, b, c, d)

        
            
if __name__ == '__main__':
    main()
