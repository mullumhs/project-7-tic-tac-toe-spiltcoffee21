# Your code goes here
board = []

print('|       connect four        |')

def init_board():
    for i in range(6):
        board.append([' - ',' - ',' - ',' - ',' - ',' - ',' - '])

def print_board():
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
    for row in board:
        print('', end='|')
        for col in row:
            print(col, end='|')
        print() 

playerCounter = 1
init_board()
print_board()

while True:

    token = ' X '
    if playerCounter % 2 == 0:
        token = ' O '

    print('')
    choice =int(input("choose column (1-7): "))
    print('')
    choice -= 1
#across
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and not board[row][col + 3] == ' - ':
                print("your woner")
                break

   #up
    for row in range(3):
        for col in range(6):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and not board[row + 3][col] == ' - ':
                print("your woner")
                break
   
   
    for i in range (5, -1, -1):


        if board[i][choice] == ' - ':
            board[i][choice] = token
            playerCounter += 1
            break

    print_board()
