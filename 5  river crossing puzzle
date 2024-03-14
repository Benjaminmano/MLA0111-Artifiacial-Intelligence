class State:
    def __init__(self, left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals):
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.boat = boat
        self.right_missionaries = right_missionaries
        self.right_cannibals = right_cannibals

    def is_valid(self):
        if self.left_missionaries < 0 or self.left_cannibals < 0 or self.right_missionaries < 0 or self.right_cannibals < 0:
            return False
        if self.left_missionaries > 0 and self.left_cannibals > self.left_missionaries:
            return False
        if self.right_missionaries > 0 and self.right_cannibals > self.right_missionaries:
            return False
        return True

    def is_goal(self):
        return self.left_missionaries == 0 and self.left_cannibals == 0

    def __eq__(self, other):
        return (self.left_missionaries == other.left_missionaries and
                self.left_cannibals == other.left_cannibals and
                self.boat == other.boat and
                self.right_missionaries == other.right_missionaries and
                self.right_cannibals == other.right_cannibals)

    def __hash__(self):
        return hash((self.left_missionaries, self.left_cannibals, self.boat, self.right_missionaries, self.right_cannibals))


def get_next_states(current_state):
    next_states = []
    if current_state.boat == 'left':
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    next_states.append(State(current_state.left_missionaries - i, current_state.left_cannibals - j, 'right',
                                             current_state.right_missionaries + i, current_state.right_cannibals + j))
    else:
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    next_states.append(State(current_state.left_missionaries + i, current_state.left_cannibals + j, 'left',
                                             current_state.right_missionaries - i, current_state.right_cannibals - j))
    return [state for state in next_states if state.is_valid()]


def dfs(current_state, visited, path):
    if current_state.is_goal():
        return path
    visited.add(current_state)
    for next_state in get_next_states(current_state):
        if next_state not in visited:
            new_path = path + [next_state]
            result = dfs(next_state, visited, new_path)
            if result:
                return result
    return None


def solve():
    initial_state = State(3, 3, 'left', 0, 0)
    visited = set()
    path = dfs(initial_state, visited, [initial_state])
    if path:
        return path
    return "No solution"


def print_solution(solution):
    if solution == "No solution":
        print("No solution found.")
    else:
        for i, state in enumerate(solution):
            print(f"Step {i + 1}:")
            print(f"Left side: {state.left_missionaries} missionaries, {state.left_cannibals} cannibals")
            print(f"Boat: {'left' if state.boat == 'right' else 'right'}")
            print(f"Right side: {state.right_missionaries} missionaries, {state.right_cannibals} cannibals")
            print()


if __name__ == "__main__":
    solution = solve()
    print_solution(solution)
