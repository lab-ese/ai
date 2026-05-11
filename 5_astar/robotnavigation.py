"""
Robot Navigation — A* Search

Run (Windows):
    python robotnavigation.py
"""

import heapq


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
    out = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            out.append((nr, nc))
    return out


def astar(grid, start, goal):
    counter = 0
    heap = [(manhattan(start, goal), 0, counter, start, [start])]
    visited = {}

    while heap:
        f, g, _, pos, path = heapq.heappop(heap)
        if pos in visited and visited[pos] <= g:
            continue
        visited[pos] = g

        if pos == goal:
            return path, g, len(visited)

        for nb in neighbors(pos, grid):
            ng = g + 1
            nf = ng + manhattan(nb, goal)
            counter += 1
            heapq.heappush(heap, (nf, ng, counter, nb, path + [nb]))

    return None, 0, len(visited)


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
    print("  ROBOT NAVIGATION — A* SEARCH")
    print("=" * 40)
    print(f"Start: {START}  |  Goal: {GOAL}\n")
    print("Grid (# = obstacle):\n")
    print_grid(DEFAULT_GRID)

    path, cost, explored = astar(DEFAULT_GRID, START, GOAL)
    if path is None:
        print("No path found.")
        return

    print(f"Optimal path length: {cost}")
    print(f"Cells explored:      {explored}\n")
    print("Path:\n")
    print_grid(DEFAULT_GRID, path)


if __name__ == "__main__":
    main()
