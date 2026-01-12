# find_Q_min.py
# Given p and n, find minimal Q_min >= p such that the first n dyadic bits
# of fractional part of pi_q = 4 * sum_{k=0}^{q-1} (1/(4k+1)-1/(4k+3))
# are stable for all q in [Q_min, Q_bound].
#
# Returns: (Q_min, bits_tuple, dyadic_value_fraction, pi_Q_fraction)
# If no Q_min found within the search bound, returns None.

from fractions import Fraction
import math

def compute_Q_bound(n):
    """Constructive bound ensuring Leibniz tail < 2^{-n}:
       need N with 4/(2N+1) < 2^{-n} -> N > (4*2^n - 1)/2
       return integer Q_bound = N+1 (safe)."""
    N_required = (4 * (2**n) - 1) / 2.0
    N = math.floor(N_required) + 1
    return N + 1

def dyadic_bits_of_fraction(frac, n):
    """Return (bits_tuple, dyadic_value Fraction) for fractional part of frac."""
    f = frac - (frac.numerator // frac.denominator)  # fractional part in [0,1)
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

def find_Q_min(p, n, max_search=None):
    """
    Main function.
    - p: starting index (int)
    - n: number of dyadic bits (int)
    - max_search: optional cap for Q_bound (int)
    """
    # compute safe bound
    Q_bound = compute_Q_bound(n)
    if max_search is not None:
        Q_bound = min(Q_bound, max_search)
    if Q_bound < p:
        Q_bound = p

    # We'll compute pi_q incrementally to avoid recomputing sums
    # pi_q = 4 * sum_{k=0}^{q-1} (1/(4k+1)-1/(4k+3))
    pi_q = Fraction(0, 1)
    bits_for_q = {}  # q -> bits tuple

    # accumulate sum for q from 1..Q_bound
    # note: for q=0 the sum is 0; we start k=0 and at step q we have sum up to k=q-1
    s = Fraction(0, 1)
    for q in range(1, Q_bound + 1):
        k = q - 1
        s += Fraction(1, 4*k + 1) - Fraction(1, 4*k + 3)
        pi_q = 4 * s
        if q >= p:
            bits, _ = dyadic_bits_of_fraction(pi_q, n)
            bits_for_q[q] = bits

    # search minimal Q such that bits[q] == bits[t] for all t in [Q, Q_bound]
    for Q in range(p, Q_bound + 1):
        target = bits_for_q.get(Q)
        if target is None:
            continue
        stable = True
        for t in range(Q, Q_bound + 1):
            if bits_for_q.get(t) != target:
                stable = False
                break
        if stable:
            # compute pi_Q and dyadic value for return
            # recompute pi_Q precisely (we already have s at end; recompute partial)
            sQ = Fraction(0, 1)
            for k in range(Q):
                sQ += Fraction(1, 4*k + 1) - Fraction(1, 4*k + 3)
            pi_Q = 4 * sQ
            _, dyadic_val = dyadic_bits_of_fraction(pi_Q, n)
            return Q, target, dyadic_val, pi_Q

    return None

# Example usage
if __name__ == "__main__":
    examples = [(797, 790)]
    for p, n in examples:
        res = find_Q_min(p, n, max_search=2000)  # increase max_search if needed
        print("p =", p, "n =", n)
        if res is None:
            print("  No stabilizing Q found within search bound.")
        else:
            Q_min, bits, dyadic_val, pi_Q = res
            print("  Q_min =", Q_min)
            print("  dyadic_{} bits = {}".format(n, bits))
            print("  dyadic value = {}/{} ≈ {:.12f}".format(dyadic_val.numerator, dyadic_val.denominator, float(dyadic_val)))
            print("  pi_Q (exact) = {}/{} ≈ {:.12f}".format(pi_Q.numerator, pi_Q.denominator, float(pi_Q)))
        print()
