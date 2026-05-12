from collections import deque
import math

def solve_water_jug_bfs(j1_cap, j2_cap, target):
    # Check if target is possible
    if target > max(j1_cap, j2_cap) or target % math.gcd(j1_cap, j2_cap) != 0:
        return None

    # Initial state: (0, 0)
    initial_state = (0, 0)
    queue = deque([(initial_state, [initial_state])])
    visited = {initial_state}

    while queue:
        (c1, c2), path = queue.popleft()

        # Goal State check
        if c1 == target or c2 == target:
            return path

        # Generate Possible Rules/Actions
        rules = [
            (j1_cap, c2),           # Fill Jug 1
            (c1, j2_cap),           # Fill Jug 2
            (0, c2),                # Empty Jug 1
            (c1, 0),                # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (c1 - min(c1, j2_cap - c2), c2 + min(c1, j2_cap - c2)),
            # Pour Jug 2 -> Jug 1
            (c1 + min(c2, j1_cap - c1), c2 - min(c2, j1_cap - c1))
        ]

        for next_state in rules:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None

if __name__ == "__main__":
    print("--- WATER JUG PROBLEM (BFS - Shortest Path) ---")
    try:
        cap1 = int(input("Enter capacity of Jug 1: "))
        cap2 = int(input("Enter capacity of Jug 2: "))
        goal = int(input("Enter target volume: "))

        result_path = solve_water_jug_bfs(cap1, cap2, goal)

        if result_path:
            print(f"\nShortest solution found with {len(result_path)-1} steps:")
            for i, (s1, s2) in enumerate(result_path):
                print(f"Step {i}: Jug1={s1}L, Jug2={s2}L")
        else:
            print("\nNo solution exists for the given capacities and target.")
    except ValueError:
        print("Invalid input! Please enter integers.")
