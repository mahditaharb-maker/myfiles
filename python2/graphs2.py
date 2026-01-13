import numpy as np
import matplotlib.pyplot as plt

# Time range
t = np.linspace(0, 0.1, 1000)  # Time from 0 to 0.1 seconds

# Charge equation: q(t) = 10^-2 (1 - exp(-20t)) C
q_t = 10**-2 * (1 - np.exp(-20 * t))

# Current equation: i(t) = 0.2 * exp(-20t) A
i_t = 0.2 * np.exp(-20 * t)

# Plot charge q(t)
plt.figure(figsize=(8, 5))
plt.plot(t, q_t, color="blue", label="Charge q(t)")
plt.xlabel("Time (s)")
plt.ylabel("Charge (C)")
plt.title("Charge Build-up in RC Circuit")
plt.legend()
plt.grid(True)

# Plot current i(t)
plt.figure(figsize=(8, 5))
plt.plot(t, i_t, color="red", label="Current i(t)")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Current Decay in RC Circuit")
plt.legend()
plt.grid(True)

# Show the plots
plt.show()
