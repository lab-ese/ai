import heapq

graph = {
    "Hyderabad": {
        "Bangalore": 500,
        "Mumbai": 800,
        "Nagpur": 500,
        "Kolkata": 1500
    },
    "Mumbai": {
        "Indore": 600,
        "Hyderabad": 800
    },
    "Nagpur": {
        "Indore": 800,
        "Kolkata": 1200,
        "Hyderabad": 500
    },
    "Indore": {
        "Delhi": 800,
        "Mumbai": 600,
        "Nagpur": 800
    },
    "Bangalore": {
        "Hyderabad": 500
    },
    "Kolkata": {
        "Hyderabad": 1500,
        "Nagpur": 1200
    },
    "Delhi": {
        "Indore": 800
    }
}

def heuristic(city, goal):
    if city == goal:
        return 0
    if len(graph[city]) == 0:
        return float('inf')
    return min(graph[city].values())

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    g_cost = {city: float('inf') for city in graph}
    g_cost[start] = 0
    parent = {}
    visited = set()
    while pq:
        f, current = heapq.heappop(pq)
        if current in visited:
            continue
        print("Visiting:", current)
        visited.add(current)
        if current == goal:
            break
        for neighbor, distance in graph[current].items():
            new_cost = g_cost[current] + distance
            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic(neighbor, goal)
                heapq.heappush(
                    pq,
                    (f_cost, neighbor)
                )
                parent[neighbor] = current
    path = []
    node = goal
    if node not in parent and node != start:
        return None, None
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()
    return path, g_cost[goal]

start = input("Enter start city: ")
goal = input("Enter goal city: ")
path, cost = a_star(start, goal)
if path:
    print("\nShortest Path:")
    print(" -> ".join(path))
    print("Total Distance:", cost)
else:
    print("No path found")