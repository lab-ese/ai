import networkx as nx
import matplotlib.pyplot as plt
#PREDEFINED MAP 
regions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
neighbors = {
    'A': ['B', 'I'],
    'B': ['A', 'C', 'E', 'F', 'I'],
    'C': ['B'],
    'D': ['F'],
    'E': ['B', 'F', 'G'],
    'F': ['B', 'D', 'E', 'H'],
    'G': ['E', 'H'],
    'H': ['F', 'G', 'I'],
    'I': ['A', 'B', 'H']
}
#SAFETY CHECK 
def is_safe(region, color, color_map):
    for neighbor in neighbors[region]:
        if neighbor in color_map and color_map[neighbor] == color:
            return False
    return True
#BACKTRACKING 
def map_coloring(index):
    if index == len(regions):
        return True
    region = regions[index]
    for color in colors:
        if is_safe(region, color, color_map):
            color_map[region] = color
            if map_coloring(index + 1):
                return True
            # Backtrack
            del color_map[region]
    return False
#VISUALIZATION
def visualize_map():
    G = nx.Graph()
    # Add nodes
    for region in regions:
        G.add_node(region)
    # Add edges
    for region in neighbors:
        for neighbor in neighbors[region]:
            G.add_edge(region, neighbor)
    # Node colors
    node_colors = [color_map[r] for r in regions]
    plt.figure()
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=2000,
        font_size=12
    )
    plt.title("Map Coloring Visualization")
    plt.show()
#USER INPUT
n = int(input("Enter number of colors: "))
colors = []
print("Enter color names:")
for i in range(n):
    colors.append(input())
color_map = {}
#RUN 
if map_coloring(0):
    print("\nSolution Found:\n")
    for region in regions:
        print(region, "->", color_map[region])
    visualize_map()
else:
    print("\nNo solution exists")