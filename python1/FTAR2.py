#!/usr/bin/env python3
import sys
from typing import List

MAX_N = 100_000

def build_spf(n: int) -> List[int]:
    """
    Build spf[0..n], where spf[x] is the smallest prime divisor of x.
    """
    spf: List[int] = list(range(n+1))
    spf[0] = spf[1] = 1
    limit = int(n**0.5) + 1
    for p in range(2, limit):
        if spf[p] == p:               # p is prime
            for multiple in range(p*p, n+1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
    return spf

def factorize(n: int, spf: List[int]) -> List[int]:
    """
    Return prime factors of n in non-decreasing order.
    """
    facs: List[int] = []
    while n > 1:
        p = spf[n]
        facs.append(p)
        n //= p
    return facs

def verify_fta(spf: List[int]) -> None:
    """
    Check for every 2 ≤ n ≤ MAX_N that product(factors)==n.
    """
    for x in range(2, MAX_N+1):
        facs = factorize(x, spf)
        prod = 1
        for p in facs:
            prod *= p
        assert prod == x, f"FTA violation at {x}: {facs}"
    print(f"✔ Verified FTA for all 2 ≤ n ≤ {MAX_N}")

def main():
    spf = build_spf(MAX_N)
    verify_fta(spf)

    try:
        n = int(input(f"Enter n (2–{MAX_N}): ").strip())
    except ValueError:
        print("Invalid integer.", file=sys.stderr)
        sys.exit(1)

    if not (2 <= n <= MAX_N):
        print(f"Pick n between 2 and {MAX_N}.", file=sys.stderr)
        sys.exit(1)

    facs = factorize(n, spf)
    print(f"{n} = " + " * ".join(map(str, facs)))

if __name__ == "__main__":
    main()
