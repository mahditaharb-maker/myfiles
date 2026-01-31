import numpy as np
import matplotlib.pyplot as plt
import os
# Define the function
def f(x):
    return  np.sin(x)

# Interval
x = np.linspace(-10, 10, 1000)
y = f(x)

# Numerical derivative
dy = np.gradient(y, x)

# Detect critical points (sign change in derivative)
critical_x = []
for i in range(len(dy) - 1):
    if dy[i] * dy[i + 1] < 0:
        critical_x.append(x[i])

critical_x = np.array(critical_x)
critical_y = f(critical_x)

# Plot
plt.figure()
plt.plot(x, y, label=r"$f(x)=sin(x)$")
plt.scatter(critical_x, critical_y, label="Critical points")

plt.axhline(0)
plt.axvline(0)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graphical Visualization with Critical Points")
plt.legend()
plt.grid()
# Save PNG with same name as script
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig(f"{script_name}.png", dpi=300, bbox_inches="tight")


# Show plot
plt.show()