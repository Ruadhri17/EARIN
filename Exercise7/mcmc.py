from text_handler import print_error, convert_string_to_array
from constants import YES, EVIDENCE_WITH_STEPS, PROVIDE_SIMPLE_QUERY, PROVIDE_NUMBER_OF_STEPS, INCORRECT_DATA

def set_parameters():
    try:
        evidence = {}
        in_text = input(EVIDENCE_WITH_STEPS)
        in_text = in_text.split(':')
        evidence[in_text[0]] = in_text[1]

        in_text = input(PROVIDE_SIMPLE_QUERY)
        query = convert_string_to_array(in_text, ',')

        steps = int(input(PROVIDE_NUMBER_OF_STEPS))

        return evidence, query, steps

    except ValueError:
        print_error(INCORRECT_DATA)