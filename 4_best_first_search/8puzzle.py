"""
8-Puzzle — Greedy Best First Search

Run (Windows):
    python 8puzzle.py
"""

import heapq

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


def board_key(board):
    return tuple(tuple(r) for r in board)


def best_first_search(initial):
    counter = 0
    heap = [(manhattan(initial), counter, initial, [initial])]
    visited = set()

    while heap:
        h, _, current, path = heapq.heappop(heap)
        key = board_key(current)
        if key in visited:
            continue
        visited.add(key)

        if current == GOAL:
            return path, len(visited)

        for nb in get_neighbors(current):
            if board_key(nb) not in visited:
                counter += 1
                heapq.heappush(heap, (manhattan(nb), counter, nb, path + [nb]))

    return None, len(visited)


def print_board(board):
    for row in board:
        print("  " + " ".join(str(x) if x != 0 else "_" for x in row))
    print()


def parse_board(text):
    nums = list(map(int, text.split()))
    if len(nums) != 9 or set(nums) != set(range(9)):
        raise ValueError("Need exactly 9 numbers (0-8)")
    return [nums[i:i + 3] for i in range(0, 9, 3)]


def main():
    print("=" * 40)
    print("  8-PUZZLE — GREEDY BEST FIRST SEARCH")
    print("=" * 40)
    print("Default initial: 1 2 3 4 0 6 7 5 8")

    choice = input("\nEnter board (9 nums) or press Enter for default: ").strip()
    initial = parse_board(choice) if choice else [[1, 2, 3], [4, 0, 6], [7, 5, 8]]

    print("\nInitial:")
    print_board(initial)
    print("Goal:")
    print_board(GOAL)

    path, explored = best_first_search(initial)

    if path is None:
        print("No solution found.")
        return

    print(f"Solution found in {len(path) - 1} moves.")
    print(f"States explored: {explored}\n")

    show = input("Show full path? (y/n): ").strip().lower()
    if show == "y":
        for i, state in enumerate(path):
            print(f"Step {i}:")
            print_board(state)


if __name__ == "__main__":
    main()
