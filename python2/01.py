# Grouped data for k = 6
# Each class has: frequency fi and midpoint mi

# Data
frequencies = [1, 5, 3, 3, 1, 3]
midpoints = [7.5, 9.5, 11.5, 13.5, 15.5, 17.5]

# Step 1: Compute n
n = sum(frequencies)

# Step 2: Compute sum(fi * mi)
sum_fi_mi = sum(f * m for f, m in zip(frequencies, midpoints))

# Step 3: Compute sum(fi * mi^2)
sum_fi_mi2 = sum(f * m**2 for f, m in zip(frequencies, midpoints))

# Step 4: Sample variance
s_squared = (sum_fi_mi2 - (sum_fi_mi**2) / n) / (n - 1)

# Step 5: Sample standard deviation
s = s_squared ** 0.5

# Output results
print(f"n = {n}")
print(f"Sum(fi * mi) = {sum_fi_mi:.4f}")
print(f"Sum(fi * mi^2) = {sum_fi_mi2:.4f}")
print(f"Sample Variance (s^2) = {s_squared:.4f}")
print(f"Sample Standard Deviation (s) = {s:.4f}")
