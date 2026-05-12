import math

def check_winner(board):
    win_configs = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in win_configs:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board: return "Tie"
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 10 - depth
    if winner == "X": return depth - 10
    if winner == "Tie": return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def get_computer_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("---+---+---")
    print("\n")

def play_game():
    board = [" "] * 9
    print("--- TIC TAC TOE (MINIMAX AI) ---")
    current_player = "X"
    for turn in range(9):
        print_board(board)
        if current_player == "X":
            while True:
                try:
                    move = int(input("Your move (0-8): "))
                    if board[move] == " ": break
                    print("Occupied!")
                except: print("Invalid input!")
        else:
            print("AI is thinking...")
            move = get_computer_move(board)
            print(f"AI chose: {move}")
        board[move] = current_player
        res = check_winner(board)
        if res:
            print_board(board)
            print("Tie!" if res == "Tie" else f"Player {res} wins!")
            return
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
