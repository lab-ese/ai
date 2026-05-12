from collections import deque

def water_jug_bfs(jug1_cap, jug2_cap, target_x, target_y):
    
    queue = deque()
    queue.append((0, 0))   
    
    visited = set()
    visited.add((0, 0))
    
    parent = {(0, 0): None}
    
    while queue:
        x, y = queue.popleft()   

        # Goal Condition
        if ((target_x == 'n' or x == target_x) and
            (target_y == 'n' or y == target_y)):

            print("\nSolution Found (Using BFS)!\n")

            path = []
            current = (x, y)
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            for step in path:
                print(step)

            print("\nTotal Steps:", len(path) - 1)
            return

        successors = []

        # Fill Jug1
        successors.append((jug1_cap, y))

        # Fill Jug2
        successors.append((x, jug2_cap))

        # Empty Jug1
        successors.append((0, y))

        # Empty Jug2
        successors.append((x, 0))

        # Pour Jug1 → Jug2
        transfer = min(x, jug2_cap - y)
        successors.append((x - transfer, y + transfer))

        # Pour Jug2 → Jug1
        transfer = min(y, jug1_cap - x)
        successors.append((x + transfer, y - transfer))

        for state in successors:
            if state not in visited:
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)

    print("\nNo solution possible.")

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))

tx = input("Enter target for Jug 1 (number or n): ")
ty = input("Enter target for Jug 2 (number or n): ")

target_x = int(tx) if tx != 'n' else 'n'
target_y = int(ty) if ty != 'n' else 'n'

water_jug_bfs(jug1, jug2, target_x, target_y)
