"""
N-Puzzle — A* Search (f(n) = g(n) + h(n))

Run (Windows):
    python npuzzle.py
"""

import heapq


def manhattan(board, n):
    dist = 0
    for r in range(n):
        for c in range(n):
            v = board[r][c]
            if v != 0:
                gr, gc = (v - 1) // n, (v - 1) % n
                dist += abs(r - gr) + abs(c - gc)
    return dist


def goal_state(n):
    goal = [[(r * n + c + 1) % (n * n) for c in range(n)] for r in range(n)]
    return goal


def find_blank(board, n):
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                return r, c


def neighbors(board, n):
    r, c = find_blank(board, n)
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            new = [row[:] for row in board]
            new[r][c], new[nr][nc] = new[nr][nc], new[r][c]
            result.append(new)
    return result


def board_key(b):
    return tuple(tuple(r) for r in b)


def astar(initial, n):
    goal = goal_state(n)
    counter = 0
    h0 = manhattan(initial, n)
    heap = [(h0, 0, counter, initial, [initial])]
    visited = {}

    while heap:
        f, g, _, current, path = heapq.heappop(heap)
        key = board_key(current)
        if key in visited and visited[key] <= g:
            continue
        visited[key] = g

        if current == goal:
            return path, g, len(visited)

        for nb in neighbors(current, n):
            ng = g + 1
            nf = ng + manhattan(nb, n)
            counter += 1
            heapq.heappush(heap, (nf, ng, counter, nb, path + [nb]))

    return None, 0, len(visited)


def print_board(b, n):
    width = len(str(n * n - 1)) + 1
    for row in b:
        print(" ".join(f"{x:>{width}}" if x != 0 else " " * width + "_" for x in row).rstrip())
    print()


def parse_board(text, n):
    nums = list(map(int, text.split()))
    expected = n * n
    if len(nums) != expected or set(nums) != set(range(expected)):
        raise ValueError(f"Need exactly {expected} numbers (0-{expected - 1})")
    return [nums[i:i + n] for i in range(0, expected, n)]


def main():
    print("=" * 40)
    print("  N-PUZZLE — A* SEARCH")
    print("=" * 40)
    n = int(input("Puzzle size N (3 for 8-puzzle, 4 for 15-puzzle): "))

    default_3 = "1 2 3 4 0 6 7 5 8"
    print(f"\nDefault (n=3): {default_3}")
    text = input(f"Enter {n * n} numbers or press Enter for default: ").strip()

    if not text and n == 3:
        initial = parse_board(default_3, n)
    else:
        initial = parse_board(text, n)

    print("\nInitial:")
    print_board(initial, n)
    print("Goal:")
    print_board(goal_state(n), n)

    path, cost, explored = astar(initial, n)
    if path is None:
        print("No solution found.")
        return

    print(f"Solved! Optimal moves: {cost}")
    print(f"States explored:      {explored}\n")

    if input("Show full path? (y/n): ").strip().lower() == "y":
        for i, state in enumerate(path):
            print(f"Step {i}:")
            print_board(state, n)


if __name__ == "__main__":
    main()
