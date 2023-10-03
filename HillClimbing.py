import networkx as nx
import matplotlib.pyplot as plt

class HillClimbingSearch:
    def __init__(self, edges):
        self.graph = {}
        self.heuristics = {}
        for start, end in edges:
            self.graph.setdefault(start, []).append(end)
            self.heuristics.setdefault(start, 0)
            self.heuristics.setdefault(end, 0)

    def get_heuristics_from_user(self):
        for node in self.heuristics:
            self.heuristics[node] = int(input(f'Enter the Heuristic value for {node}: '))

    def hill_climbing_search(self, current, goal, path=[]):
        path.append(current)
        if current == goal:
            return path
        if current not in self.graph:
            return []

        neighbors = self.graph[current]
        neighbors.sort(key=lambda node: self.heuristics[node])
        for neighbor in neighbors:
            if neighbor not in path:
                new_path = self.hill_climbing_search(neighbor, goal, path.copy())
                if new_path:
                    return new_path

    def visualize_path_hill_climbing(self, start, end):
        path = self.hill_climbing_search(start, end)
        if path:
            print("Path derived by Hill Climbing Search Algorithm:")
            print(" -> ".join(path))

            # Create a directed graph
            G = nx.DiGraph()
            for edge in self.graph:
                for neighbor in self.graph[edge]:
                    G.add_edge(edge, neighbor)

            pos = nx.spring_layout(G, seed=42)

            plt.figure(figsize=(10, 6))

            # Draw nodes and edges
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')

            # Highlight the path
            for i in range(len(path) - 1):
                edge = (path[i], path[i + 1])
                nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='red', width=2)

            plt.title("Hill Climbing Search Algorithm Visualization")

            plt.show()
        else:
            print("No valid path found.")

# Define the edges with updated values
edges = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]

hill_climbing_search = HillClimbingSearch(edges)
hill_climbing_search.get_heuristics_from_user()
hill_climbing_search.visualize_path_hill_climbing('S', 'G')
