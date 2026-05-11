"""
N-Queens Problem — Backtracking (Non-AI)

Run (Windows):
    python nqueens.py
"""


def is_safe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def solve(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions)
            board[row][col] = 0


def print_solution(board, n):
    for row in board:
        print(" " + " ".join("Q" if c == 1 else "." for c in row))
    print()


def main():
    n = int(input("Enter N (board size): "))
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions)

    print(f"\nFound {len(solutions)} solution(s) for {n}-Queens\n")
    if solutions:
        print("First solution:")
        print_solution(solutions[0], n)

        show_all = input("Show all solutions? (y/n): ").strip().lower()
        if show_all == "y":
            for i, sol in enumerate(solutions, 1):
                print(f"Solution {i}:")
                print_solution(sol, n)


if __name__ == "__main__":
    main()
