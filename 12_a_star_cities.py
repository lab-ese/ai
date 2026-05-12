import heapq

def a_star_search(graph, heuristics, start, goal):
    pq = [(heuristics[start], 0, start, [])]
    visited = {start: 0}
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal: return path + [current], g
        for neighbor, weight in graph.get(current, []):
            new_g = g + weight
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                heapq.heappush(pq, (new_g + heuristics[neighbor], new_g, neighbor, path + [current]))
    return None, 0

if __name__ == "__main__":
    graph = {'Arad': [('Zerind', 75), ('Sibiu', 140)], 'Zerind': [('Arad', 75), ('Oradea', 71)], 'Oradea': [('Zerind', 71), ('Sibiu', 151)], 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99)], 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)], 'Bucharest': [('Fagaras', 211)]}
    heuristics = {'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Fagaras': 176, 'Bucharest': 0}
    print("--- A* SEARCH: CITIES ---")
    start = input("Enter Start City: ")
    goal = input("Enter Goal City: ")
    path, cost = a_star_search(graph, heuristics, start, goal)
    if path: print(f"Path: {' -> '.join(path)}\nTotal Distance: {cost} km")
    else: print("No path.")
