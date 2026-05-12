import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search_robot(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [(heuristic(start, goal), start, [])]
    visited = set()
    while pq:
        h, (r, c), path = heapq.heappop(pq)
        if (r, c) == goal: return path + [(r, c)]
        if (r, c) in visited: continue
        visited.add((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    heapq.heappush(pq, (heuristic((nr, nc), goal), (nr, nc), path + [(r, c)]))
    return None

if __name__ == "__main__":
    grid = [[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,1,0,0,0],[0,0,0,0,0]]
    print("--- BEST FIRST SEARCH: ROBOT ---")
    try:
        sr = int(input("Start Row (0-4): ")); sc = int(input("Start Col (0-4): "))
        gr = int(input("Goal Row (0-4): ")); gc = int(input("Goal Col (0-4): "))
        path = best_first_search_robot(grid, (sr, sc), (gr, gc))
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
