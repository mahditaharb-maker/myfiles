# find_minimal_Q.py
# Find minimal Q >= p such that dyadic_n(pi_q) stabilizes for q in [Q, Q_bound]
# where pi_q = 4 * sum_{k=0}^{q-1} (1/(4k+1) - 1/(4k+3))
# Uses Fraction for exact arithmetic.

from fractions import Fraction
import math
import sys

def pi_q(q):
    """Exact rational pi_q = 4 * sum_{k=0}^{q-1} (1/(4k+1) - 1/(4k+3))."""
    s = Fraction(0, 1)
    for k in range(q):
        s += Fraction(1, 4*k+1) - Fraction(1, 4*k+3)
    return 4 * s

def fractional_part(frac):
    """Fraction in [0,1) representing fractional part."""
    return frac - (frac.numerator // frac.denominator)

def dyadic_bits_of_fraction(frac, n):
    """Return tuple of n bits (b1..bn) and Fraction dyadic value."""
    f = fractional_part(frac)
    bits = []
    val = Fraction(0, 1)
    for i in range(1, n+1):
        f *= 2
        if f >= 1:
            bits.append(1)
            val += Fraction(1, 2**i)
            f -= 1
        else:
            bits.append(0)
    return tuple(bits), val

def compute_Q_bound(n):
    """
    Constructive bound Q_bound ensuring tail < 2^{-n}:
    need N with 4/(2N+1) < 2^{-n} -> N > (4*2^n - 1)/2
    We return Q_bound = ceil(N) + 1 (safe).
    """
    N_required = (4 * (2**n) - 1) / 2.0
    N = math.floor(N_required) + 1
    return N + 1  # choose Q_bound = N+1 for safety

def find_minimal_Q(p, n, max_search=None):
    """
    Find minimal Q >= p such that dyadic_n(pi_q) is constant for q in [Q, Q_bound].
    Returns (Q_min, Q_bound, bits_at_Q).
    If no Q found before max_search (if provided) or before Q_bound, returns None.
    """
    Q_bound = compute_Q_bound(n)
    if max_search is not None:
        Q_bound = min(Q_bound, max_search)

    # Precompute dyadic bits for q = p..Q_bound
    bits_dict = {}
    for q in range(p, Q_bound+1):
        bits, _ = dyadic_bits_of_fraction(pi_q(q), n)
        bits_dict[q] = bits

    # Find minimal Q such that bits[q] equal for all q in [Q, Q_bound]
    for Q in range(p, Q_bound+1):
        target = bits_dict[Q]
        stable = True
        for q in range(Q, Q_bound+1):
            if bits_dict[q] != target:
                stable = False
                break
        if stable:
            return Q, Q_bound, target

    # If not found
    return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python find_minimal_Q.py p n [max_search]")
        print("Example: python find_minimal_Q.py 23 8 10000")
        return

    p = int(sys.argv[1])
    n = int(sys.argv[2])
    max_search = int(sys.argv[3]) if len(sys.argv) >= 4 else None

    print(f"Searching minimal Q >= {p} stabilizing first {n} dyadic bits...")
    result = find_minimal_Q(p, n, max_search)
    if result is None:
        print("No stabilizing Q found within the search bound. Try increasing max_search.")
        return

    Q_min, Q_bound, bits = result
    # compute dyadic value and representative pi values
    bits_val = sum(b * Fraction(1, 2**(i+1)) for i, b in enumerate(bits))
    pi_Q = pi_q(Q_min)
    print(f"Found Q_min = {Q_min}, stability guaranteed up to Q_bound = {Q_bound}.")
    print(f"dyadic_{n} bits = {bits}")
    print(f"dyadic value = {bits_val} ≈ {float(bits_val)}")
    print(f"pi_Q (exact) = {pi_Q}")
    print(f"pi_Q (decimal) ≈ {float(pi_Q)}")

if __name__ == "__main__":
    main()
