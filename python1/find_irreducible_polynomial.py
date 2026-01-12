#!/usr/bin/env python3
"""
Given a prime p and degree n, find the lexicographically smallest
monic irreducible polynomial of degree n over GF(p).
"""

import sys
from itertools import product

import sympy as sp
from sympy import Poly
from sympy.abc import x

def find_irreducible_polynomial(p: int, n: int) -> Poly:
    # Try all coefficient‐tuples (a_{n-1},…,a_0) in GF(p)
    for coeffs in product(range(p), repeat=n):
        expr = x**n
        for i, a in enumerate(coeffs):
            expr += a * x**i
        poly = Poly(expr, x, modulus=p)
        if poly.is_irreducible:
            return poly
    return None

def main():
    try:
        p = int(input("Enter prime p: "))
        n = int(input("Enter degree n: "))
    except ValueError:
        print("Both p and n must be integers.")
        sys.exit(1)

    if not sp.isprime(p):
        print(f"{p} is not prime. Exiting.")
        sys.exit(1)

    poly = find_irreducible_polynomial(p, n)
    if poly:
        # sstr gives a nice human‐readable string
        print(f"Irreducible polynomial over GF({p}) of degree {n}:")
        print("   ", sp.sstr(poly.as_expr()))
    else:
        print(f"No irreducible polynomial of degree {n} found over GF({p}).")

if __name__ == "__main__":
    main()
