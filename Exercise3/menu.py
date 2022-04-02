import os
from sys import platform

def clear_screen():
    if platform == "linux" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system('cls')

def choose_mark():
    human_player_choice = ''
    while True:
        try:
            human_player_choice = input('Please choose your mark X or O: ').upper()
            if human_player_choice == 'O' or human_player_choice == 'X':
                break
            else:
                print('Incorrect choice! Choose X or O, try again.')
        except (EOFError, KeyboardInterrupt):
            print('\nThank you for the game!')
            exit()
        except (KeyError, ValueError):
            print('Incorrect choice! Choose X or O, try again.')


    return human_player_choice

def print_info(ai_player_mark, human_player_mark):
    print('Human player ' + human_player_mark + ', Score: 0\n')
    print('AI player ' + ai_player_mark + ', Score: 0\n')

def choose_order():
    human_player_choice = ''
    while True:
        try:
            human_player_choice = input('Do you want to start(y/n)? ').upper()
            if human_player_choice == 'Y' or human_player_choice == 'N':
                break
            else:
                print('Incorrect choice! Choose Y or N, try again.')
        except (EOFError, KeyboardInterrupt):
            print('\nThank you for the game!')
            exit()
        except (KeyError, ValueError):
            print('Incorrect choice! Choose Y or N, try again.')

    return human_player_choice
