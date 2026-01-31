import numpy as np
import matplotlib.pyplot as plt
import os
# Define the function
def f(x):
    return x**2 * np.sin(x)

# Define the interval
x = np.linspace(-10, 10, 400)
y = f(x)

# Create the plot
plt.figure()
plt.plot(x, y, label="f(x) = x² sin(x)")

# Axes lines
plt.axhline(0)
plt.axvline(0)

# Labels and title
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graphical Visualization of the Function f(x) = x² sin(x)")
plt.legend()
plt.grid()


# Save PNG with same name as script
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"{script_name}.png", dpi=300, bbox_inches="tight")

# Display the figure
plt.show()


