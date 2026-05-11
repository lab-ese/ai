"""
8-Puzzle — Hill Climbing (Steepest Ascent)

Run (Windows):
    python 8puzzle.py
"""

GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def manhattan(board):
    dist = 0
    for r in range(3):
        for c in range(3):
            v = board[r][c]
            if v != 0:
                gr, gc = (v - 1) // 3, (v - 1) % 3
                dist += abs(r - gr) + abs(c - gc)
    return dist


def find_blank(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return r, c


def get_neighbors(board):
    r, c = find_blank(board)
    moves = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new = [row[:] for row in board]
            new[r][c], new[nr][nc] = new[nr][nc], new[r][c]
            moves.append(new)
    return moves


def print_board(board):
    for row in board:
        print("  " + " ".join(str(x) if x != 0 else "_" for x in row))
    print()


def hill_climbing(initial):
    current = [row[:] for row in initial]
    steps = 0
    path = [current]

    while True:
        if current == GOAL:
            return current, steps, path, True

        neighbors = get_neighbors(current)
        best = min(neighbors, key=manhattan)

        if manhattan(best) >= manhattan(current):
            return current, steps, path, False  # local max

        current = best
        path.append(current)
        steps += 1


def parse_board(text):
    nums = list(map(int, text.split()))
    if len(nums) != 9 or set(nums) != set(range(9)):
        raise ValueError("Need exactly 9 numbers (0-8)")
    return [nums[i:i + 3] for i in range(0, 9, 3)]


def main():
    print("=" * 40)
    print("  8-PUZZLE — HILL CLIMBING")
    print("=" * 40)
    print("Use 0 for blank tile.")
    print("Default initial: 1 2 3 4 0 6 7 5 8")

    choice = input("\nEnter board (9 nums) or press Enter for default: ").strip()
    if not choice:
        initial = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    else:
        initial = parse_board(choice)

    print("\nInitial state:")
    print_board(initial)

    print("Goal state:")
    print_board(GOAL)

    final, steps, path, success = hill_climbing(initial)

    print(f"Result: {'SOLVED' if success else 'STUCK AT LOCAL MAXIMUM'}")
    print(f"Steps: {steps}  |  Final h(Manhattan): {manhattan(final)}\n")

    print("Solution path:")
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print_board(state)


if __name__ == "__main__":
    main()
