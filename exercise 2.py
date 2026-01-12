import numpy as np
import matplotlib.pyplot as plt

# Given data
P0 = 224681  # Initial population
r = 0.032  # Growth rate (3.2% per year)
years = np.arange(2010, 2025, 1)  # Range of years to plot

# Exponential growth formula
P = P0 * np.exp(r * (years - 2010))

# Solve for the key year when increase surpasses half of initial population
target_population_b = P0 + (P0 / 2)  # Population increase surpasses half of initial population
target_year_b = 2010 + (np.log(target_population_b / P0) / r)  # Compute year

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(years, P, marker='o', linestyle='-')

# Vertical dotted lines for key years
plt.axvline(x=2015, linestyle="dotted", color="black", linewidth=2)  # Year when P reaches 263665
plt.axvline(x=target_year_b, linestyle="dotted", color="black", linewidth=2)  # Year when increase surpasses half

# Labels and axis limits (y-axis fixed)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Exponential Growth of Population")
plt.xlim(2010, 2025)
plt.ylim(220000, 340000)  # Fixed y-axis as requested
plt.grid(True)

# Show the graph
plt.show()
