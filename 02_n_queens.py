def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1 # Place queen

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, 
            # then backtrack: remove queen
            board[i][col] = 0

    return False

def print_board(board, n):
    print(f"\nSolution for {n}-Queens:")
    print("-" * (n * 2 + 1))
    for row in board:
        print("|" + "|".join("Q" if x else " " for x in row) + "|")
    print("-" * (n * 2 + 1))

if __name__ == "__main__":
    print("--- N-QUEENS PROBLEM (BACKTRACKING) ---")
    try:
        n_input = int(input("Enter the number of Queens (N): "))
        if n_input <= 0:
            print("N must be a positive integer.")
        elif n_input in [2, 3]:
            print(f"No solution exists for {n_input}-Queens.")
        else:
            # Initialize board with 0s
            chess_board = [[0 for _ in range(n_input)] for _ in range(n_input)]
            
            if solve_n_queens(chess_board, 0, n_input):
                print_board(chess_board, n_input)
            else:
                print("No solution exists.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
