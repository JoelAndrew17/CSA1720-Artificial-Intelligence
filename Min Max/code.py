import math

def evaluate(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 10
        elif all(cell == 'O' for cell in row):
            return -10

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 10
        elif all(board[row][col] == 'O' for row in range(3)):
            return -10

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)):
        return 10
    elif all(board[i][2-i] == 'X' for i in range(3)):
        return 10
    elif all(board[i][i] == 'O' for i in range(3)):
        return -10
    elif all(board[i][2-i] == 'O' for i in range(3)):
        return -10

    # No winner
    return 0

def is_moves_left(board):
    return any(cell == ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_val = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best_val = max(best_val, minimax(board, depth+1, not is_maximizing))
                    board[i][j] = ' '
        return best_val
    else:
        best_val = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best_val = min(best_val, minimax(board, depth+1, not is_maximizing))
                    board[i][j] = ' '
        return best_val

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe (Minimax Edition)!")
    print_board(board)

    while True:
        player_row, player_col = map(int, input("Enter row and column number (1-3) for your move: ").split())
        player_row -= 1
        player_col -= 1

        if board[player_row][player_col] != ' ':
            print("That cell is already occupied. Please choose another.")
            continue

        board[player_row][player_col] = 'O'
        print_board(board)

        if evaluate(board) == -10:
            print("You win!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break

        print("Computer is making a move...")
        computer_row, computer_col = find_best_move(board)
        board[computer_row][computer_col] = 'X'
        print_board(board)

        if evaluate(board) == 10:
            print("Computer wins!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
