# import numpy as np
import menu
import newton
import gradient_descent

def main():
    method_choice = 0
    stopping_condition = 0
    show_main_menu = True
    while True:
        menu.print_main_menu()
        method_choice = menu.choose_method()
        menu.clear_screen()

        menu.print_stopping_conditions_options()
        stopping_condition = menu.choose_stopping_condition()
        stopping_value = menu.choose_stopping_value(stopping_condition)
        menu.clear_screen()

        menu.print_functions_options()
        function_choice = menu.choose_function()
        menu.clear_screen()

        if function_choice == 1:
            (a, b, c, d, x) = menu.provide_coefficients_fx()
            menu.clear_screen()
            if method_choice == 1:
                print(gradient_descent.execute_fx(a, b, c, d, x, stopping_condition, stopping_value))
            elif method_choice == 2:
                restart_method = menu.choose_restart_method()
                repetitions = menu.provide_restart_repetitions(restart_method)
                for _ in range(repetitions):
                    print(newton.execute_fx(a, b, c, d, x, stopping_condition, stopping_value))
        elif function_choice == 2:
            (a, b, c, d, x) = menu.provide_coefficients_gx()
            menu.clear_screen()
            if method_choice == 1:
                print(gradient_descent.execute_gx(a, b, c, d, x, stopping_condition, stopping_value))
            elif method_choice == 2:
                restart_method = menu.choose_restart_method()
                repetitions = menu.provide_restart_repetitions(restart_method)
                for _ in range(repetitions):
                    print(newton.execute_gx(a, b, c, d, x, stopping_condition, stopping_value))
        
            
if __name__ == '__main__':
    main()
