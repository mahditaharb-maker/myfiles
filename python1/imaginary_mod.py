def solve_mod_equation(p):
    solutions = []
    for x in range(p):
        if (x**2+1 ) % p == 0:
            solutions.append(x)
    return solutions

# Example usage
p = int(input("Enter a prime number p: "))
sols = solve_mod_equation(p)
print(f"The imaginary number in pZ is: {sols}")
