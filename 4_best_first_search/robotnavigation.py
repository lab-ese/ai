"""
Robot Navigation — Greedy Best First Search

Run (Windows):
    python robotnavigation.py
"""

import heapq


# 0 = free, 1 = obstacle.  S = start, G = goal.
DEFAULT_GRID = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
START = (0, 0)
GOAL  = (9, 9)


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def neighbors(pos, grid):
    r, c = pos
    rows, cols = len(grid), len(grid[0])
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            result.append((nr, nc))
    return result


def best_first_search(grid, start, goal):
    counter = 0
    heap = [(manhattan(start, goal), counter, start, [start])]
    visited = set()

    while heap:
        h, _, pos, path = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)

        if pos == goal:
            return path, len(visited)

        for nb in neighbors(pos, grid):
            if nb not in visited:
                counter += 1
                heapq.heappush(heap, (manhattan(nb, goal), counter, nb, path + [nb]))

    return None, len(visited)


def print_grid(grid, path=None):
    path_set = set(path) if path else set()
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[0])):
            if (r, c) == START:
                line += "S "
            elif (r, c) == GOAL:
                line += "G "
            elif (r, c) in path_set:
                line += "* "
            elif grid[r][c] == 1:
                line += "# "
            else:
                line += ". "
        print(line)
    print()


def main():
    print("=" * 40)
    print("  ROBOT NAVIGATION — BEST FIRST SEARCH")
    print("=" * 40)
    print(f"Start: {START}  |  Goal: {GOAL}\n")
    print("Initial grid (# = obstacle):\n")
    print_grid(DEFAULT_GRID)

    path, explored = best_first_search(DEFAULT_GRID, START, GOAL)
    if path is None:
        print("No path found.")
        return

    print(f"Path length: {len(path) - 1}")
    print(f"Cells explored: {explored}\n")
    print("Final path:\n")
    print_grid(DEFAULT_GRID, path)


if __name__ == "__main__":
    main()
