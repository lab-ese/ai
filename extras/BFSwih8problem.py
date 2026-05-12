import heapq
import copy

# Goal State
GOAL = [[1,2,3],
        [8,0,4],
        [7,6,5]]

# Objective Function 
def objective_function(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == GOAL[i][j] and state[i][j] != 0:
                count += 1
    return count


# Find blank 
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate neighbors 
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


# Best First Search 
def best_first_search(start):

    visited = set()
    pq = []

    # Convert to tuple for hashing
    start_tuple = tuple(tuple(row) for row in start)

    # Use NEGATIVE because heapq is min-heap (we want max objective)
    heapq.heappush(pq, (-objective_function(start), start_tuple))

    print("\nInitial State:")
    for row in start:
        print(row)
    print("Initial Objective Value =", objective_function(start))

    while pq:

        neg_value, state = heapq.heappop(pq)
        current_value = -neg_value

        # Convert tuple back to list
        state_list = [list(row) for row in state]

        if state in visited:
            continue

        visited.add(state)

        print("\nCurrent State:")
        for row in state_list:
            print(row)
        print("Objective Value =", current_value)

        # Goal check
        if current_value == 8:
            print("\nGoal Reached!")
            return state_list

        neighbors = generate_neighbors(state_list)

        for n in neighbors:
            n_tuple = tuple(tuple(row) for row in n)
            if n_tuple not in visited:
                heapq.heappush(pq, (-objective_function(n), n_tuple))


# -------- INPUT --------

print("Enter initial 8 puzzle configuration (0 for blank):")
start = []
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

result = best_first_search(start)

print("\nFinal State:")
for row in result:
    print(row)