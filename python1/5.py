#!/usr/bin/env python3
"""
Given a positive integer n, compute

  1) the number of (isomorphism classes of) groups of order n
  2) the number of commutative rings with unity of order n
  3) the number of finite fields of order n

We implement known classification results in special cases:
  - Groups of order p^k for k ≤ 3, or order p·q (p<q primes).
  - Commutative rings of square‐free order and prime‐square order.
  - Finite fields exist iff n is a prime power (then exactly one).
For other orders, we raise NotImplementedError.
"""

from sympy import factorint

def num_fields(n: int) -> int:
    """
    Number of finite fields of order n.
    Exactly one if n = p^k for some prime p and k ≥ 1; otherwise zero.
    """
    fac = factorint(n)
    # A single prime power
    if len(fac) == 1:
        return 1
    return 0

def num_groups(n: int) -> int:
    """
    Number of isomorphism classes of groups of order n,
    implemented for:
      • n = p^k with k ≤ 3
      • n = p·q with p<q both primes
    """
    fac = factorint(n)
    # Case 1: prime-power
    if len(fac) == 1:
        p, k = next(iter(fac.items()))
        if k == 1:
            return 1              # cyclic of prime order
        if k == 2:
            return 2              # ℤ/p^2 and ℤ/p×ℤ/p
        if k == 3:
            return 5              # five groups of order p^3
        raise NotImplementedError(f"Group‐count for p^{k} not implemented.")
    # Case 2: product of two distinct primes
    if len(fac) == 2 and all(e == 1 for e in fac.values()):
        p, q = sorted(fac.keys())
        # if q ≡ 1 mod p, there is a nonabelian semidirect product
        return 2 if (q - 1) % p == 0 else 1
    raise NotImplementedError(f"Group‐count for order {n} not covered.")

def num_rings(n: int) -> int:
    """
    Number of commutative rings with unity of order n, up to isomorphism.
    Implemented for:
      • n square‐free  →  ℤ/nℤ  (unique)
      • n = p^2       →  three rings: ℤ/p², 𝔽_p[x]/(x²), 𝔽_p×𝔽_p
    """
    fac = factorint(n)
    # Square‐free case: only ℤ/nℤ exists
    if all(e == 1 for e in fac.values()):
        return 1
    # Prime‐square case p^2: exactly three commutative rings with 1
    if len(fac) == 1 and next(iter(fac.values())) == 2:
        return 3
    raise NotImplementedError(f"Ring‐count for order {n} not implemented.")

def main():
    try:
        n = int(input("Enter n: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
        return

    try:
        g = num_groups(n)
    except NotImplementedError as e:
        g = str(e)

    try:
        r = num_rings(n)
    except NotImplementedError as e:
        r = str(e)

    f = num_fields(n)

    print(f"\nOrder {n}:")
    print(f"  Number of groups: {g}")
    print(f"  Number of commutative rings with 1: {r}")
    print(f"  Number of finite fields: {f}")

if __name__ == "__main__":
    main()
