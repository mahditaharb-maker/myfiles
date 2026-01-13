import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = -0.20           # Decay rate (per year)
P0 = 104651         # Initial population at t0 = 2000
t0 = 2000           # Starting year
tf = 2050           # Final year for the graph

# Define time values for the graph
years = np.linspace(t0, tf, 500)

# Analytical solution of the differential equation:
# P(t) = P0 * exp(r * (t - t0))
population = P0 * np.exp(r * (years - t0))

# Plotting the function
plt.figure(figsize=(10, 6))
plt.plot(years, population, color='blue', lw=2)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Decay: ')
plt.legend()
plt.grid(True)
plt.show()
