import heapq
import networkx as nx
import matplotlib.pyplot as plt

class AStar:
    def __init__(self, edges, heuristic_values):
        self.edges = edges
        self.graph = {}
        self.heuristics = heuristic_values
        self.path_found = False

        for start, end, cost in edges:
            if start not in self.graph:
                self.graph[start] = []
            self.graph[start].append((end, cost))

    def find_shortest_path(self, start_node, end_node):
        open_list = [(0, start_node, [])]  # (Total cost, Current node, Path)
        closed_set = set()

        while open_list:
            total_cost, current_node, path = heapq.heappop(open_list)

            if current_node == end_node:
                path.append(current_node)
                return path

            if current_node in closed_set:
                continue

            closed_set.add(current_node)

            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in closed_set:
                    heuristic_cost = self.heuristics[neighbor]
                    new_total_cost = total_cost + cost + heuristic_cost
                    new_path = path + [current_node]
                    heapq.heappush(open_list, (new_total_cost, neighbor, new_path))

        return []

    def visualize_path(self, start_node, end_node):
        path = self.find_shortest_path(start_node, end_node)
        if path:
            print("Shortest Path derived by A* Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

        # Create a directed graph for visualization
        G = nx.DiGraph()
        for start, end, cost in self.edges:
            G.add_edge(start, end, label=cost)  # Add cost as a label to the edge

        # Create a plot for the graph
        pos = nx.spring_layout(G, seed=42)  # You can choose different layout algorithms

        # Draw the graph nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight the A* search path
        for i in range(len(path) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2)

        plt.title("A* Search Path Visualization")

        # Show the plot
        plt.show()

if __name__ == "__main__":
    # Define the edges and heuristic values
    edges = [('S', 'A', 4), ('S', 'B', 2), ('A', 'B', 2), ('B', 'A', 1),
             ('A', 'D', 1), ('D', 'F', 2), ('B', 'C', 3), ('C', 'E', 1), ('F', 'G', 2)]
    heuristic_values = {'S': 7, 'A': 2, 'B': 4, 'C': 6, 'D': 5, 'E': 1, 'F': 2, 'G': 0}

    # Create an AStar object and find the path
    a_star = AStar(edges, heuristic_values)
    a_star.visualize_path('S', 'G')
