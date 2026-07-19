# Simple Perceptron

inputs = [1, 1]
weights = [0.5, 0.5]
bias = -0.7

output = inputs[0] * weights[0] + inputs[1] * weights[1] + bias

if output > 0:
    print("Output: 1")
else:
    print("Output: 0")
