import copy

def get_manhattan_distance(state, goal):
    distance = 0
    goal_pos = {}
    for r in range(3):
        for c in range(3):
            goal_pos[goal[r][c]] = (r, c)
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0: 
                tr, tc = goal_pos[val]
                distance += abs(r - tr) + abs(c - tc)
    return distance

def get_neighbors(state):
    neighbors = []
    r, c = 0, 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                r, c = i, j
                break
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append(new_state)
    return neighbors

def hill_climbing(initial, goal):
    current = initial
    current_h = get_manhattan_distance(current, goal)
    steps = [(current, current_h)]
    while True:
        neighbors = get_neighbors(current)
        best_neighbor, best_h = None, current_h
        for neighbor in neighbors:
            h = get_manhattan_distance(neighbor, goal)
            if h < best_h:
                best_h, best_neighbor = h, neighbor
        if best_neighbor is None: break
        current, current_h = best_neighbor, best_h
        steps.append((current, current_h))
    return steps

def print_puzzle(state):
    for row in state: print(f" {row[0]} {row[1]} {row[2]} ")

def get_input():
    print("Enter Puzzle (3x3) row by row (0 for blank):")
    return [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]

if __name__ == "__main__":
    print("--- HILL CLIMBING: 8-PUZZLE ---")
    start = get_input()
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] # Default Goal
    path = hill_climbing(start, goal)
    for i, (state, h) in enumerate(path):
        print(f"Step {i} (H: {h}):"); print_puzzle(state); print("-" * 10)
    print("Goal Reached!" if path[-1][1] == 0 else "Stuck in Local Optimum.")
