"""
Map Coloring — CSP with Backtracking (Australia Map)

Run (Windows):
    python mapcoloring.py
"""


REGIONS = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

ADJACENCIES = [
    ("WA", "NT"), ("WA", "SA"),
    ("NT", "SA"), ("NT", "Q"),
    ("SA", "Q"), ("SA", "NSW"), ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V"),
]

COLORS = ["Red", "Green", "Blue"]


def get_neighbors():
    nb = {r: set() for r in REGIONS}
    for r1, r2 in ADJACENCIES:
        nb[r1].add(r2)
        nb[r2].add(r1)
    return nb


def is_consistent(region, color, assignment, neighbors):
    for nb in neighbors[region]:
        if nb in assignment and assignment[nb] == color:
            return False
    return True


def backtrack(assignment, neighbors, stats):
    if len(assignment) == len(REGIONS):
        return dict(assignment)

    unassigned = [r for r in REGIONS if r not in assignment]
    # MRV: pick variable with fewest legal colors remaining
    def remaining(r):
        return sum(1 for c in COLORS if is_consistent(r, c, assignment, neighbors))
    var = min(unassigned, key=remaining)

    for color in COLORS:
        stats["tries"] += 1
        if is_consistent(var, color, assignment, neighbors):
            assignment[var] = color
            result = backtrack(assignment, neighbors, stats)
            if result:
                return result
            del assignment[var]
            stats["backtracks"] += 1
    return None


def verify(assignment):
    for r1, r2 in ADJACENCIES:
        if assignment[r1] == assignment[r2]:
            return False, (r1, r2)
    return True, None


def main():
    print("=" * 40)
    print("  MAP COLORING — CSP (Australia)")
    print("=" * 40)
    print(f"Regions      : {', '.join(REGIONS)}")
    print(f"Adjacencies  : {len(ADJACENCIES)}")
    print(f"Colors       : {', '.join(COLORS)}\n")

    neighbors = get_neighbors()
    stats = {"tries": 0, "backtracks": 0}
    solution = backtrack({}, neighbors, stats)

    if solution is None:
        print("No valid coloring exists.")
        return

    print("Coloring assignment:")
    for r in REGIONS:
        print(f"  {r:<4} = {solution[r]}")

    ok, conflict = verify(solution)
    print(f"\nValid: {'YES' if ok else 'NO'}")
    if not ok:
        print(f"Conflict: {conflict}")

    print(f"\nAttempts: {stats['tries']}  |  Backtracks: {stats['backtracks']}")


if __name__ == "__main__":
    main()
