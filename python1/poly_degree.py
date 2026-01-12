#!/usr/bin/env python3
# Python 3.8 compatible

from math import sqrt

def degree(poly):
    """Return degree of polynomial (highest bit index)."""
    return poly.bit_length() - 1

def poly_mul(a, b):
    """Multiply two polynomials in GF(2) (no modulus)."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result

def poly_mod(num, mod_poly):
    """Compute num(x) mod mod_poly(x) over GF(2)."""
    dm = degree(mod_poly)
    while degree(num) >= dm:
        shift = degree(num) - dm
        num ^= (mod_poly << shift)
    return num

def is_irreducible(poly):
    """Check if poly is irreducible over GF(2) via Rabin’s test."""
    d = degree(poly)
    # x^(2^i) mod poly minus x should be non-zero for all 1 <= i <= d//2
    test = 2  # represents x
    for i in range(1, d // 2 + 1):
        test = poly_mod(poly_mul(test, test), poly)
        if poly_mod(test ^ 2, poly) == 0:
            return False
    return True

def is_primitive(poly):
    """Check if irreducible poly is primitive: x is a generator of GF(2^d)*."""
    if not is_irreducible(poly):
        return False
    d = degree(poly)
    order = (1 << d) - 1  # 2^d - 1
    # factor order and ensure x^(order / p) != 1 for each prime p dividing order
    n = order
    primes = set()
    # simple factorization
    p = 2
    while p * p <= n:
        if n % p == 0:
            primes.add(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        primes.add(n)
    # test generator property
    for p in primes:
        if poly_mod(pow(2, order // p, poly), poly) == 1:
            return False
    return True

def primitive_polys(deg):
    """Return all primitive polynomials of exact degree `deg` over GF(2)."""
    results = []
    # iterate over monic polynomials of degree `deg`
    start = 1 << deg
    end = 1 << (deg + 1)
    for poly in range(start + 1, end, 2):  # skip even (must have constant term 1)
        if is_primitive(poly):
            results.append(poly)
    return results

def poly_to_str(poly):
    """Pretty-print a polynomial integer as e.g. x^4 + x + 1."""
    terms = []
    for i in range(degree(poly), -1, -1):
        if (poly >> i) & 1:
            if i == 0:
                terms.append("1")
            elif i == 1:
                terms.append("x")
            else:
                terms.append(f"x^{i}")
    return " + ".join(terms) or "0"

# Example usage
if __name__ == "__main__":
    for d in range(1, 6):
        prims = primitive_polys(d)
        print(f"Degree {d} primitives:")
        for p in prims:
            print("   ", poly_to_str(p))
        print()
