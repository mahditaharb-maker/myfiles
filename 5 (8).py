#!/usr/bin/env python3
"""
Dyadic‐Rational Approximation of a Constant via Its Power‐Series Expansion.

Given
    x      -- the real constant to approximate,
    term(k)-- the k-th term of a convergent series summing to x,
    N      -- the exponent of 2 in the denominator of the dyadic rational,

this script finds the smallest M so that the tail |x – S_M| < 2**(-N),
where S_M = sum_{k=0}^M term(k), and then returns
    r = floor(x * 2**N) / 2**N.

Output:
    M -- the tail‐order where the approximation first hits tolerance
    r -- the dyadic rational approximation of x with denominator 2**N
"""

import math

def dyadic_approx(x, term, N, max_iter=10_000_00):
    """
    Parameters
    ----------
    x        : float
               the true value of the constant (e.g. math.e or math.pi)

    term     : callable
               term(k) must return the k-th term a_k of the series for x.

    N        : int
               we seek a dyadic of the form floor(x*2^N)/2^N

    max_iter : int
               maximum number of terms to sum before giving up

    Returns
    -------
    M : int
        the smallest index so that |x - sum_{k=0}^M term(k)| < 2**(-N)

    r : float
        the dyadic approximation floor(x*2^N)/2^N
    """
    eps = 2**(-N)
    S   = 0.0

    for M in range(max_iter):
        S += term(M)
        if abs(x - S) < eps:
            r = math.floor(x * 2**N) / (2**N)
            return M, r

    raise ValueError(f"Failed to approximate within 2^-{N} after {max_iter} terms.")

# ---------------- Example usage ----------------

if __name__ == "__main__":
    from math import factorial, e, pi

    # 1) Approximate e = sum_{k=0}^∞ 1/k!
    def e_term(k): 
        return 1.0 / factorial(k)

    M_e, e_dyadic = dyadic_approx(e, e_term, N=16)
    print(f"e ≈ {e_dyadic} with denominator 2^8, reached tolerance at M={M_e}")

    # 2) Approximate pi = 4 * sum_{k=0}^∞ (-1)**k/(2k+1)
    def pi_term(k):
        return 4.0 * ((-1)**k) / (2*k + 1)

    M_pi, pi_dyadic = dyadic_approx(pi, pi_term, N=16)
    print(f"π ≈ {pi_dyadic} with denominator 2^8, reached tolerance at M={M_pi}")
