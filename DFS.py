import networkx as nx
import matplotlib.pyplot as plt

class DepthFirstSearch:
    def __init__(self, edges_dfs):
        self.edges = edges_dfs
        self.graph_dict = {}
        self.found_path = False
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)

    def depth_first_search_dfs(self, start_node, end_node, current_path=[]):
        if self.found_path:
            return []
        current_path.append(start_node)
        if start_node == end_node:
            self.found_path = True
            return [current_path]

        if start_node not in self.graph_dict:
            return []

        sorted_neighbors = sorted(self.graph_dict[start_node])
        paths = []

        for neighbor in sorted_neighbors:
            if neighbor not in current_path:
                new_paths = self.depth_first_search_dfs(neighbor, end_node, current_path.copy())
                paths.extend(new_paths)

        return paths

    def visualize_paths_dfs(self, start_node, end_node):
        paths = self.depth_first_search_dfs(start_node, end_node)
        if paths:
            print("Path derived by Depth First Search Algorithm:")
            for path in paths:
                print(" -> ".join(path))
        else:
            print("No valid path found.")

        # Create a directed graph for visualization
        G = nx.DiGraph()
        for start, end in self.edges:
            G.add_edge(start, end)

        # Create a plot for the graph
        pos = nx.spring_layout(G, seed=42)  # You can choose different layout algorithms

        # Draw the graph nodes and edges
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
        plt.title("Graph Visualization")

        # Highlight the DFS path
        for path in paths:
            dfs_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='red', width=2)

        # Show the plot
        plt.show()

# Define the edges with updated values
edges_dfs = [('S', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')]
dfs = DepthFirstSearch(edges_dfs)
dfs.visualize_paths_dfs('S', 'G')
