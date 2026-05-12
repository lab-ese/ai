import copy
# Goal State
GOAL = [[1,2,3],
        [4,5,6],
        [7,8,0]]


# Objective Function (heuristic function)
def objective_function(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == GOAL[i][j] and state[i][j] != 0:
                count += 1
    return count


# Find blank position
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


# Hill Climbing
def hill_climbing(start):
    current = start
    current_value = objective_function(current)
    print("\nInitial State:")
    for row in current:
        print(row)
    print("Initial Objective Value =", current_value)
    while True:
        neighbors = generate_neighbors(current)
        best_neighbor = None
        best_value = -1
        for n in neighbors:
            value = objective_function(n)
            if value > best_value:
                best_value = value
                best_neighbor = n
        # Stop condition
        if best_value <= current_value:
            print("\nStopped (Local Maximum / Plateau / Ridge)")
            return current
        # Move to better state
        current = best_neighbor
        current_value = best_value
        print("\nCurrent State:")
        for row in current:
            print(row)
        print("Objective Value =", current_value)
        if current_value == 8:
            print("\nGoal Reached!")
            return current

# MAIN FUNCTION
print("Enter the initial 8 puzzle configuration (0 for blank):")
start = []
for i in range(3):
    row = list(map(int,input().split()))
    start.append(row)

result = hill_climbing(start)

print("\nFinal State:")
for row in result:
    print(row)
