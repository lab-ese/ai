"""
Crossword Puzzle — CSP with Backtracking

Run (Windows):
    python crossword.py
"""


# 5x5 crossword skeleton — '.' = letter cell, '#' = blocked
GRID_TEMPLATE = [
    [".", "#", ".", "#", "."],
    [".", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", ".", "#", "."],
    [".", "#", ".", "#", "."],
]


# Slot defs: (name, row, col, length, direction)
SLOTS = [
    ("1A", 2, 0, 5, "across"),
    ("1D", 0, 0, 5, "down"),
    ("2D", 0, 2, 5, "down"),
    ("3D", 0, 4, 5, "down"),
]


WORD_LIST = [
    "HEART", "HACKS", "ERNES", "TYING", "STING",
    "TABLE", "ANGEL", "BREAD", "STORY", "GREEN",
    "BRAVE", "PLANT", "CRANE", "GLASS", "BRAIN",
    "STEEL", "OCEAN", "MOUTH", "RIVER", "STORM",
]


def slot_cells(slot):
    name, r, c, length, direction = slot
    if direction == "across":
        return [(r, c + i) for i in range(length)]
    return [(r + i, c) for i in range(length)]


def overlaps(slot1, slot2):
    cells1 = slot_cells(slot1)
    cells2 = slot_cells(slot2)
    for p1, cell1 in enumerate(cells1):
        for p2, cell2 in enumerate(cells2):
            if cell1 == cell2:
                return p1, p2
    return None


def is_consistent(slot, word, assignment):
    for other_name, other_word in assignment.items():
        other_slot = next(s for s in SLOTS if s[0] == other_name)
        ov = overlaps(slot, other_slot)
        if ov:
            p1, p2 = ov
            if word[p1] != other_word[p2]:
                return False
    return True


def backtrack(assignment, slots_left, stats):
    if not slots_left:
        return dict(assignment)
    slot = slots_left[0]
    rest = slots_left[1:]
    for word in WORD_LIST:
        if word in assignment.values():
            continue
        if len(word) != slot[3]:
            continue
        stats["tries"] += 1
        if is_consistent(slot, word, assignment):
            assignment[slot[0]] = word
            result = backtrack(assignment, rest, stats)
            if result:
                return result
            del assignment[slot[0]]
            stats["backtracks"] += 1
    return None


def print_grid(assignment):
    grid = [row[:] for row in GRID_TEMPLATE]
    for slot in SLOTS:
        word = assignment.get(slot[0], "")
        for i, (r, c) in enumerate(slot_cells(slot)):
            if i < len(word):
                grid[r][c] = word[i]

    for row in grid:
        print(" ".join(cell if cell != "#" else "#" for cell in row))


def main():
    print("=" * 40)
    print("  CROSSWORD PUZZLE — CSP")
    print("=" * 40)
    print("Grid (5x5) with 4 slots: 1A, 1D, 2D, 3D\n")

    print("Empty grid:")
    for row in GRID_TEMPLATE:
        print(" ".join(row))

    stats = {"tries": 0, "backtracks": 0}
    solution = backtrack({}, SLOTS, stats)

    if solution is None:
        print("\nNo solution found.")
        return

    print("\nSolution found!\n")
    for name, word in solution.items():
        print(f"  {name} = {word}")

    print("\nFilled grid:")
    print_grid(solution)
    print(f"\nAttempts: {stats['tries']}  |  Backtracks: {stats['backtracks']}")


if __name__ == "__main__":
    main()
