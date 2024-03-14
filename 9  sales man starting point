import sys

def tsp_dp(distances):
    n = len(distances)
    memo = {}

    # Helper function to recursively calculate the shortest path
    def tsp_helper(curr, visited):
        if (curr, visited) in memo:
            return memo[(curr, visited)]

        # Base case: if all cities have been visited, return the distance to the starting city
        if visited == (1 << n) - 1:
            return distances[curr][0]

        min_distance = sys.maxsize

        for next_city in range(n):
            if not visited & (1 << next_city):  # Check if next_city has not been visited
                new_visited = visited | (1 << next_city)
                distance_to_next = distances[curr][next_city] + tsp_helper(next_city, new_visited)
                min_distance = min(min_distance, distance_to_next)

        memo[(curr, visited)] = min_distance
        return min_distance

    # Start the recursion from the starting city (index 0)
    return tsp_helper(0, 1)

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_route_length = tsp_dp(distances)
print("Shortest route length:", shortest_route_length)
