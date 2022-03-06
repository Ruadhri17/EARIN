def validate_number_input(input_msg):
    try:
        choice_value = float(input(input_msg))
        return choice_value
    except ValueError:
        print("You did not provide number!")

def validate_integer_input(input_msg):
    try:
        choice_value = int(input(input_msg))
        return choice_value
    except ValueError:
        print("You did not provide integer!")

def validate_boolean_choice_input(input_msg):
    choice_value = input(input_msg)
    if choice_value.lower() == "y" or choice_value.lower() == "yes" or choice_value.lower() == "n" or choice_value.lower() == "no":
        return choice_value.lower()
    else:
        print("You provided wrong input! Please use y/n option.")    
