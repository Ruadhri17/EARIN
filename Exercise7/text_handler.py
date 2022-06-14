from constants import YES, NEW_VARIABLES
import sys

def convert_string_to_array(text, delimiter):
    text = text.replace(' ', '')
    text = text.split(delimiter)
    return text

def print_error(error):
    print(error)
    ans = input(NEW_VARIABLES)
    if ans not in YES:
        sys.exit()