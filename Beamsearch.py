import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Priority queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

class BeamSearch:
    def __init__(self, edges_with_cost):
        self.graph_dict = defaultdict(list)
        for start, end, cost in edges_with_cost:
            self.graph_dict[start].append((end, cost))

    def perform_beam_search(self, start_node, end_node, beam_width=1):
        beam = PriorityQueue()
        beam.push(0, [start_node])

        G = nx.Graph()
        for start, end, cost in edges_with_cost:
            G.add_edge(start, end, weight=cost)

        pos = nx.spring_layout(G, seed=42)  # You can choose different layout algorithms

        while not beam.is_empty():
            total_cost, path = beam.pop()

            current_node = path[-1]

            if current_node == end_node:
                return path

            if current_node in self.graph_dict:
                neighbors = self.graph_dict[current_node]
                neighbors.sort(key=lambda x: x[1])
                for neighbor, edge_cost in neighbors[:beam_width]:
                    new_path = path + [neighbor]
                    new_total_cost = total_cost + edge_cost
                    beam.push(new_total_cost, new_path)

        return []

    def visualize_path(self, start_node, end_node, beam_width=1):
        path = self.perform_beam_search(start_node, end_node, beam_width)
        if path:
            print("Path derived by Beam Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")
        
        # Create a plot for the graph
        G = nx.Graph()
        for start, end, cost in edges_with_cost:
            G.add_edge(start, end, weight=cost)

        pos = nx.spring_layout(G, seed=42)  # You can choose different layout algorithms

        # Draw the graph nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight the Beam Search path
        for i in range(len(path) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2)

        plt.title("Beam Search Path Visualization")

        # Show the plot
        plt.show()

if __name__ == "__main__":
    # Define the edges with updated values
    edges_with_cost = [('S', 'B', 4), ('S', 'A', 5), ('A', 'B', 3), ('B', 'A', 3),
                       ('A', 'D', 4), ('D', 'F', 3), ('B', 'C', 4), ('C', 'E', 6), ('F', 'G', 1)]

    beam_search = BeamSearch(edges_with_cost)
    beam_search.visualize_path('S', 'G', beam_width=2)
