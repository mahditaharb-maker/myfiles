#!/usr/bin/env python3
"""
Check when 2 is a primitive root modulo a prime p.

This script implements:

  1. Definition of primitive root.
  2. Criterion via prime‐factor checks.
  3. Examples for p=7 and p=13.
  4. Simple prime‐factor routine (no dependencies).

References
----------
  Ireland & Rosen, A Classical Introduction to Modern Number Theory
  Burton, Elementary Number Theory
"""

import math

def prime_factors(n):
    """
    Return the set of prime divisors of n.
    """
    factors = set()
    # Factor out 2's
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # Trial division by odd
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.add(f)
            n //= f
        f += 2
    if n > 1:
        factors.add(n)
    return factors

def is_primitive_root(g, p):
    """
    Check if g is a primitive root modulo the prime p.

    By Theorem: g is primitive mod p iff
      for every prime factor q of (p-1),
      pow(g, (p-1)//q, p) != 1
    """
    assert 2 <= g < p, "g must lie in 2..p-1"
    if not all(p % q for q in prime_factors(p-1)):
        raise ValueError(f"{p} must be prime")
    for q in prime_factors(p - 1):
        if pow(g, (p - 1) // q, p) == 1:
            return False
    return True

def demonstrate(ps, base=2):
    """
    For each prime p in ps, report whether 'base' is primitive mod p.
    Show the failing exponent when it's not.
    """
    for p in ps:
        print(f"p = {p:2d}:", end=" ")
        try:
            factors = prime_factors(p - 1)
            checks = [(q, pow(base, (p - 1) // q, p)) for q in factors]
        except AssertionError:
            print("skipped (not prime)")
            continue

        if is_primitive_root(base, p):
            print(f"{base} is a primitive root (checks:", end=" ")
            print(", ".join(f"{base}^((p-1)/{q})≡{r}" for q, r in checks), "mod p)")
        else:
            fails = [q for q, r in checks if r == 1]
            print(f"{base} is NOT primitive (failed at q={fails})")

if __name__ == "__main__":
    primes_to_test = [19,23 ]
    demonstrate(primes_to_test)

    # Example output:
    # p =  7: 2 is NOT primitive (failed at q=[2])
    # p = 13: 2 is a primitive root (checks: 2^((p-1)/2)≡12, 2^((p-1)/3)≡3 mod p)
