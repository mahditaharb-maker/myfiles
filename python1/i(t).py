import numpy as np
import matplotlib.pyplot as plt

# Given data
V = 100   # Voltage in Volts
R = 200   # Resistance in Ohms
C = 10**-4  # Capacitance in Farads
k = 1 / (R * C)  # Decay constant (50)

# Time range
t = np.linspace(0, 0.1, 1000)

# Current equation: i(t) = (V/R) * exp(-kt)
i_t = (V / R) * np.exp(-k * t)

# Plot current i(t)
plt.figure(figsize=(8, 5))
plt.plot(t, i_t, label="Current i(t)", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Current Decay in RC Circuit")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
