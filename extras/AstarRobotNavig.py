import heapq

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic: Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    pq = []

    heapq.heappush(pq, (0, start[0], start[1], []))

    visited = set()

    g_cost = {start: 0}

    while pq:

        f, r, c, path = heapq.heappop(pq)

        if (r, c) == goal:
            return path + [(r, c)]

        if (r, c) in visited:
            continue

        visited.add((r, c))

        for dr, dc in directions:

            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == 0):

                new_g = g_cost[(r, c)] + 1

                if ((nr, nc) not in g_cost or
                    new_g < g_cost[(nr, nc)]):

                    g_cost[(nr, nc)] = new_g

                    h = heuristic((nr, nc), goal)

                    f_cost = new_g + h

                    heapq.heappush(
                        pq,
                        (f_cost, nr, nc, path + [(r, c)])
                    )

    return None


# -------- INPUT --------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the grid (0 = free, 1 = obstacle):")

grid = []

for i in range(rows):

    row = list(map(int, input().split()))

    grid.append(row)


start_row = int(input("Enter start row: "))
start_col = int(input("Enter start column: "))

goal_row = int(input("Enter goal row: "))
goal_col = int(input("Enter goal column: "))

start = (start_row, start_col)
goal = (goal_row, goal_col)


path = a_star(grid, start, goal)


if path:

    print("\nPath found:")

    for step in path:
        print(step)

else:

    print("\nNo path exists")