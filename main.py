import menu_service

def main():
    repetitions = menu_service.select_restart_method()
    for _ in range(repetitions):
        method_choice = menu_service.select_method()
        (stopping_condition, stopping_value) = menu_service.select_stopping_conditions()
        function_choice = menu_service.select_function()
        if function_choice == 1:
            menu_service.run_fx(method_choice, stopping_condition, stopping_value)
        elif function_choice == 2:
            menu_service.run_gx(method_choice, stopping_condition, stopping_value)
        
            
if __name__ == '__main__':
    main()
