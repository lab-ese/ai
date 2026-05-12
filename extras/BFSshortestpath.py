import heapq

graph = {
    "Hyderabad": {
        "Bangalore": 500,
        "Mumbai": 600,
        "Nagpur": 800,
        "Kolkata": 1500
    },
    "Nagpur": {
        "Indore": 800,
        "Kolkata": 1200
    },
    "Mumbai": {
        "Indore": 600
    },
    "Indore": {
        "Delhi": 800
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

# Updated heuristic (depends on goal)
def calculate_heuristic(city, goal):
    if city == goal:
        return 0
    if len(graph[city]) == 0:
        return float('inf')
    return min(graph[city].values())

def best_first_search(start, goal):
    visited = set()
    pq = []

    heapq.heappush(pq, (calculate_heuristic(start, goal), start))
    path = []

    while pq:
        h, node = heapq.heappop(pq)

        if node not in visited:
            print("Visiting:", node,
                  "| Heuristic:", calculate_heuristic(node, goal))

            visited.add(node)
            path.append(node)

            if node == goal:
                print("\nGoal Reached!")
                return path

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        pq,
                        (calculate_heuristic(neighbor, goal), neighbor)
                    )

    return None


# Input
start = input("Enter start city: ")
goal = input("Enter goal city: ")

# Run search
result = best_first_search(start, goal)

# Output
print("\nPath taken:")
if result:
    print(" -> ".join(result))
else:
    print("No path found")