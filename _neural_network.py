import numpy as np

inputs = np.array([1, 2])
weights = np.array([[0.5, 0.3],
                    [0.2, 0.8]])

output = np.dot(inputs, weights)

print("Output:", output)
