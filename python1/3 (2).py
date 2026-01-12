import numpy as np
import matplotlib.pyplot as plt

# Given data
C = 10**-4  # Capacitance in Farads
R = 200  # Resistance in Ohms
V = 100  # Voltage in Volts
k = 1 / (R * C)  # Decay constant (50)

# Time range
t = np.linspace(0, 0.1, 1000)  # Time from 0 to 0.1 seconds

# Charge equation: q(t) = (V * C) * (1 - exp(-kt))
q_t = (V * C) * (1 - np.exp(-k * t))

# Current equation: i(t) = (V/R) * exp(-kt)
i_t = (V/R) * np.exp(-k * t)

# Plot charge q(t)
plt.figure(figsize=(10, 5))
plt.plot(t, q_t, label="Charge q(t)", color="blue")
plt.plot(t, i_t, label="Current i(t)", color="red", linestyle="dashed")

# Labels and title
plt.xlabel("Time (s)")
plt.ylabel("Charge (C) / Current (A)")
plt.title("Charge and Current in RC-Series Circuit")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
