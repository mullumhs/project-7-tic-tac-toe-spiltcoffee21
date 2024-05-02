board = []
print('|      ☛​tik tak toe☚      |')

def init_board():
    for i in range(3):
        board.append([' - ',' - ',' - ',])

def print_board():
    print('|      | 1 | 2 | 3 |      |')
    for row in board:
        print('|      ', end='|')
        for col in row:
            print(col, end='|')
        print("      |") 

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
    

    # check if coordinate is hyphen
   
    board[choice_col][choice_row] = token
    playerCounter += 1    
      
    print_board()
