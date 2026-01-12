from fractions import Fraction
from sympy import primerange
from typing import Dict

def legendre_symbol(a: int, p: int) -> int:
    """
    Compute the Legendre symbol (a|p):
      1  if a is a nonzero quadratic residue mod p
     -1  if a is a non-residue mod p
      0  if a ≡ 0 mod p
    """
    a_mod = a % p
    if a_mod == 0:
        return 0
    ls = pow(a_mod, (p - 1) // 2, p)
    return 1 if ls == 1 else -1

def ultraproduct_legendre_sequence(
    r: float,
    max_prime: int,
    max_denominator: int = 10000
) -> Dict[int, int]:
    """
    For each prime p ≤ max_prime, compute the Legendre symbol of the F_p–
    representative of r (via its best rational approximation m/n).
    Returns a dict mapping p → (−1, 0, +1).
    """
    # 1) approximate r by a fraction m/n
    frac = Fraction(r).limit_denominator(max_denominator)
    m, n = frac.numerator, frac.denominator

    seq: Dict[int, int] = {}
    for p in primerange(2, max_prime + 1):
        if n % p == 0:
            seq[p] = 0
        else:
            inv_n = pow(n, p - 2, p)   # n^(p-2) ≡ n^(-1) mod p
            a_p = (m * inv_n) % p
            seq[p] = legendre_symbol(a_p, p)
    return seq

if __name__ == "__main__":
    max_p = int(input("Enter maximum prime: "))
    r = float(input("Enter real number: "))
    seq = ultraproduct_legendre_sequence(r, max_p)

    print("\n   p  → symbol")
    print("  ----+-------")
    for p, sym in seq.items():
        print(f"  {p:3d}  → {sym:+d}")
    
    # And if you want just the list of symbols:
    symbols = [seq[p] for p in sorted(seq)]
    print("\nSequence of symbols:", symbols)
