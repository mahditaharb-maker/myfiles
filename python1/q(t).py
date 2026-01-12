import numpy as np
import matplotlib.pyplot as plt

# Given data
V = 100
C = 10**-4
k = 1 / (200 * C)

# Time range
t = np.linspace(0, 0.1, 1000)

# Charge equation: q(t) = (V*C) * (1 - exp(-kt)), flipped for symmetry
q_t = 1 - np.exp(-k * t)  # Scaling it to match the symmetry of i(t)

# Plot charge q(t)
plt.figure(figsize=(8, 5))
plt.plot(t, q_t, label="Scaled Charge q(t)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Scaled Charge (unitless)")
plt.title("Charge Build-up in RC Circuit (Symmetric to i(t))")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
