from fractions import Fraction
import math

def leibniz_polyserie(p):
    """Compute π_p = 4 * sum_{k=0}^{p-1} (1/(4k+1) - 1/(4k+3)) as a Fraction."""
    s = Fraction(0, 1)
    for k in range(p):
        s += Fraction(1, 4*k + 1) - Fraction(1, 4*k + 3)
    return 4 * s  # polyserie version

def dyadic_bits(frac, n):
    """Return first n dyadic bits of fractional part of frac (truncation)."""
    f = frac - frac.numerator // frac.denominator  # fractional part
    bits = []
    value = Fraction(0, 1)
    for i in range(1, n+1):
        f *= 2
        if f >= 1:
            bits.append(1)
            value += Fraction(1, 2**i)
            f -= 1
        else:
            bits.append(0)
    return bits, value

# Example usage
if __name__ == "__main__":
    p = 79769       # prime index for polyserie
    n = 50000       # number of dyadic bits

    pi_p = leibniz_polyserie(p)
    bits, val = dyadic_bits(pi_p, n)

    print(f"Modular polyserie π_p for p = {p}:")
    print("π_p =", pi_p, "≈", float(pi_p))
    print(f"Dyadic_{n} bits of fractional part:", bits)
    print("Dyadic value =", val, "≈", float(val))
