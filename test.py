board_space = [' ' for i in range(1,10)]

#print(board_space[3]+ 'There')

def square_board(board):
    for row in  [board[i*3:(i+1)*3] for i in range(3)]:
        print(' | '.join(row))

turn = 'X'
for i in range(1, 10):
    #Print the board
    square_board(board_space)
    #get an input for user and insert in to board_space
    # check if input is valid
    square = int(input(f'Its {turn}\'s turn Enter a value between 0 - 8: '))
    board_space[square] = turn
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'  


square_board(board_space)
