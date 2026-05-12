import heapq

# Goal State
GOAL = ((1,2,3),
        (8,0,4),
        (7,6,5))


# Heuristic: misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                count += 1
    return count


# Find blank
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate neighbors (no deepcopy)
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            
            temp = [list(row) for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]

            neighbors.append(tuple(tuple(row) for row in temp))

    return neighbors


# Print state
def print_state(state):
    for row in state:
        print(list(row))
    print()


# Print path
def print_path(parent_map, final_state):
    path = []
    state = final_state

    while state is not None:
        path.append(state)
        state = parent_map[state]

    path.reverse()

    print("\nSolution Path:")
    for step in path:
        print_state(step)


# A* Algorithm
def a_star(start):

    visited = set()
    parent_map = {}
    pq = []

    start = tuple(tuple(row) for row in start)

    parent_map[start] = None

    g_start = 0
    h_start = heuristic(start)
    f_start = g_start + h_start

    heapq.heappush(pq, (f_start, g_start, start))

    print("\nInitial State:")
    print_state(start)
    print("f(n) =", f_start, "g(n) =", g_start, "h(n) =", h_start)

    while pq:

        f, g, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        print("\nCurrent State:")
        print_state(current)
        print("f(n) =", f, "g(n) =", g, "h(n) =", heuristic(current))

        if current == GOAL:
            print("\nGoal Reached!")
            print_path(parent_map, current)
            return current

        for neighbor in generate_neighbors(current):

            if neighbor not in visited:

                g_new = g + 1
                h_new = heuristic(neighbor)
                f_new = g_new + h_new

                heapq.heappush(pq, (f_new, g_new, neighbor))

                if neighbor not in parent_map:
                    parent_map[neighbor] = current

    print("No solution found.")


# -------- INPUT --------

print("Enter initial 8 puzzle configuration (0 for blank):")

start = [list(map(int, input().split())) for _ in range(3)]

a_star(start)