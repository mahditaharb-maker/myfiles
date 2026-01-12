import numpy as np
import matplotlib.pyplot as plt

# Given circuit parameters
E = 100     # Voltage in Volts
R = 500     # Resistance in Ohms
C = 10**-4  # Capacitance in Farads
k = 1 / (R * C)  # Decay constant

# Time range
t = np.linspace(0, 0.1, 1000)

# Charge equation: q(t) = (V*C) * (1 - exp(-kt))
q_t = (E * C) * (1 - np.exp(-k * t))

# Current equation: i(t) = (E/R) * exp(-kt)
i_t = (E / R) * np.exp(-k * t)

# Create figure for Charge q(t)
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(t, q_t, color="blue", label="Charge q(t)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Charge (C)")
ax1.set_title("Charge Build-Up in RC Circuit")
ax1.grid(True)
ax1.legend()
ax1.set_xlim([0, 0.1])
ax1.set_ylim([0, max(q_t) * 1.1])  # Adjust y-scale for symmetry

# Create figure for Current i(t) with inverted scale for symmetry
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(t, -i_t, color="red", label="Inverted Current i(t)")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Scaled Current (-A)")  # Negative for symmetry
ax2.set_title("Current Decay in RC Circuit (Symmetric Representation)")
ax2.grid(True)
ax2.legend()
ax2.set_xlim([0, 0.1])
ax2.set_ylim([min(-i_t) * 1.1, 0])  # Adjust scale for symmetry

# Show both figures
plt.show()
