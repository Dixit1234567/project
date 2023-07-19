import numpy as np

# Create a NumPy array
numbers = np.array([1, 2, 3, 4, 5])

# Perform some common NumPy functions
mean_value = np.mean(numbers)
median_value = np.median(numbers)
standard_deviation = np.std(numbers)
variance = np.var(numbers)

# Print the results
print("Original array:", numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", standard_deviation)
print("Variance:", variance)
