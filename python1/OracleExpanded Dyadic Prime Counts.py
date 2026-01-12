#!/usr/bin/env python3
"""
Builds the oracle table F(k) = #primes in [2^k, 2^(k+1)),
writes (k, F(k)) to a file, and finds eventual monotonicity index k0.
"""

from sympy import primerange

def compute_F(max_k):
    """
    Returns a list F where F[k] = number of primes p with 2^k <= p < 2^(k+1).
    Index 0 is unused (set to None).
    """
    F = [None] * (max_k + 1)
    for k in range(1, max_k + 1):
        lo = 1 << k
        hi = 1 << (k + 1)
        count = sum(1 for _ in primerange(lo, hi))
        F[k] = count
        print(f"Computed F({k}) = {count}")
    return F

def write_table(F, filename="oracle_table.txt"):
    """
    Writes the table of (k, F[k]) to a text file.
    """
    with open(filename, "w") as fout:
        for k in range(1, len(F)):
            fout.write(f"{k}\t{F[k]}\n")
    print(f"Table written to {filename}")

def find_monotonic_index(F):
    """
    Finds the smallest k0 such that F[k] >= F[k-1] for all k in [k0+1..].
    Returns k0 if found, else None.
    """
    max_k = len(F) - 1
    # Try every candidate k0 from 1..max_k
    for k0 in range(1, max_k):
        ok = True
        for k in range(k0 + 1, max_k + 1):
            if F[k] < F[k - 1]:
                ok = False
                break
        if ok:
            return k0
    return None

def main():
    max_k = 20  # adjust as needed
    F = compute_F(max_k)
    write_table(F)
    k0 = find_monotonic_index(F)
    if k0 is not None:
        print(f"Sequence F(k) is non-decreasing for all k >= {k0}.")
    else:
        print("No index k0 found: F(k) is not eventually monotonic up to max_k.")

if __name__ == "__main__":
    main()
