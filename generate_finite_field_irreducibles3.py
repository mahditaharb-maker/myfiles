#!/usr/bin/env python3
import sys
from itertools import product
from typing import Optional      # ← add this
import sympy as sp
from sympy import Poly
from sympy.abc import x

def find_irreducible_poly(p: int, n: int) -> Optional[Poly]:   # ← use Optional[Poly]
    """
    Search for the lexicographically smallest monic irreducible
    polynomial of degree exactly n over GF(p). Returns a Poly or None.
    """
    for coeffs in product(range(p), repeat=n):
        expr = x**n
        for i, a in enumerate(coeffs):
            expr += a * x**i
        poly = Poly(expr, x, modulus=p)
        if poly.is_irreducible:
            return poly
    return None

def format_defining_relation(poly: Poly, p: int) -> str:
    n = poly.degree()
    coeffs = poly.all_coeffs()
    terms = []
    for idx, a in enumerate(coeffs[1:], start=1):
        a_mod = a % p
        if a_mod == 0:
            continue
        c = (-a_mod) % p
        exp = n - idx
        if exp == 0:
            term = f"{c}"
        elif exp == 1:
            term = f"{c}*α"
        else:
            term = f"{c}*α**{exp}"
        terms.append(term)
    rhs = " + ".join(terms) if terms else "0"
    return f"α**{n} = {rhs}  (in GF({p}))"

def main():
    try:
        p = int(input("Enter prime p: ").strip())
        n = int(input("Enter degree n (≥ 2): ").strip())
    except ValueError:
        sys.exit("Error: p and n must be integers.")

    if not sp.isprime(p):
        sys.exit(f"Error: {p} is not prime.")
    if n < 2:
        sys.exit("Error: n must be ≥ 2.")

    poly = find_irreducible_poly(p, n)
    if poly is None:
        print(f"No irreducible polynomial of degree {n} over GF({p}).")
        return

    f = poly.as_expr()
    print(f"\nIrreducible polynomial f(x) over GF({p}):")
    print("   ", sp.sstr(f), "mod", p)
    print("\nDefining relation:")
    print("   Let α be a root of f(x), then")
    print("   ", format_defining_relation(poly, p))

if __name__ == "__main__":
    main()
