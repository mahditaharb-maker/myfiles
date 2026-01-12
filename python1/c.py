def integer_solutions(x_min, x_max):
    """
    Returns a list of (t, x) pairs such that x^2 - x + t = 0 has integer root x.
    Based on t = x - x^2.
    """
    solutions = []
    for x in range(x_min, x_max + 1):
        t = x - x*x
        solutions.append((t, x))
    return solutions

# Example: scan x from -10 to 10
if __name__ == "__main__":
    sol = integer_solutions(-10, 10)
    for t, x in sol:
        print(f"t = {t:3d},  x = {x:3d}")
