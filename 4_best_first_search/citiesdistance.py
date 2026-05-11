"""
Cities Distance — Greedy Best First Search (Romania Map)

Run (Windows):
    python citiesdistance.py
"""

import heapq


# Romania road map (city -> [(neighbor, distance), ...])
EDGES = {
    "Arad":      [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind":    [("Arad", 75), ("Oradea", 71)],
    "Oradea":    [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu":     [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj":     [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia":   [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta":   [("Mehadia", 75), ("Craiova", 120)],
    "Craiova":   [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras":   [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti":   [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu":   [("Bucharest", 90)],
    "Urziceni":  [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova":   [("Urziceni", 98), ("Eforie", 86)],
    "Eforie":    [("Hirsova", 86)],
    "Vaslui":    [("Urziceni", 142), ("Iasi", 92)],
    "Iasi":      [("Vaslui", 92), ("Neamt", 87)],
    "Neamt":     [("Iasi", 87)],
}

# Straight-Line Distance to Bucharest (heuristic)
SLD_BUCHAREST = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242,
    "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193, "Sibiu": 253,
    "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374,
}


def best_first_search(start, goal):
    counter = 0
    heap = [(SLD_BUCHAREST[start], counter, start, [start], 0)]
    visited = set()
    trace = []

    while heap:
        h, _, city, path, cost = heapq.heappop(heap)
        if city in visited:
            continue
        visited.add(city)
        trace.append((city, h, cost))

        if city == goal:
            return path, cost, trace

        for nb, dist in EDGES.get(city, []):
            if nb not in visited:
                counter += 1
                heapq.heappush(heap, (SLD_BUCHAREST.get(nb, 999), counter,
                                        nb, path + [nb], cost + dist))

    return None, 0, trace


def main():
    print("=" * 40)
    print("  CITIES DISTANCE — BEST FIRST SEARCH")
    print("        (Romania Map)")
    print("=" * 40)

    print("\nAvailable cities:")
    print(", ".join(sorted(EDGES.keys())))

    start = input("\nStart city (default: Arad): ").strip() or "Arad"
    goal  = input("Goal city  (default: Bucharest): ").strip() or "Bucharest"

    if start not in EDGES or goal not in EDGES:
        print("Invalid city.")
        return

    path, cost, trace = best_first_search(start, goal)
    if path is None:
        print("No path found.")
        return

    print(f"\nPath  : {' -> '.join(path)}")
    print(f"Cost  : {cost} km")
    print(f"Cities expanded: {len(trace)}\n")

    print("Expansion trace (city | h=SLD | g=cost-so-far):")
    print("-" * 50)
    for city, h, g in trace:
        print(f"  {city:<18} h={h:<5} g={g}")


if __name__ == "__main__":
    main()
