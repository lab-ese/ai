import heapq

def get_manhattan_distance(state, goal):
    distance = 0
    goal_map = {val: (r, c) for r, row in enumerate(goal) for c, val in enumerate(row)}
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                tr, tc = goal_map[val]
                distance += abs(r - tr) + abs(c - tc)
    return distance

def get_neighbors(state):
    neighbors = []
    r, c = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0: r, c = i, j; break
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [list(row) for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def a_star_8_puzzle(initial, goal):
    start_node = tuple(tuple(row) for row in initial)
    goal_node = tuple(tuple(row) for row in goal)
    pq = [(get_manhattan_distance(initial, goal), 0, start_node, [])]
    visited = {start_node: 0}
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal_node: return path + [current]
        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                h = get_manhattan_distance(neighbor, goal)
                heapq.heappush(pq, (new_g + h, new_g, neighbor, path + [current]))
    return None

def get_input():
    print("Enter Puzzle (3x3) row by row (0 for blank):")
    return [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]

if __name__ == "__main__":
    print("--- A* SEARCH: 8-PUZZLE ---")
    start = get_input()
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    solution = a_star_8_puzzle(start, goal)
    if solution:
        for i, step in enumerate(solution):
            print(f"Step {i}:")
            for row in step: print(f" {row[0]} {row[1]} {row[2]} ")
            print("-" * 10)
    else: print("No solution.")
