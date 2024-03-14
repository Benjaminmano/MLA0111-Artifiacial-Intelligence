from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        bfs_order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                bfs_order.append(node)
                visited.add(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return bfs_order

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

print("BFS traversal:", graph.bfs(0))
