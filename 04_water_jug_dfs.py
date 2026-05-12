import math

def solve_water_jug_dfs(j1_cap, j2_cap, target):
    # (jug1, jug2)
    initial_state = (0, 0)
    
    # Check if target is possible
    if target > max(j1_cap, j2_cap) or target % math.gcd(j1_cap, j2_cap) != 0:
        return None

    # Stack for DFS: stores (current_state, path_taken)
    stack = [(initial_state, [initial_state])]
    visited = set()

    while stack:
        (c1, c2), path = stack.pop()

        if (c1, c2) in visited:
            continue
        visited.add((c1, c2))

        # Goal State check
        if c1 == target or c2 == target:
            return path

        # Generate Possible Rules/Actions
        rules = [
            (j1_cap, c2),           # Rule 1: Fill Jug 1
            (c1, j2_cap),           # Rule 2: Fill Jug 2
            (0, c2),                # Rule 3: Empty Jug 1
            (c1, 0),                # Rule 4: Empty Jug 2
            # Rule 5: Pour Jug 1 -> Jug 2
            (c1 - min(c1, j2_cap - c2), c2 + min(c1, j2_cap - c2)),
            # Rule 6: Pour Jug 2 -> Jug 1
            (c1 + min(c2, j1_cap - c1), c2 - min(c2, j1_cap - c1))
        ]

        for next_state in rules:
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))

    return None

if __name__ == "__main__":
    print("--- WATER JUG PROBLEM (DFS) ---")
    try:
        cap1 = int(input("Enter capacity of Jug 1: "))
        cap2 = int(input("Enter capacity of Jug 2: "))
        goal = int(input("Enter target volume: "))

        result_path = solve_water_jug_dfs(cap1, cap2, goal)

        if result_path:
            print(f"\nSolution found with {len(result_path)-1} steps:")
            for i, (s1, s2) in enumerate(result_path):
                print(f"Step {i}: ({s1}, {s2})")
        else:
            print("\nNo solution exists for the given capacities and target.")
    except ValueError:
        print("Invalid input! Please enter integers.")
