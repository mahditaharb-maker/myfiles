from fractions import Fraction
from sympy import primerange
import math

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

def ultraproduct_sequence(r: float,
                          max_prime: int = 1000,
                          max_denominator: int = 10000
                         ) -> dict:
    """
    Return a dict mapping each prime p ≤ max_prime to the representative a_p ∈ F_p
    of the real number r, via its best rational approximation m/n with n ≤ max_denominator.
    """
    # 1) approximate r by a rational m/n
    frac = Fraction(r).limit_denominator(max_denominator)
    m, n = frac.numerator, frac.denominator

    seq = {}
    for p in primerange(2, max_prime + 1):
        # if p divides n, n has no inverse mod p; choose a_p = 0
        if n % p == 0:
            a_p = 0
        else:
            inv_n = pow(n, p-2, p)       # n^(p-2) ≡ n^(-1) mod p
            a_p = (m * inv_n) % p
        seq[p] = a_p

    return seq

# --- Example usage ---------------------------------------------------------

if __name__ == "__main__":
    # represent √2 in the ultraproduct up to primes ≤ 200
    r = math.sqrt(2)
    seq = ultraproduct_sequence(r, max_prime=200, max_denominator=100000)
    # print first 20 entries
    for i,(p,a_p) in enumerate(seq.items()):
        if i == 20: break
        print(f"p={p:3d}, a_p={a_p:3d},  legendre(a_p|p)={legendre_symbol(a_p,p)}")
