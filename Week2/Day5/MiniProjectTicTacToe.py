board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def display_board():
    print('TIC TAC TOE')
    print("*************************")
    for row in board :
        print("*      " + row[0] + "  |   " + row[1] + "  |  " + row[2] + "      *")
        print("*    --- | --- | ---    *")
    print("*************************")

def check_win() :
    if board[0][0] == board[0][1] == board[0][2] != '' or \
       board[1][0] == board[1][1] == board[1][2] != '' or \
       board[2][0] == board[2][1] == board[2][2] != '' or \
       board[0][0] == board[1][0] == board[2][0] != '' or \
       board[0][1] == board[1][1] == board[2][1] != '' or \
       board[0][2] == board[1][2] == board[2][2] != '' or \
       board[0][0] == board[1][1] == board[2][2] != '' or \
       board[0][2] == board[1][1] == board[2][0] != '':
       return True
    else :
       return False
   


        
print()
print('Welcome to TIC TAC TOE!')
print()   
display_board()
print()

# Choose your variable
player_1 = input('Players 1: please choose X or O: ').upper()
player_2 = ''
while player_1 not in ['X', 'O'] :
    player_1 = input('Invalid entry. Players 1: please choose X or O: ').upper()
if player_1 == 'X' :
    player_2 = 'O'
else :
    player_1 = 'O'
    player_2 = 'X'


# Start playing
for num in range(1, 10) :
    print(f'Round number {num}:')
    if num % 2 !=0 and check_win()==False :
        print('Player 1, its your turn...')
        player_row = int(input('Enter row: '))
        player_column = int(input('Enter column: '))
        while board[player_row][player_column] != '':
            player_row = int(input('That spot is taken. Enter row: '))
            player_column = int(input('Enter column: '))
        board[player_row][player_column] = player_1 
        display_board()
    elif num % 2 ==0 and check_win()==False :
        print('Player 2, its your turn...')
        player_row = int(input('Enter row: '))
        player_column = int(input('Enter column: '))
        while board[player_row][player_column] != '':
            player_row = int(input('That spot is taken. Enter row: '))
            player_column = int(input('Enter column: '))
        board[player_row][player_column] = player_2
        display_board()
    else :
       if check_win () :
        print('You win!') 
    
      