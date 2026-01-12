# compute_dyadic_table.py
# Compute minimal Q_min that stabilizes dyadic_n(pi_q) for given (p,n) pairs,
# then print LaTeX table rows: p, n, Q_min, dyadic bits, dyadic value (frac & dec), pi_Q (frac & dec).

from fractions import Fraction
import math

# ---------- parameters ----------
pairs = [
    (97, 32),
    (101, 34),
    (107, 36),
    (113, 38),
    (127, 40),
    (131, 42),
    (137, 44),
]
# safe bound multiplier: the theoretical bound grows ~2^n, so choose a practical Q_bound factor
DEFAULT_Q_BOUND = 100  # increase if needed; may need much larger for big n

# ---------- helpers ----------
def compute_T_q(q):
    """Compute T_q = 4 * sum_{k=0}^{q-1} (1/(4k+1) - 1/(4k+3)) exactly."""
    s = Fraction(0, 1)
    for k in range(q):
        s += Fraction(1, 4*k + 1) - Fraction(1, 4*k + 3)
    return 4 * s

def fractional_part(frac):
    return frac - (frac.numerator // frac.denominator)

def dyadic_bits_and_value(frac, n):
    """Return (bits_tuple, dyadic_value Fraction) for fractional part of frac."""
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

def compute_theoretical_Q_bound(n):
    """
    Conservative theoretical bound: find N with 4/(2N+1) < 2^{-n}.
    Return Q_bound = ceil(N) + 1.
    """
    N_required = (4 * (2**n) - 1) / 2.0
    N = math.floor(N_required) + 1
    return N + 1

# ---------- main search function ----------
def find_minimal_Q_for_pair(p, n, Q_limit):
    """
    Search q from p..Q_limit and detect earliest Q_min such that bits[q] == bits[t]
    for all t in [Q_min, Q_limit]. If none found, return None.
    """
    bits_for_q = {}
    # compute T_q incrementally for efficiency
    s = Fraction(0, 1)
    # We'll compute up to Q_limit
    for q in range(1, Q_limit + 1):
        k = q - 1
        s += Fraction(1, 4*k + 1) - Fraction(1, 4*k + 3)
        Tq = 4 * s
        if q >= p:
            bits, val = dyadic_bits_and_value(Tq, n)
            bits_for_q[q] = (bits, val, Tq)

    # search minimal Q_min
    for Q in range(p, Q_limit + 1):
        target_bits = bits_for_q[Q][0]
        stable = True
        for t in range(Q, Q_limit + 1):
            if bits_for_q[t][0] != target_bits:
                stable = False
                break
        if stable:
            bits, val, TQ = bits_for_q[Q]
            return Q, bits, val, TQ
    return None

# ---------- run for all pairs and print LaTeX rows ----------
if __name__ == "__main__":
    print("% LaTeX table rows: p & n & Q_min & dyadic_bits & dyadic_value & pi_Q \\\\")
    for p, n in pairs:
        # choose Q_limit: min of theory and DEFAULT_Q_BOUND to keep runtime manageable;
        # for very large n the theory bound is enormous, so allow DEFAULT_Q_BOUND cap.
        theory_bound = compute_theoretical_Q_bound(n)
        Q_limit = min(theory_bound, DEFAULT_Q_BOUND)
        # If theory_bound is smaller than reasonable, use it; otherwise use DEFAULT_Q_BOUND and warn
        use_note = ""
        if theory_bound > DEFAULT_Q_BOUND:
            use_note = f" (search capped at {DEFAULT_Q_BOUND}, theoretical bound {theory_bound})"
        result = find_minimal_Q_for_pair(p, n, Q_limit)
        if result is None:
            print(f"% p={p}, n={n}: no stabilizing Q found up to Q_limit={Q_limit}{use_note}")
            # print an empty LaTeX row you can fill later
            print(f"{p} & {n} & - & - & - & - \\\\")
            continue
        Q_min, bits, dyadic_val, pi_Q = result
        # format bits as (b1,b2,...)
        bits_str = "(" + ", ".join(str(b) for b in bits) + ")"
        # dyadic value fraction and decimal (with 15 digits)
        dy_frac = f"{dyadic_val.numerator}/{dyadic_val.denominator}"
        dy_dec = f"{float(dyadic_val):.15f}"
        # pi_Q fraction and decimal
        pi_frac = f"{pi_Q.numerator}/{pi_Q.denominator}"
        pi_dec = f"{float(pi_Q):.15f}"
        # print LaTeX row
        print(f"{p} & {n} & {Q_min} & {bits_str} & ${dy_frac}\\approx {dy_dec}$ & ${pi_frac}\\approx {pi_dec}$ \\\\")
