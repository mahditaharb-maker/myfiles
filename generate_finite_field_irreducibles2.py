#!/usr/bin/env python3
"""
Given a prime p, find the lexicographically smallest monic irreducible
polynomial of lowest non‐trivial degree over GF(p), and print both the
polynomial and the defining relation for a root α.
"""

import sys
from itertools import product

import sympy as sp
from sympy import Poly
from sympy.abc import x


def find_irreducible_poly(p: int):
    """
    Search for the smallest-degree monic irreducible polynomial over GF(p).
    Returns a sympy.Poly, or None if none found up through degree p.
    """
    # skip n=1 (all x+a are irreducible but trivial), start at n=2
    for n in range(2, p + 1):
        for coeffs in product(range(p), repeat=n):
            # build x^n + a_{n-1} x^{n-1} + … + a_0
            expr = x**n
            for i, a in enumerate(coeffs):
                expr += a * x**i
            poly = Poly(expr, x, modulus=p)
            if poly.is_irreducible:
                return poly
    return None


def format_defining_relation(poly: Poly, p: int):
    """
    Given an irreducible polynomial f(x) over GF(p), build the relation
    α^n = -(a_{n-1} α^{n-1} + … + a_0) in GF(p).
    """
    deg = poly.degree()
    coeffs = poly.all_coeffs()  # [1, a_{n-1}, a_{n-2}, ..., a_0]
    terms = []
    # for each coefficient a_i (skipping leading 1)
    for i, a in enumerate(coeffs[1:], start=1):
        if a % p == 0:
            continue
        # compute -(a) mod p
        coeff = (-a) % p
        exp = deg - i
        if exp == 0:
            term = f"{coeff}"
        elif exp == 1:
            term = f"{coeff}*α"
        else:
            term = f"{coeff}*α**{exp}"
        terms.append(term)

    rhs = " + ".join(terms) if terms else "0"
    return f"α**{deg} = {rhs}  (in GF({p}))"


def main():
    try:
        p = int(input("Enter prime p: ").strip())
    except ValueError:
        sys.exit("Error: p must be an integer.")

    if not sp.isprime(p):
        sys.exit(f"Error: {p} is not prime.")

    poly = find_irreducible_poly(p)
    if poly is None:
        print(f"No irreducible polynomial found for GF({p}) up to degree {p}.")
        return

    f = poly.as_expr()
    print(f"Smallest non‐trivial irreducible polynomial over GF({p}):")
    print("    f(x) =", sp.sstr(f), "mod", p)
    print()
    print("Defining relation:")
    print("    let α be a root of f(x), then")
    print("    ", format_defining_relation(poly, p))


if __name__ == "__main__":
    main()
