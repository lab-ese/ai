"""
Water Jug Problem — Breadth First Search (BFS)

Run (Windows):
    python bfs.py
"""

from collections import deque


def get_successors(state, jug_a, jug_b):
    a, b = state
    return [
        (jug_a, b),                                   # Fill A
        (a, jug_b),                                   # Fill B
        (0, b),                                       # Empty A
        (a, 0),                                       # Empty B
        (max(0, a - (jug_b - b)), min(jug_b, a + b)), # Pour A -> B
        (min(jug_a, a + b), max(0, b - (jug_a - a))), # Pour B -> A
    ]


def bfs(jug_a, jug_b, goal):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        a, b = state
        if a == goal or b == goal:
            return path
        for nxt in get_successors(state, jug_a, jug_b):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None


def main():
    print("=" * 30)
    print("  WATER JUG PROBLEM — BFS")
    print("=" * 30)
    jug_a = int(input("Capacity of Jug A: "))
    jug_b = int(input("Capacity of Jug B: "))
    goal  = int(input("Goal amount: "))

    path = bfs(jug_a, jug_b, goal)
    if path is None:
        print("\nNo solution exists.")
        return

    print(f"\nSolution found in {len(path) - 1} steps:\n")
    print(f"{'Step':<6}{'Jug A':<8}{'Jug B':<8}")
    print("-" * 22)
    for i, (a, b) in enumerate(path):
        print(f"{i:<6}{a:<8}{b:<8}")


if __name__ == "__main__":
    main()
