"""
Tic Tac Toe — Minimax Algorithm with Alpha-Beta Pruning

Run (Windows):
    python tictactoe.py
"""


WINS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
]


def check_winner(board):
    for a, b, c in WINS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(v is not None for v in board):
        return "draw"
    return None


def minimax(board, is_max, depth, alpha, beta):
    result = check_winner(board)
    if result == "O":    return 10 - depth   # AI wins
    if result == "X":    return depth - 10   # Human wins
    if result == "draw": return 0

    if is_max:
        best = -1000
        for i in range(9):
            if board[i] is None:
                board[i] = "O"
                best = max(best, minimax(board, False, depth + 1, alpha, beta))
                board[i] = None
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] is None:
                board[i] = "X"
                best = min(best, minimax(board, True, depth + 1, alpha, beta))
                board[i] = None
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


def best_move(board):
    best_score, best_idx = -1000, -1
    for i in range(9):
        if board[i] is None:
            board[i] = "O"
            score = minimax(board, False, 0, -1000, 1000)
            board[i] = None
            if score > best_score:
                best_score, best_idx = score, i
    return best_idx


def print_board(board):
    print()
    for i in range(3):
        row = board[i * 3:(i + 1) * 3]
        print(" " + " | ".join(v if v else str(i * 3 + j + 1) for j, v in enumerate(row)))
        if i < 2:
            print("---+---+---")
    print()


def main():
    print("=" * 40)
    print("  TIC TAC TOE — MINIMAX AI (unbeatable)")
    print("=" * 40)
    print("You = X    AI = O    (enter cell 1-9)\n")

    board = [None] * 9
    current = "X"

    while True:
        print_board(board)
        result = check_winner(board)
        if result:
            if result == "draw":
                print("DRAW!")
            elif result == "X":
                print("You WIN!")
            else:
                print("AI WINS!")
            break

        if current == "X":
            try:
                pos = int(input("Your move (1-9): ")) - 1
            except ValueError:
                print("Invalid input.")
                continue
            if not (0 <= pos < 9) or board[pos] is not None:
                print("Invalid cell.")
                continue
            board[pos] = "X"
            current = "O"
        else:
            print("AI is thinking...")
            pos = best_move(board)
            board[pos] = "O"
            print(f"AI plays cell {pos + 1}")
            current = "X"


if __name__ == "__main__":
    main()
