class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)

    def dfs_util(self, node, visited, dfs_order):
        visited.add(node)
        dfs_order.append(node)

        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, dfs_order)

    def dfs(self, start):
        visited = set()
        dfs_order = []
        self.dfs_util(start, visited, dfs_order)
        return dfs_order

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

print("DFS traversal:", graph.dfs(0))
