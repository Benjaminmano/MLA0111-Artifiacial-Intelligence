import random

# Define the objective function
def objective_function(x):
    return x ** 2  # Example objective function (minimize x^2)


# Hill Climbing Algorithm
def hill_climbing(max_iterations, step_size, current_solution):
    for _ in range(max_iterations):
        next_solution = current_solution + random.uniform(-step_size, step_size)
        if objective_function(next_solution) < objective_function(current_solution):
            current_solution = next_solution
    return current_solution


# Example usage
initial_solution = 10  # Initial solution
max_iterations = 1000  # Maximum number of iterations
step_size = 0.1  # Step size for perturbation

final_solution = hill_climbing(max_iterations, step_size, initial_solution)
print("Final solution:", final_solution)
print("Objective function value:", objective_function(final_solution))
