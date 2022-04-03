from math import inf
import menu

AI_PLAYER = 1
HUMAN_PLAYER = -1

def human_player_turn(current_board):
    human_move = 0
    possible_moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2]
    }

    result = ending_condition(current_board)
    if result is not None:
        return

    while human_move < 1 or human_move > 9:
        try:
            human_move = int(input('Choose field by typing number from 1 to 9: '))
            human_move_coordinates = possible_moves[human_move]
            valid_move = make_move(current_board, human_move_coordinates[0], human_move_coordinates[1], HUMAN_PLAYER)
            if not valid_move:
                print('Your move was invalid! Choose value from 1 to 9, try again.')
                human_move = 0
        except (EOFError, KeyboardInterrupt):
            print('\nThank you for the game!')
            exit()
        except (KeyError, ValueError):
            print('Your move was invalid! Choose value from 1 to 9, try again.')

def ai_player_turn(current_board, is_maximizing):
    depth = len(find_empty_fields(current_board))
    score = minimax(current_board, depth, -inf, inf, is_maximizing)
    make_move(current_board, score[0], score[1], AI_PLAYER)

def ending_condition(current_board):
    for i in range(3):
        # check all vertical lines 
        if current_board[0][i] != 0 and current_board[0][i] == current_board[1][i] == current_board[2][i]:
            return current_board[0][i]
        # check all horizontal lines 
        if current_board[i][0] != 0 and current_board[i][0] == current_board[i][1] == current_board[i][2]:
            return current_board[i][0]
    # Check first diagonal
    if current_board[0][0] != 0 and current_board[0][0] == current_board[1][1] == current_board[2][2]:
        return current_board[0][0] 
    # Check second diagonal
    if current_board[0][2] != 0 and current_board[0][2] == current_board[1][1] == current_board[2][0]:     
        return current_board[0][2]  
    # check if there are still empty fields when no one wins
    if len(find_empty_fields(current_board)) == 0:
        return 0 
    # return None if players can still play 
    return None
    
def minimax(current_board, depth, alpha, beta, is_maximizing):
    result = ending_condition(current_board)
    if result is not None:
        return [-1, -1, result]

    if(is_maximizing):
        best_score = [-1, -1, -inf]
        for i in range(3):
            for j in range(3):
                if current_board[i][j] == 0:
                    current_board[i][j] = AI_PLAYER
                    score = minimax(current_board, depth - 1, alpha, beta, not is_maximizing)
                    current_board[i][j] = 0
                    score[0], score[1] = i, j
                    if score[2] > best_score[2]:
                        best_score = score
                    alpha = max(best_score[2], alpha)
                    if alpha >= beta:
                        break
        return best_score
    else:
        best_score = [-1, -1, inf]
        for i in range(3):
            for j in range(3):
                if current_board[i][j] == 0:
                    current_board[i][j] = HUMAN_PLAYER
                    score = minimax(current_board, depth - 1, alpha, beta, not is_maximizing)
                    current_board[i][j] = 0
                    score[0], score[1] = i, j
                    if score[2] < best_score[2]:
                        best_score = score
                    beta = max(best_score[2], beta)
                    if alpha >= beta:
                        break
        return best_score

def print_board(current_board, ai_player_mark, human_player_mark):
    values = {
        -1: human_player_mark,
        0: ' ',
        1: ai_player_mark
    }
    row_border_line = '---------------'
    print(row_border_line)
    for row in current_board:
        for field in row:
            symbol = values[field]
            print(f'| {symbol} |', end='')
        print('\n' + row_border_line)

def make_move(current_board, x_coordinate, y_coordinate, current_player):
    if validate_move(current_board, x_coordinate, y_coordinate):
        current_board[x_coordinate][y_coordinate] = current_player
        return True
    else:
        return False

def validate_move(current_board, x_coordinate, y_coordinate):
    if [x_coordinate, y_coordinate] in find_empty_fields(current_board):
        return True
    else:
        return False

def find_empty_fields(current_board):
    empty_fields = []
    for x, row in enumerate(current_board):
        for y, field in enumerate(row):
            if field == 0:
                empty_fields.append([x, y])

    return empty_fields

def play():
    human_score , player_score = 0 , 0
    game_board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    
    human_player_mark = menu.choose_mark()
    if human_player_mark == 'X':
        ai_player_mark = 'O'
    else:
        ai_player_mark = 'X'

    human_player_first = False
    human_player_order = menu.choose_order()
    if human_player_order == 'Y':
        human_player_first = True

    
    while len(find_empty_fields(game_board)) > 0 and not ending_condition(game_board):
        
        menu.clear_screen()
        menu.print_info(ai_player_mark, human_player_mark)        
        # if tictactoe.ending_condition():
        #     exit(0)

        if human_player_first:
            print_board(game_board, ai_player_mark, human_player_mark)
            human_player_turn(game_board)
            ai_player_turn(game_board, True)
        else:
            ai_player_turn(game_board, True)
            print_board(game_board, ai_player_mark, human_player_mark)
            human_player_turn(game_board)
    
    menu.clear_screen()
    menu.print_info(ai_player_mark, human_player_mark)
    print_board(game_board, ai_player_mark, human_player_mark)
        
    return