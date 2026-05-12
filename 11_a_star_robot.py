import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_robot(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [(heuristic(start, goal), 0, start, [])]
    visited = {start: 0}
    while pq:
        f, g, (r, c), path = heapq.heappop(pq)
        if (r, c) == goal: return path + [(r, c)]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g = g + 1
                if (nr, nc) not in visited or new_g < visited[(nr, nc)]:
                    visited[(nr, nc)] = new_g
                    heapq.heappush(pq, (new_g + heuristic((nr, nc), goal), new_g, (nr, nc), path + [(r, c)]))
    return None

if __name__ == "__main__":
    grid = [[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,1,0,0,0],[0,0,0,0,0]]
    print("--- A* ALGORITHM: ROBOT ---")
    try:
        sr = int(input("Start Row (0-4): ")); sc = int(input("Start Col (0-4): "))
        gr = int(input("Goal Row (0-4): ")); gc = int(input("Goal Col (0-4): "))
        path = a_star_robot(grid, (sr, sc), (gr, gc))
        if path:
            print("Path found:", path)
            for r in range(5):
                for c in range(5):
                    if (r, c) == (sr, sc): print("S", end=" ")
                    elif (r, c) == (gr, gc): print("G", end=" ")
                    elif (r, c) in path: print("*", end=" ")
                    elif grid[r][c] == 1: print("#", end=" ")
                    else: print(".", end=" ")
                print()
        else: print("No path.")
    except: print("Invalid Input.")
