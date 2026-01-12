from math import factorial
from fractions import Fraction

mod = 65537 # Modular base (can adjust)
terms = 100  # Number of terms to calculate
approx_e = sum(Fraction(1, factorial(n)) for n in range(terms)) % mod

print(f"Approximation of e as fraction: {approx_e}")
