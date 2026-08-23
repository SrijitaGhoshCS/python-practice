#Program 35: Tic-Tac-Toe
# Program: Tic Tac Toe Game

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

def check_winner(board, player):
    # Winning combinations
    combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def tic_tac_toe():
    board = [" "]*9
    current_player = "X"

    for turn in range(9):
        print_board(board)
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Position already taken! Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")

# Run the game
tic_tac_toe()
