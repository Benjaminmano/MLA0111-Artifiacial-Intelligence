import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    # Manhattan distance heuristic
    return abs(current.position[0] - goal.position[0]) + abs(current.position[1] - goal.position[1])

def astar(maze, start, goal):
    open_list = []
    closed_set = set()
    
    start_node = Node(start)
    goal_node = Node(goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node)
        
        if current_node == goal_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Adjacent squares
        
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            if node_position[0] < 0 or node_position[0] >= len(maze) or node_position[1] < 0 or node_position[1] >= len(maze[0]):
                continue
            
            if maze[node_position[0]][node_position[1]] == 1:
                continue
            
            new_node = Node(node_position, current_node)
            
            if new_node in closed_set:
                continue
            
            new_node.g = current_node.g + 1
            new_node.h = heuristic(new_node, goal_node)
            new_node.f = new_node.g + new_node.h
            
            for open_node in open_list:
                if new_node == open_node and new_node.g > open_node.g:
                    continue
            
            heapq.heappush(open_list, new_node)
    
    return None  # No path found

# Example usage:
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(maze, start, goal)
print(path)
