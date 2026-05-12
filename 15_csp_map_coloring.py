def is_safe(state, color, assignment, neighbors):
    for neighbor in neighbors.get(state, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring_backtracking(states, colors, neighbors, assignment):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment]
    current_state = unassigned[0]

    for color in colors:
        if is_safe(current_state, color, assignment, neighbors):
            assignment[current_state] = color
            result = map_coloring_backtracking(states, colors, neighbors, assignment)
            if result:
                return result
            del assignment[current_state]
    return None

if __name__ == "__main__":
    states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    available_colors = ['Red', 'Green', 'Blue']
    adj_matrix = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    print("--- MAP COLORING (CSP) ---")
    solution = map_coloring_backtracking(states, available_colors, adj_matrix, {})
    if solution:
        for state in states:
            print(f"{state}: {solution[state]}")
    else:
        print("No solution exists.")
