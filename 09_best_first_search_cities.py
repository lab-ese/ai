import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    pq = [(heuristics[start], start, [])]
    visited = set()
    while pq:
        h, current, path = heapq.heappop(pq)
        if current == goal: return path + [current]
        if current in visited: continue
        visited.add(current)
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [current]))
    return None

if __name__ == "__main__":
    graph = {'Arad': [('Zerind', 75), ('Sibiu', 140)], 'Zerind': [('Arad', 75), ('Oradea', 71)], 'Oradea': [('Zerind', 71), ('Sibiu', 151)], 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99)], 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 'Bucharest': [('Fagaras', 211)]}
    heuristics = {'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Fagaras': 176, 'Bucharest': 0}
    print("--- BEST FIRST SEARCH: CITIES ---")
    start = input("Enter Start City: ")
    goal = input("Enter Goal City: ")
    path = greedy_best_first_search(graph, heuristics, start, goal)
    if path: print("Path:", " -> ".join(path))
    else: print("City not found or no path.")
