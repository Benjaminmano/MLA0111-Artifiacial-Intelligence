import numpy as np

class FeedForwardNN:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        self.weights = []
        self.biases = []

        # Initialize weights and biases for each layer
        sizes = [input_size] + hidden_sizes + [output_size]
        for i in range(len(sizes) - 1):
            self.weights.append(np.random.randn(sizes[i], sizes[i+1]))
            self.biases.append(np.random.randn(sizes[i+1]))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        for i in range(len(self.weights)):
            x = self.sigmoid(np.dot(x, self.weights[i]) + self.biases[i])
        return x

# Example usage
input_size = 2
hidden_sizes = [4, 3]
output_size = 1

# Create an instance of the feedforward neural network
model = FeedForwardNN(input_size, hidden_sizes, output_size)

# Generate some sample input data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)

# Get the model predictions for the input data
predictions = model.forward(X)

print("Input Data:")
print(X)
print("\nPredictions:")
print(predictions)
