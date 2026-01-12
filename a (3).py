#!/usr/bin/env python3
"""
test.py

Generate all finite fields GF(p^n) of order < max_q, together with
one example monic irreducible polynomial in GF(p)[x] of degree n.

If you run without arguments, it will prompt you for MAX_Q.
You can also do:
    python test.py 50
to skip the prompt and use MAX_Q=50 directly.
"""

import sys
from itertools import product

# sympy is used for prime generation and irreducibility tests
import sympy as sp
from sympy import Poly
from sympy.abc import x


def find_irreducible_polynomial(p: int, n: int) -> Poly:
    """
    Brute-force search for the lexicographically smallest monic irreducible
    polynomial of degree n over GF(p). Returns a sympy.Poly or None.
    """
    # Try all choices of coefficients for x^(n-1),…,x^0 in GF(p)
    for coeffs in product(range(p), repeat=n):
        # Build x^n + a_{n-1} x^(n-1) + … + a_0
        expr = x**n
        for i, a in enumerate(coeffs):
            expr += a * x**i
        poly = Poly(expr, x, modulus=p)
        if poly.is_irreducible:
            return poly
    return None


def generate_finite_fields(max_q: int):
    """
    Returns a list of (q, p, n, f) tuples where
      - p is prime,
      - n ≥ 1 integer,
      - q = p^n < max_q,
      - f(x) is a monic irreducible polynomial in GF(p)[x] of degree n.
    """
    result = []
    # Generate all primes p < max_q
    for p in sp.primerange(2, max_q):
        n = 1
        while True:
            q = p**n
            if q >= max_q:
                break
            f = find_irreducible_polynomial(p, n)
            if f:
                result.append((q, p, n, f))
            n += 1
    # Sort by field size q
    return sorted(result, key=lambda t: t[0])


def main():
    # 1) Try to read max_q from command-line
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        max_q = int(sys.argv[1])
    else:
        # 2) Otherwise prompt interactively
        while True:
            try:
                raw = input("Enter MAX_Q (e.g. 100): ")
                max_q = int(raw)
                break
            except ValueError:
                print("Please enter a positive integer for MAX_Q.")

    fields = generate_finite_fields(max_q)

    # Print a simple table to the console
    print(f"{'q':>4} | {'p':>2} | {'n':>2} | irreducible polynomial over GF(p)")
    print("-" * 60)
    for q, p, n, poly in fields:
        # sp.sstr formats the polynomial in a readable way
        print(f"{q:>4} | {p:>2} | {n:>2} | {sp.sstr(poly.as_expr())}")


if __name__ == "__main__":
    main()
