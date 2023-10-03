import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class BreadthFirstSearch:
    def __init__(self, edges_bfs):
        self.graph = defaultdict(list)
        for start, end in edges_bfs:
            self.graph[start].append(end)

    def find_shortest_path_bfs(self, start_node, end_node):
        visited = set()
        queue = [[start_node]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end_node:
                return path

            if node not in visited:
                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                visited.add(node)

        return []

    def visualize_path_bfs(self, start_node, end_node):
        path = self.find_shortest_path_bfs(start_node, end_node)
        if path:
            print("Shortest Path derived by Breadth-First Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")
        
        # Create a plot for the graph
        G = nx.Graph()
        for start, end in edges_bfs:
            G.add_edge(start, end)

        pos = nx.spring_layout(G, seed=42)  # You can choose different layout algorithms

        # Draw the graph nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')

        # Highlight the BFS path
        if path:
            edge_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2)

        plt.title("Breadth-First Search Path Visualization")

        # Show the plot
        plt.show()

# Define the edges for BFS
edges_bfs = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]

# Create a BreadthFirstSearch object and find the path
bfs = BreadthFirstSearch(edges_bfs)
bfs.visualize_path_bfs('S', 'G')
