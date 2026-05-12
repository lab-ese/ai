import math

# Board
board = [
    ['X', ' ', ' '],
    [' ', 'O', ' '],
    [' ', ' ', ' ']
]

# ---------------- PRINT BOARD ----------------
def print_board():
    for r in board:
        print(" | ".join(r))
        print("-" * 9)

# ---------------- CHECK WIN ----------------
def is_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# ---------------- CHECK DRAW ----------------
def is_full():
    return all(cell != ' ' for row in board for cell in row)

# ---------------- MINIMAX ----------------
def minimax(is_max):
    if is_winner('X'):
        return 10
    if is_winner('O'):
        return -10
    if is_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    val = minimax(False)
                    board[i][j] = ' '
                    best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    val = minimax(True)
                    board[i][j] = ' '
                    best = min(best, val)
        return best

# ---------------- FIND BEST MOVE ----------------
def best_move(player):
    best_val = -math.inf if player == 'X' else math.inf
    move = None

    print("\nMove evaluations:")

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player

                val = minimax(player == 'O')

                print(f"Move ({i}, {j}) -> Value: {val}")

                board[i][j] = ' '

                if (player == 'X' and val > best_val) or \
                   (player == 'O' and val < best_val):
                    best_val = val
                    move = (i, j)

    print(f"Best Move: {move} with value {best_val}")
    return move

# ---------------- TURN DETECTION ----------------
def detect_turn():
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    return 'X' if x_count == o_count else 'O'

# ---------------- MAIN LOOP ----------------
print("Initial Board:")
print_board()

while True:
    turn = detect_turn()
    print(f"\nTurn: {turn}")

    move = best_move(turn)

    if move:
        board[move[0]][move[1]] = turn

    print_board()

    if is_winner(turn):
        print(f"\n{turn} wins!")
        break

    if is_full():
        print("\nGame Draw!")
        break