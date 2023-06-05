def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def get_move(board, player):
    while True:
        row = int(input(f"Player {player}, enter row number (1-3): "))
        col = int(input(f"Player {player}, enter column number (1-3): "))
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid input, try again!")
        elif board[row-1][col-1] != " ":
            print("That spot is already taken, try again!")
        else:
            return (row-1, col-1)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    players = ["X", "O"]
    turn = 0
    while True:
        player = players[turn]
        row, col = get_move(board, player)
        board[row][col] = player
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        elif all(all(row) for row in board):
            print("It's a tie!")
            break
        turn = (turn + 1) % 2

tic_tac_toe()
