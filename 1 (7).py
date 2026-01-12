#!/usr/bin/env python3
import math
import sys
from itertools import product
from sympy import symbols, Poly, GF, rem

def is_prime_power(n):
    for p in range(2, int(math.isqrt(n)) + 2):
        if n % p == 0:
            k, tmp = 0, n
            while tmp % p == 0:
                tmp //= p
                k += 1
            if tmp == 1 and all(p % q for q in range(2, int(math.isqrt(p)) + 1)):
                return p, k
    if all(n % q for q in range(2, int(math.isqrt(n)) + 1)):
        return n, 1
    return None, None

def find_irred_poly(p, k):
    x = symbols('x')
    for coeffs in product(range(p), repeat=k):
        poly = Poly(x**k + sum(c*x**i for i,c in enumerate(coeffs)),
                    x, domain=GF(p))
        if poly.is_irreducible:
            return poly
    raise ValueError(f"No irreducible polynomial for GF({p}^{k})")

def build_field(p, k, irr_poly=None):
    if k == 1:
        elems = list(range(p))
        return (
            elems,
            lambda a,b: (a + b) % p,
            lambda a,b: (a * b) % p,
            lambda a: str(a)
        )

    x = symbols('x')
    elems = list(product(range(p), repeat=k))

    def to_poly(v):
        return sum(coef * x**i for i,coef in enumerate(v))

    def to_vec(poly):
        remp = rem(Poly(poly, x, domain=GF(p)),
                   irr_poly, domain=GF(p))
        coeffs = [0]*k
        for mon,c in zip(remp.monoms(), remp.coeffs()):
            coeffs[mon[0]] = int(c)
        return tuple(coeffs)

    def add(a,b):
        return tuple((a[i] + b[i]) % p for i in range(k))

    def mul(a,b):
        prod = Poly(to_poly(a) * to_poly(b), x, domain=GF(p))
        return to_vec(prod)

    def fmt(v):
        terms = []
        for i,c in enumerate(v):
            if c:
                if i == 0:
                    terms.append(f"{c}")
                elif c == 1:
                    terms.append(f"x^{i}")
                else:
                    terms.append(f"{c}x^{i}")
        return "0" if not terms else " + ".join(terms)

    return elems, add, mul, fmt

def tex_table(elems, op, fmt):
    labels = [fmt(e) for e in elems]
    n = len(elems)

    lines = []
    # Here’s the fix: one single f-string, no raw-string split
    lines.append(f"\\begin{{array}}{{c|{'c'*n}}}")
    lines.append(" & " + " & ".join(labels) + r" \\")
    lines.append(r"\hline")
    for a in elems:
        row = [fmt(a)] + [fmt(op(a,b)) for b in elems]
        lines.append(" & ".join(row) + r" \\")
    lines.append(r"\end{array}")
    return "\n".join(lines)

def generate_gf_tex(n):
    p,k = is_prime_power(n)
    if p is None:
        raise ValueError(f"{n} is not a prime power.")
    irr = None if k==1 else find_irred_poly(p,k)
    elems, add, mul, fmt = build_field(p,k,irr)

    add_tbl = tex_table(elems, add, fmt)
    mul_tbl = tex_table(elems, mul, fmt)

    print("\

\[")
    print(f"\\text{{Addition in }}\\mathbb{{F}}_{{{n}}}=")
    print(add_tbl)
    print("\\]

\n")

    print("\

\[")
    print(f"\\text{{Multiplication in }}\\mathbb{{F}}_{{{n}}}=")
    print(mul_tbl)
    print("\\]

\n")

if __name__ == "__main__":
    # Allow: python 1.py 9
    n = int(sys.argv[1]) if len(sys.argv)>1 else 9
    generate_gf_tex(n)
