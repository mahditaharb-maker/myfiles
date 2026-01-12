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

def poly_pow_mod(base, exponent, mod_poly):
    """Compute base(x)^exponent mod mod_poly(x) in GF(2)."""
    result = 1
    while exponent:
        if exponent & 1:
            result = poly_mod(poly_mul(result, base), mod_poly)
        base = poly_mod(poly_mul(base, base), mod_poly)
        exponent >>= 1
    return result

def is_irreducible(poly):
    """Check if poly is irreducible over GF(2) via Rabin’s test."""
    d = degree(poly)
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

    # Factor 2^d - 1 and collect prime divisors
    n = order
    primes = set()
    p = 2
    while p * p <= n:
        if n % p == 0:
            primes.add(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        primes.add(n)

    # Verify generator property
    for p in primes:
        if poly_pow_mod(2, order // p, poly) == 1:
            return False

    return True

def primitive_polys(deg):
    """Return all primitive polynomials of exact degree `deg` over GF(2)."""
    results = []
    start = 1 << deg
    end   = 1 << (deg + 1)
    for poly in range(start + 1, end, 2):  # monic, constant term = 1
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

if __name__ == "__main__":
    print()
    print("Primitive Polynomial Finder over GF(2)")
    print("This program lists all primitive (maximal-period) polynomials of degree d.")
    print()

    # Prompt for user input
    try:
        deg = int(input("Enter desired degree (e.g. 1, 2, 3, ...): ").strip())
        if deg < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer degree.")
        exit(1)

    prims = primitive_polys(deg)
    if not prims:
        print(f"No primitive polynomials found for degree {deg}.")
    else:
        print(f"\nPrimitive polynomials of degree {deg}:")
        for p in prims:
            print("  ", poly_to_str(p))
    print()
