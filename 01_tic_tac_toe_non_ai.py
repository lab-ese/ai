import random

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    win_configs = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # cols
        (0, 4, 8), (2, 4, 6)             # diags
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_configs)

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == " "]

def find_best_move(board, player):
    """Rule-based Non-AI Logic: Win > Block > Center > Corner > Edge"""
    empty = get_empty_cells(board)
    opponent = "O" if player == "X" else "X"

    # 1. WIN: If there is a move that wins, take it.
    for move in empty:
        board[move] = player
        if check_winner(board, player):
            board[move] = " " # reset
            return move
        board[move] = " "

    # 2. BLOCK: If the opponent can win, block them.
    for move in empty:
        board[move] = opponent
        if check_winner(board, opponent):
            board[move] = " " # reset
            return move
        board[move] = " "

    # 3. CENTER: Take center if available.
    if 4 in empty:
        return 4

    # 4. CORNERS: Take any available corner.
    corners = [c for c in [0, 2, 6, 8] if c in empty]
    if corners:
        return random.choice(corners)

    # 5. EDGES: Take any available edge.
    edges = [e for e in [1, 3, 5, 7] if e in empty]
    if edges:
        return random.choice(edges)
    
    return None

def play_tic_tac_toe():
    board = [" "] * 9
    print("--- TIC TAC TOE: NON-AI (Rule-Based) ---")
    print("Positions: 0 | 1 | 2")
    print("           3 | 4 | 5")
    print("           6 | 7 | 8")
    
    human = "X"
    computer = "O"
    current_player = human # Human starts first

    for turn in range(9):
        print_board(board)
        
        if current_player == human:
            while True:
                try:
                    move = int(input(f"Your move (0-8): "))
                    if move in get_empty_cells(board):
                        break
                    print("Invalid move! Cell already taken or out of range.")
                except (ValueError, IndexError):
                    print("Invalid input! Please enter a number between 0-8.")
        else:
            print("Computer is thinking...")
            move = find_best_move(board, computer)
            print(f"Computer chose: {move}")

        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Game Over! {'You win!' if current_player == human else 'Computer wins!'}")
            return

        current_player = computer if current_player == human else human
        
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
