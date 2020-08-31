from IPython.display import clear_output

def display_board(board):
    print('   |   |  ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-----------')
    print('   |   |  ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-----------')
    print('   |   |  ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')

def player_input():
    marker = ''

    #Keep asking Player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O: ')

    #Assign Player 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'
    return (player1,player2)


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return(board[7] == mark and board[8] == mark and board[9] == mark or #across the top
        board[4] == mark and board[5] == mark and board[6] == mark or #across the middle
        board[1] == mark and board[2] == mark and board[3] == mark or #across the bottom
        board[1] == mark and board[4] == mark and board[7] == mark or #up the left side
        board[2] == mark and board[5] == mark and board[8] == mark or #up the middle
        board[3] == mark and board[6] == mark and board[9] == mark or #up the right
        board[1] == mark and board[5] == mark and board[9] == mark or #bottom to up right diagonal
        board[3] == mark and board[5] == mark and board[7] == mark) #bottom to up left diagonal

test_board = ['#','X','O','X','O','X','O','X','O','X']
#test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(test_board)
player1_variable, player2_variable = player_input()

place_marker(test_board,'$',8)
display_board(test_board)
win_check(test_board,'X')