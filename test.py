import sympy

# Function to compute b_n = smallest prime divisor of a_n = 2^n + 1
def b(n):
    a_n = 2**n + 1
    return sympy.divisors(a_n)[1]  # [0] = 1, [1] = smallest prime

# Compute b_n and b_{5n} for several values of n
results = [(n, b(n), b(5*n)) for n in range(1, 21)]

for n, bn, b5n in results:
    print(f"n = {n:2}, b_n = {bn}, b_5n = {b5n}, Equal? {bn == b5n}")
