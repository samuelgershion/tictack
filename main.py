import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def evaluate_board(board):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, is_maximizing):
    score = evaluate_board(board)

    if score is not None:
        return score

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_over = False

    while not game_over:
        print_board(board)

        # Get valid user input for row
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                if 0 <= row <= 2:
                    break
                else:
                    print("Invalid row. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get valid user input for column
        while True:
            try:
                col = int(input("Enter the column (0, 1, or 2): "))
                if 0 <= col <= 2:
                    break
                else:
                    print("Invalid column. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        if is_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            game_over = True
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
            break

        print("AI is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = "O"

        if is_winner(board, "O"):
            print_board(board)
            print("AI wins! Better luck next time.")
            game_over = True
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
            break

play_tic_tac_toe()
