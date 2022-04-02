from cmath import inf

AI_PLAYER = -1
HUMAN_PLAYER = 1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
def human_player_turn():
    human_move = 0
    possible_moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2]
    }

    while human_move < 1 or human_move > 9:
        try:
            human_move = int(input('Choose field by typing number from 1 to 9: '))
            human_move_coordinates = possible_moves[human_move]
            valid_move = make_move(human_move_coordinates[0], human_move_coordinates[1], HUMAN_PLAYER)
            if not valid_move:
                print('Your move was invalid! Choose value from 1 to 9, try again.')
                human_move = 0
        except (EOFError, KeyboardInterrupt):
            print('\nThank you for the game!')
            exit()
        except (KeyError, ValueError):
            print('Your move was invalid! Choose value from 1 to 9, try again.')

def ai_player_turn():
    depth = len(find_empty_fields())
    if depth == 0 or ending_condition():
        return

    ai_player_move = minimax(depth, alpha, beta, AI_PLAYER)
    make_move(ai_player_move[0], ai_player_move[1], AI_PLAYER)

def ending_condition():
    return
    
def minimax(depth, alpha, beta, is_maximazing_player):
    
    if is_maximazing_player == AI_PLAYER:
        
        max_value = inf
        
        for child in find_empty_fields():
            
            value = minimax(child, depth - 1, alpha, beta, False)
            
            max_value = max(value, max_value)
            alpha = max(alpha, value)
            
            if beta <= alpha:
                break
            
            return max_value
    else:
        min_value = -inf
        for child in find_empty_fields():
            
            value = minimax(child, depth - 1, alpha, beta, True)
            
            min_value = min(value, min_value)
            beta = min(beta, value)

            if beta <= alpha:
                break

            return min_value
                    
def print_board(ai_player_mark, human_player_mark):
    values = {
        -1: ai_player_mark,
        0: ' ',
        1: human_player_mark
    }
    row_border_line = '---------------'
    print(row_border_line)
    for row in board:
        for field in row:
            symbol = values[field]
            print(f'| {symbol} |', end='')
        print('\n' + row_border_line)

def make_move(x_coordinate, y_coordinate, current_player):
    if validate_move(x_coordinate, y_coordinate):
        board[x_coordinate][y_coordinate] = current_player
        return True
    else:
        return False

def validate_move(x_coordinate, y_coordinate):
    if [x_coordinate, y_coordinate] in find_empty_fields():
        return True
    else:
        return False

def find_empty_fields():
    empty_fields = []
    for x, row in enumerate(board):
        for y, field in enumerate(row):
            if field == 0:
                empty_fields.append([x, y])

    return empty_fields

