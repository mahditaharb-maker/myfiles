import random
import sympy

# Function to compute b_n = smallest prime divisor of a_n = 2^n + 1
def b(n):
    a_n = 2**n + 1
    return sympy.divisors(a_n)[1]  # [0] = 1, [1] = smallest prime

# Generate 10 random values of n in range 21 to 100
random_ns = random.sample(range(21, 101), 10)

# Calculate and print b_n and b_{5n}
for n in random_ns:
    bn = b(n)
    b5n = b(5*n)
    print(f"n = {n:2}, b_n = {bn}, b_5n = {b5n}, Equal? {bn == b5n}")
