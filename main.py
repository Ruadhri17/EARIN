import tictactoe
import menu

def main(): 
    human_player_mark = menu.choose_mark()
    if human_player_mark == 'X':
        ai_player_mark = 'O'
    else:
        ai_player_mark = 'X'
    
    while len(tictactoe.find_empty_fields()) > 0:
        menu.clear_screen()
        menu.print_info(ai_player_mark, human_player_mark)
        tictactoe.print_board(ai_player_mark, human_player_mark)
        tictactoe.human_player_turn()
    
    menu.clear_screen()
    menu.print_info(ai_player_mark, human_player_mark)
    tictactoe.print_board(ai_player_mark, human_player_mark)


if __name__ == '__main__':
    main()
