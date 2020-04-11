#Tic-Tac-Toe using two dimensional array
import copy # need this to make a copy of 2D list

# This procedure prints the game table showing the Xs, Os, and empty slots
# and the number to enter for the empty slots
def print_board(gt):
    #gt is the game table
    for row in range(3):
        for col in range(3):
            print(xo_str[gt[row][col]],end=divider[col])
        for col in range(3):
            print(xo_str[0] if gt[row][col] else num_str[row][col], end=divider[col])
        print("\n",line[row],"\t\t",line[row],sep="")

def disp_game_over(gt, winner):
    global xo_str
    print_board(gt)
    if winner:
        print("Game over! ",xo_str[winner], "is the winner!\n\n")
    else:
        print("Game over! We have a tie.\n\n")

# Heuristic based AI move
# inputs:
#   gt: game board
# returns:
#   the best move a tuple (row, col)
def ai_next_move_heuristic(gb):
    return (0,0)

# This procedure checks if the game is over
# returns a tuple (game_over(T/F), the player who won):
#   True/False indicating if the game is over
#   The winner (value of 1 or 2) or 0 for tie
def check_game_over(gt):
    # check the rows first
    for i in range(3):
        # check the row
        if gt[i][0] and len(set(gt[i]))==1:
            return True, gt[i][0]
        # check the colum
        if gt[0][i] and len(set([gt[_][i] for _ in range(3)]))==1:
            return True, gt[0][i] 
    # check the crosses
    if gt[0][0] and len(set([gt[i][i] for i in range(3)])) == 1:
        return True, gt[0][0]
    if gt[0][2] and len(set([gt[i][2-i] for i in range(3)]))==1:
        return True, gt[0][2]
    # check for a tie
    return (True,0) if sum(x.count(0) for x in gt)==0 else (False,0)

##################################
# Start of main code
##################################

line = ["-"*11,"-"*11,""]
divider = ["|","|","\t\t"]
num_str =  [[" 1 ", " 2 ", " 3 "],
            [" 4 ", " 5 ", " 6 "],
            [" 7 ", " 8 ", " 9 "]]
# can do this instead
#num_str = [[" "+str(c+r*3)+" " for c in range(1,4)] for r in range(3)] 
 
xo_str = ["   ", " O "," X "]

turn_str = ["","O's turn, plase make your move: ", "X's turn, please make your move: "]
turn_val = [0,1,2]

while True:
    turn = -1
    game_over=False
    game_table = [[0]*3 for _ in range(3)]  # 3x3 table to hold the game table
    while not game_over:
        # switch turns
        turn *= -1
        
        print("Game Table\t\tEmpty Slot Num")
        print_board(game_table)

        if turn==-1:
            # AI's turn
            move_row, move_col = ai_next_move_heuristic(game_table)
            # no need to double check the move since it's done by AI
            game_table[move_row][move_col] = turn_val[turn]
            print("AI Move: ",move_row*3+move_col)
        else:
            # Human's turn
            while True:
                # prompt users for their "move"
                move = input(turn_str[turn])
                if move in [str(i) for i in range(1,10)]:
                    move = int(move) - 1
                    if move in range(0,9) and not game_table[move//3][move%3]:
                        #update the game table with the "correct" turn (move)
                        game_table[move//3][move%3] = turn_val[turn]
                        break
                print("Error: invalid move!")
        game_over, winner = check_game_over(game_table)
        if game_over:
            disp_game_over(game_table, winner)
    print("\n\n********** New Game **********\n\n")
