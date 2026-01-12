#!/usr/bin/env python3
"""
generate_finite_field_irreducibles.py

Generate all finite fields GF(p^n) of order < max_q, together with
one example of a monic irreducible polynomial f(x) in GF(p)[x] of degree n.

Usage:
    python generate_finite_field_irreducibles.py MAX_Q

Example:
    python generate_finite_field_irreducibles.py 100
"""
import sys
import math
from itertools import product

import sympy as sp
from sympy import Poly
from sympy.abc import x


def find_irreducible_polynomial(p: int, n: int) -> Poly:
    """
    Brute‐force search for the lexicographically smallest monic irreducible
    polynomial of degree n over GF(p).

    Returns a SymPy Poly with modulus=p, or None if not found.
    """
    # iterate over all tuples of coefficients for x^(n-1), ..., x^0
    for coeffs in product(range(p), repeat=n):
        # build the polynomial: x^n + coeffs[n-1]*x^(n-1) + ... + coeffs[0]
        expr = x**n
        for i, a in enumerate(coeffs, start=0):
            # coeffs[0] → x^0, coeffs[1] → x^1, ..., coeffs[n-1] → x^(n-1)
            expr += a * x**i
        poly = Poly(expr, x, modulus=p)
        if poly.is_irreducible:
            return poly
    return None


def generate_finite_fields(max_q: int):
    """
    Generate a list of tuples (q, p, n, f) such that:
      - p is prime
      - n >= 1 integer
      - q = p**n < max_q
      - f(x) is a monic irreducible polynomial in GF(p)[x] of degree n

    Returns:
      List of (q, p, n, Poly)
    """
    result = []
    # generate primes up to max_q
    for p in sp.primerange(2, max_q):
        # try exponents n = 1, 2, ... until p^n >= max_q
        n = 1
        while True:
            q = p**n
            if q >= max_q:
                break
            f = find_irreducible_polynomial(p, n)
            if f is not None:
                result.append((q, p, n, f))
            n += 1
    # sort by field size q
    result.sort(key=lambda tup: tup[0])
    return result


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python generate_finite_field_irreducibles.py MAX_Q")
        sys.exit(1)

    max_q = int(sys.argv[1])
    fields = generate_finite_fields(max_q)

    # print results in a simple table
    print(f"{'q':>4} | {'p':>2} | {'n':>2} | irreducible polynomial over GF(p)")
    print("-" * 60)
    for q, p, n, poly in fields:
        # poly.as_expr() gives a human‐readable sympy expression
        print(f"{q:>4} | {p:>2} | {n:>2} | {sp.sstr(poly.as_expr())}")


if __name__ == "__main__":
    main()
