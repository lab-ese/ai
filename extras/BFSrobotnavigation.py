import heapq

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic: Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # Priority queue (min-heap)
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start[0], start[1], []))

    visited = set()
    visited.add(start)

    while pq:
        h, r, c, path = heapq.heappop(pq)

        # Goal check
        if (r, c) == goal:
            return path + [(r, c)]

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 0 and (nr, nc) not in visited):

                new_path = path + [(r, c)]
                new_h = heuristic((nr, nc), goal)

                heapq.heappush(pq, (new_h, nr, nc, new_path))
                visited.add((nr, nc))

    return None


# -------- USER INPUT --------
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

# -------- RUN SEARCH --------
path = best_first_search(grid, start, goal)

# -------- OUTPUT --------
if path:
    print("\nPath found:")
    for step in path:
        print(step)
else:
    print("\nNo path exists")