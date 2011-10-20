# a Two Olayer TicTacTow
a0,a1,a2,b0,b1,b2,c0,c1,c2 = 1,2,3,4,5,6,7,8,9
r0,r1,r2                   = -1,-2,-3
row,column = 0,0


blankIdentifier = [1,2,3,4,5,6,7,8,9,-1,-2,-3] 
endIdentifier = [3,7,11]
board = [
            [a0,a1,a2,r0],
            [b0,b1,b2,r1],
            [c0,c1,c2,r2]         
        ]

blank_board = """
  1 2 3
1 _|_|_
2 _|_|_
3  | |

"""


def print_board():
    """
        >>> prints Tic Tac Toe board state.
    """
    colCount = 
    print("\n")
    for i in board:
        ind_row = board.index(i)        
        for ii in i:
            ind_col = i.index(ii)
            colCount += 1
  
            if ind_row == 2:
                if ii in blankIdentifier:
                    if ind_col == 3:
                        print()
                    else:
                        if ind_col == 2:
                            print(' ', end='')
                        else:
                            print(' ', end='|')
                elif colCount not in endIdentifier:
                    print(ii, end='|')
                else:
                    print(ii, end='')
            else:
                if ii in blankIdentifier:
                    if ind_col == 3:
                        print()
                    else:
                        if ind_col == 2:
                            print('_', end='')
                        else:
                            print('_', end='|')
                elif colCount not in endIdentifier:
                    print(ii, end='|')
                else:
                    print(ii, end='')
    print("\n")

def check_move():
    
    global move, row, column
    move = input("enter :\nRow,Column:\t").strip()
    while True:
        if (len(move) == 3) and \
        (move[1] == ',') and \
        (move[0].isnumeric() == True) and \
        (move[2].isnumeric() == True):
                                        
            row    = (int(move[0]) - 1) 
            column = (int(move[2]) - 1) 
            
            if (0 <= row <= 2) and \
               (0 <= column <= 2) :                
          
                if (board[row][column] != 'X'): 
                    if (board[row][column] != 'O'):
                       break
                    else:
                        move = input \
            ("Sorry, Player 2 is already there! Enter!\nRow,Column:\t").strip()
                else:
                    move = input \
            ("Sorry, Player 1 is already there! Enter!\nRow,Column:\t").strip()
            else:
                move = input \
            ("Invalid move. Try Again!\nRow,Column:\t").strip()
        else:
            move = input \
            ("Check format. Try Again!\nRow,Column:\t").strip()

            
def place_move():
    global row, column, t

    if t % 2 == 0: #<player 1>#
        board[row][column]='X'
    if t % 2 != 0: #<player 2>#
        board[row][column]='O'
    t += 1   
    
def check_win():
    
    global t
    if (    ['X','X','X',-1] in board or  \
            ['O','O','O',-1] in board or   \
            ['X','X','X',-2] in board or    \
            ['O','O','O',-2] in board or     \
            ['X','X','X',-3] in board or      \
            ['O','O','O',-3] in board or       \
            (board[0][0] == board[1][0] == board[2][0]) or \
            (board[0][1] == board[1][1] == board[2][1]) or  \
            (board[0][2] == board[1][2] == board[2][2]) or   \
            (board[0][0] == board[1][1] == board[2][2]) or    \
            (board[0][2] == board[1][1] == board[2][0]) ):
        t = -1*(t-1)
        
while True:
    start = input ("""
Welcome to Tic Tac Toe!

IF you would like to play, then just type anything.

""").capitalize().strip()
    
        break

print(blank_board)

t = 0
while 0 <= t < 9:

    if t % 2 == 0:
        print ("Player 1", end=', ')
        check_move()
        place_move()
        check_win()
        print_board()
    elif t % 2 != 0:
        print ("Player 2", end=', ')
        check_move()
        place_move()
        check_win()
        print_board()


if t == 9:
    print("""
It's a draw! Try harder next time.
""")
    
elif t % 2 == 0:
    print("""
Congratulations Player 1! You've won!
""")
    
elif t % 2 != 0:
    print("""
Congratulations Player 2! You've won!
""")

print ("\nThanks!\n")