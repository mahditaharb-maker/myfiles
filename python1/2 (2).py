import numpy as np
import matplotlib.pyplot as plt

# Given data
P0 = 224681  # Initial population
r = 0.032  # Growth rate (3.2% per year)
years = np.arange(2010, 2025, 1)  # Range of years to plot

# Exponential growth formula
P = P0 * np.exp(r * (years - 2010))

# Plot the population growth
plt.figure(figsize=(10, 5))
plt.plot(years, P, label="Population Growth", marker='o', linestyle='-')

# Mark the target population with a dotted vertical line
target_year = 2015
target_population = 263665
plt.axvline(x=target_year, linestyle="dotted", color="black", linewidth=2, label="Year Population Reaches 263665")

# Labels and title
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Exponential Growth of Population")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
