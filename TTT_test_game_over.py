# test row wins

for winner in [1, 2]:
    print ('Testing row wins for winner: ', winner)
    game_board = [[winner] * 3] + [[0] * 3 for i in range(2)]
    print check_game_over(game_board)
    print_board(game_board)
    game_board = [[0] * 3, [winner] * 3, [0] * 3]
    print check_game_over(game_board)
    print_board(game_board)
    game_board = [[0] * 3 for i in range(2)] + [[winner] * 3]
    print check_game_over(game_board)
    print_board(game_board)

# test col wins

    print ('Testing col wins for winner: ', winner)
    game_board = [[winner, 0, 0] for i in range(3)]
    print check_game_over(game_board)
    print_board(game_board)
    game_board = [[0, winner, 0] for i in range(3)]
    print check_game_over(game_board)
    print_board(game_board)
    game_board = [[0, 0, winner] for i in range(3)]
    print check_game_over(game_board)
    print_board(game_board)

# test cross wins

    print ('Testing cross wins for winner: ', winner)
    game_board = [[winner, 0, 0], [0, winner, 0], [0, 0, winner]]
    print check_game_over(game_board)
    print_board(game_board)
    game_board = [[0, 0, winner], [0, winner, 0], [winner, 0, 0]]
    print check_game_over(game_board)
    print_board(game_board)

# test ties

print 'Testing not game over'
game_board = [[0] * 3 for i in range(3)]
for r in range(2):
    for c in range(3):
        game_board[r][c] = (r * 3 + c) % 2 + 1
        print check_game_over(game_board)
        print_board(game_board)
game_board[2] = [2, 0, 0]
print check_game_over(game_board)
print_board(game_board)
game_board[2] = [2, 1, 0]
print check_game_over(game_board)
print_board(game_board)
game_board[2] = [2, 1, 2]
print check_game_over(game_board)
print_board(game_board)

quit()
