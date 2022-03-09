import menu
import gradient_descent
import newton

def select_method():
    menu.print_main_menu()
    method_choice = menu.choose_method()
    menu.clear_screen()
    return method_choice

def select_stopping_conditions():
    menu.print_stopping_conditions_options()
    stopping_condition = menu.choose_stopping_condition()
    stopping_value = menu.choose_stopping_value(stopping_condition)
    menu.clear_screen()
    return (stopping_condition, stopping_value)

def select_restart_method():
    restart_method = menu.choose_restart_method()
    repetitions = menu.provide_restart_repetitions(restart_method)
    menu.clear_screen()
    return repetitions

def select_function():
    menu.print_functions_options()
    function_choice = menu.choose_function()
    return function_choice

def run_fx(method_choice, stopping_condition, stopping_value):
    (a, b, c, d, x) = menu.provide_coefficients_fx()
    if method_choice == 1:
        (xn, fx) = gradient_descent.execute_fx(a, b, c, d, x, stopping_condition, stopping_value)
    elif method_choice == 2:
        (xn, fx) = newton.execute_fx(a, b, c, d, x, stopping_condition, stopping_value)
    print("Found solution of x: ", xn)
    print("Function value: ", fx)

def run_gx(method_choice, stopping_condition, stopping_value):
    (A, b, c, d, x) = menu.provide_coefficients_gx()
    if method_choice == 1:
        (xn, gx) = gradient_descent.execute_gx(A, b, c, x, stopping_condition, stopping_value)
    elif method_choice == 2:
        (xn, gx) = newton.execute_gx(A, b, c, x, stopping_condition, stopping_value)
    print("Found solution of x: ", xn)
    print("Function value: ", gx)
