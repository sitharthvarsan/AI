import networkx as nx
import matplotlib.pyplot as plt

class BritishMuseumSearch:
    def __init__(self, edges_bms):
        self.edges = edges_bms
        self.graph_dict = {}
        for i, j in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)

    def find_all_paths_bms(self, start_node, end_node, current_path=[]):
        all_paths = []
        current_path = current_path + [start_node]

        if start_node == end_node:
            return [current_path]

        if start_node not in self.graph_dict:
            return []

        sorted_neighbors = sorted(self.graph_dict[start_node])

        for neighbor in sorted_neighbors:
            if neighbor not in current_path:
                new_paths = self.find_all_paths_bms(neighbor, end_node, current_path)
                for path in new_paths:
                    all_paths.append(path)

        return all_paths

    def visualize_paths_bms(self, start_node, end_node):
        paths = self.find_all_paths_bms(start_node, end_node)
        if not paths:
            print("No valid path found.")
            return

        # Create a directed graph
        G = nx.DiGraph()

        for edge in self.edges:
            G.add_edge(edge[0], edge[1])

        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(10, 6))

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')

        # Draw the paths
        for path in paths:
            edge_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2)

        plt.title("British Museum Search Algorithm Visualization")

        plt.show()

edges_bms = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]
bms = BritishMuseumSearch(edges_bms)
bms.visualize_paths_bms('S', 'G')
