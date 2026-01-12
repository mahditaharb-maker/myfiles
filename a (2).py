# Grouped data for k = 6
# Each class has: frequency fi and midpoint mi

# Data
frequencies = [2, 7, 3, 4]
midpoints = [7.75, 10.75, 13.75, 15.75]

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
