"""
Tic Tac Toe — Non-AI Implementation (Rule-Based, Two Player)

Run (Windows):
    python tictactoe.py
"""


def print_board(board):
    print()
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    lines = []
    for i in range(3):
        lines.append(board[i])                        # rows
        lines.append([board[r][i] for r in range(3)]) # cols
    lines.append([board[i][i] for i in range(3)])     # main diagonal
    lines.append([board[i][2 - i] for i in range(3)]) # anti diagonal

    for line in lines:
        if line[0] == line[1] == line[2] != " ":
            return line[0]
    if all(board[r][c] != " " for r in range(3) for c in range(3)):
        return "draw"
    return None


def main():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    print("=" * 30)
    print("  TIC TAC TOE (Two Player)")
    print("=" * 30)
    print("Enter row (1-3) and column (1-3) separated by space")

    while True:
        print_board(board)
        try:
            move = input(f"Player {player} - enter row col: ").split()
            r, c = int(move[0]) - 1, int(move[1]) - 1
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        if not (0 <= r < 3 and 0 <= c < 3):
            print("Out of range!")
            continue
        if board[r][c] != " ":
            print("Cell already taken!")
            continue

        board[r][c] = player
        result = check_winner(board)
        if result:
            print_board(board)
            if result == "draw":
                print("It's a DRAW!")
            else:
                print(f"Player {result} WINS!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
