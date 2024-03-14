from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))

    def best_first_search(self, start, goal):
        visited = set()
        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            cost, node = pq.get()
            if node == goal:
                return True
            visited.add(node)
            for neighbor, weight in self.adj_list.get(node, []):
                if neighbor not in visited:
                    pq.put((weight, neighbor))
        return False

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 7)
graph.add_edge('B', 'D', 9)
graph.add_edge('B', 'E', 8)
graph.add_edge('C', 'F', 6)

start = 'A'
goal = 'F'
if graph.best_first_search(start, goal):
    print(f"There is a path from {start} to {goal}")
else:
    print(f"There is no path from {start} to {goal}")
