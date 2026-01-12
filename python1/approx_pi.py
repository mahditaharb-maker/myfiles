from fractions import Fraction

n = 10000  # Number of points
inside = 0

# Count points inside the "circle"
for x in range(-100, 101):
    for y in range(-100, 101):
        if x**2 + y**2 <= 100**2:  # Circle boundary
            inside += 1

# Approximation as a fraction
approx_pi = Fraction(inside, n) * 4
print(f"Approximation of pi as fraction: {approx_pi}")
