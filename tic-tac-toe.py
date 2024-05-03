board = []
print('|    ☛​  Tik tak toe ☚     |')

def init_board():
    for i in range(3):
        board.append([' - ',' - ',' - ',])

def print_board():
    print('|      | 1 | 2 | 3 |      |')
    for i,row in enumerate(board):
        print(f'|     {i+1}', end='|')
        for col in row:
            print(col, end='|')
        print("      |") 

def win_check():
    # check top row
    if board[0][0] == board[0][1] == board[0][2] and not board[0][0] == ' - ':
        return True
    # check middle row
    if board[1][0] == board[1][1] == board[1][2] and not board[1][0] == ' - ':
        return True
    # check bottom row
    if board[2][0] == board[2][1] == board[2][2] and not board[2][0] == ' - ':
        return True
    # check left column


playerCounter = 0
init_board()
print_board()

while True:

    token = ' X '
    if playerCounter % 2 == 0:
        token = ' O '

    print('')
    choice_col =int(input("choose row (1-3): "))-1
    choice_row =int(input("choose collome (1-3): "))-1
    print('')

    # check if row and column are between 1 and 3
    if (choice_row >= 0 and choice_row < 3) and (choice_col >= 0 and choice_col < 3):

        # check if coordinate is hyphen    
        if board[choice_col][choice_row] == ' - ':
            board[choice_col][choice_row] = token
            playerCounter += 1
        else:
            print("token already placed")

    else:
        print("invaled placement")
    
    
    if win_check():
        print("Win")
        
      
    print_board()

