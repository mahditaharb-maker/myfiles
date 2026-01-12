import numpy as np

# Sample grouped data: (midpoint, frequency)
grouped_data = [
    (7.75, 2),
    (10.75, 7),
    (13.75, 3),
    (16.75, 4),
    
]

# Extract midpoints and frequencies
midpoints = np.array([x[0] for x in grouped_data])
frequencies = np.array([x[1] for x in grouped_data])

# Total frequency
total_frequency = np.sum(frequencies)

# Mean calculation
mean = np.sum(midpoints * frequencies) / total_frequency

# Variance calculation
variance = np.sum(frequencies * (midpoints - mean)**2) / total_frequency

# Standard deviation
std_dev = np.sqrt(variance)

# Mode (midpoint with highest frequency)
mode = midpoints[np.argmax(frequencies)]

# Print results
print(f"Mean: {mean:.5f}")
print(f"Variance: {variance:.5f}")
print(f"Standard Deviation: {std_dev:.5f}")
print(f"Mode: {mode}")
