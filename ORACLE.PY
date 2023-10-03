import networkx as nx
import matplotlib.pyplot as plt

class PathOracle:
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end, cost in edges:
            self.graph_dict.setdefault(start, []).append((end, cost))

    def find_all_paths_with_cost(self, start, end, current_path=[], cost=0):
        current_path = current_path + [start]
        if start == end:
            return [(cost, current_path)]

        if start not in self.graph_dict:
            return []

        paths = []
        for neighbor, edge_cost in self.graph_dict[start]:
            if neighbor not in current_path:
                new_paths = self.find_all_paths_with_cost(neighbor, end, current_path.copy(), cost + edge_cost)
                paths.extend(new_paths)

        return paths

    def visualize_ranked_paths(self, start_node, end_node, show_oracle_value=False):
        paths = self.find_all_paths_with_cost(start_node, end_node)

        if not paths:
            print("No valid path found.")
            return

        paths.sort(key=lambda x: x[0])

        print("Paths ranked from best to worst based on cost:")
        oracle = paths[0]
        print("Oracle:", oracle[0] if show_oracle_value else "Hidden")  # Show oracle value on request

        # Create a directed graph
        G = nx.DiGraph()

        for edge in self.graph_dict:
            for neighbor, cost in self.graph_dict[edge]:
                G.add_edge(edge, neighbor, weight=cost)

        pos = nx.spring_layout(G, seed=42)
        edge_labels = {}
        for edge in G.edges(data=True):
            source, target, data = edge
            edge_labels[(source, target)] = data['weight']

        plt.figure(figsize=(10, 6))

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        # Extract edges from the best path
        best_path = paths[0][1]
        edge_list = [(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2)

        plt.title("Path Oracle Algorithm Visualization")

        plt.show()

# Define the edges with updated values
edges_with_cost = [('S', 'B', 4), ('S', 'A', 3), ('A', 'B', 2), ('B', 'A', 3),
                   ('A', 'D', 5), ('D', 'F', 4), ('B', 'C', 2), ('C', 'E', 4), ('F', 'G', 2)]

path_oracle = PathOracle(edges_with_cost)
path_oracle.visualize_ranked_paths('S', 'G', show_oracle_value=True)
