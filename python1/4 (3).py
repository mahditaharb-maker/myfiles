#!/usr/bin/env python3
"""
Given a positive integer n, compute

  1) the number of (isomorphism classes of) groups of order n
  2) the number of commutative rings with unity of order n
  3) the number of finite fields of order n

We implement known classification results in special cases:
  - Groups of order p^k for k ≤ 3, or order p·q (p<q primes).
  - Commutative rings of square‐free order.
  - Finite fields exist iff n is a prime power (then exactly one).
For other orders, we raise NotImplementedError.
"""

from sympy import factorint

def num_fields(n: int) -> int:
    """
    Number of finite fields of order n.
    There is exactly one iff n = p^k for some prime p and k ≥ 1.
    Otherwise zero.
    """
    fac = factorint(n)
    if len(fac) == 1:
        # n = p^k
        return 1
    return 0

def num_groups(n: int) -> int:
    """
    Number of isomorphism classes of groups of order n,
    implemented in a few classical cases:
      • n = p^k with k ≤ 3
      • n = p·q with p<q both primes
    For other n, not implemented.
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
            return 5              # classification of groups of order p^3
        raise NotImplementedError(
            f"Group‐count for p^{k} not implemented.")
    # Case 2: product of two distinct primes
    if len(fac) == 2 and all(e == 1 for e in fac.values()):
        p, q = sorted(fac.keys())
        # if q ≡ 1 mod p, there is one non‐abelian semidirect product
        if (q - 1) % p == 0:
            return 2  # cyclic and one nonabelian
        else:
            return 1  # only cyclic
    raise NotImplementedError(
        f"Group‐count for order {n} not covered by this routine.")

def num_rings(n: int) -> int:
    """
    Number of commutative rings with unity of order n,
    up to isomorphism.  We implement only the square‐free case:
      • If n is square‐free, the only ring is ℤ/nℤ ≅ ∏ ℤ/pᵢℤ.
      • Otherwise not implemented.
    """
    fac = factorint(n)
    if all(e == 1 for e in fac.values()):
        return 1
    raise NotImplementedError(
        f"Ring‐count for non‐squarefree order {n} not implemented.")

def main():
    n = int(input("Enter n: ").strip())
    try:
        g = num_groups(n)
    except NotImplementedError as ex:
        g = str(ex)
    try:
        r = num_rings(n)
    except NotImplementedError as ex:
        r = str(ex)
    f = num_fields(n)
    print(f"Order {n}:")
    print(f"  Number of groups: {g}")
    print(f"  Number of commutative rings with 1: {r}")
    print(f"  Number of finite fields: {f}")

if __name__ == "__main__":
    main()
