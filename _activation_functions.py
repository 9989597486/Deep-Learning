import math

x = 2

sigmoid = 1 / (1 + math.exp(-x))
relu = max(0, x)

print("Sigmoid:", sigmoid)
print("ReLU:", relu)
