#!/usr/bin/env python3
from fractions import Fraction

def compute_Tp(p):
    """
    Compute Tp = 4 * sum_{k=0}^{v} (-1)^k / (2k+1),
    where v = (p - 3) // 2 (term count v+1).
    """
    v = (p - 3) // 2
    s = Fraction(0, 1)
    for k in range(v + 1):
        s += Fraction((-1) ** k, 2 * k + 1)
    return 4 * s

def fractional_part(frac):
    """Return fractional part of a Fraction in [0,1)."""
    return frac - (frac.numerator // frac.denominator)

def dyadic_bits_of_fraction(frac, n):
    """
    Return (bits, dyadic_fraction) where:
      - bits is a list of n bits (0/1) for the fractional part of frac
      - dyadic_fraction is a Fraction representing sum_{i=1..n} b_i / 2^i
    """
    f = fractional_part(frac)
    bits = []
    val = Fraction(0, 1)
    for i in range(1, n + 1):
        f *= 2
        if f >= 1:
            bits.append(1)
            val += Fraction(1, 2 ** i)
            f -= 1
        else:
            bits.append(0)
    return bits, val

def format_row(p, n, Qmin):
    Tp = compute_Tp(p)
    bits, dyadic_frac = dyadic_bits_of_fraction(Tp, n)
    dyadic_dec = float(dyadic_frac)
    # pi_full = integer part of Tp + 4 * dyadic_frac (gives 3.x when appropriate)
    pi_full = float((Tp.numerator // Tp.denominator) + 4 * dyadic_frac)
    binary_err = f"2^-{n}"
    bit_str = "(" + ",".join(str(b) for b in bits) + ")"
    frac_str = f"{dyadic_frac.numerator}/{dyadic_frac.denominator}"
    print(f"{p:<3} {n:<3} {Qmin:<6} {bit_str:<40} {frac_str:<22} {dyadic_dec:<18.15f} {pi_full:<18.12f} {binary_err}")

def main():
    print(f"{'p':<3} {'n':<3} {'Qmin':<6} {'dyadic bits':<40} {'dyadic (frac)':<22} {'dyadic (dec)':<18} {'pi_Q (approx)':<18} {'binary err'}")
    print("-" * 130)
    format_row(23, 8, 104)
    format_row(29, 8, 104)
    format_row(31, 10, 173)
    format_row(3, 35, "-")
    format_row(3, 36, "-")

if __name__ == "__main__":
    main()
