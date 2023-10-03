import networkx as nx
import matplotlib.pyplot as plt

class BranchAndBound:
    def __init__(self, edges_with_cost, oracle_value):
        self.edges = edges_with_cost
        self.graph_dict = {}
        self.oracle = oracle_value
        self.best_path = None
        for start, end, cost in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = []
            self.graph_dict[start].append((end, cost))
    
    def find_optimal_path_bnb(self, start, end, path=[], cost=0):
        path = path + [start]
        if start == end:
            if (self.oracle[0] is None) or (cost == self.oracle[0]):
                self.oracle[0] = cost
                if self.best_path is None or cost < self.best_path[0]:
                    self.best_path = (cost, path.copy())
            return
        if start not in self.graph_dict:
            return
        for neighbor, edge_cost in self.graph_dict[start]:
            if neighbor not in path:
                self.find_optimal_path_bnb(neighbor, end, path, cost + edge_cost)
    
    def visualize_optimal_path_bnb(self, start, end):
        self.find_optimal_path_bnb(start, end)
        if self.best_path is not None:
            cost, path = self.best_path
            path.pop(0)
            print("Optimal Path derived by Branch And Bound Algorithm:")
            print(" -> ".join(path))
            
            # Create a directed graph
            G = nx.DiGraph()

            for edge in self.edges:
                G.add_edge(edge[0], edge[1], weight=edge[2])

            pos = nx.spring_layout(G, seed=42)

            plt.figure(figsize=(10, 6))

            # Draw nodes and edges
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')

            # Draw the optimal path
            edge_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
            edge_labels = {(edge[0], edge[1]): G.get_edge_data(edge[0], edge[1])['weight'] for edge in edge_list}
            nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=2)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

            plt.title("Branch and Bound Algorithm Visualization")

            plt.show()
        else:
            print("No valid path found.")

# Define the edges with updated values
edges_with_cost = [('S', 'B', 4), ('S', 'A', 3), ('A', 'B', 2), ('B', 'A', 3),
                   ('A', 'D', 5), ('D', 'F', 4), ('B', 'C', 2), ('C', 'E', 4), ('F', 'G', 2)]

oracle_value = [14]
bnb = BranchAndBound(edges_with_cost, oracle_value)
bnb.visualize_optimal_path_bnb('S', 'G')
