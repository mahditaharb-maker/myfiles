from decimal import Decimal, getcontext
from fractions import Fraction
import math

def required_bits_for_digits(d, safety=3):
    """
    Estimate number of dyadic bits needed for d correct decimal digits.
    Uses n ≈ ceil(d / log10(2)). Adds a small safety margin.
    """
    log10_2 = math.log10(2)  # ≈ 0.30102999566398114
    n = math.ceil(d / log10_2) + safety
    return n

def compute_dyadic_bits_of_pi(n):
    """
    Compute first n dyadic bits of fractional part of pi using Decimal.
    Returns (bits_tuple, dyadic_fraction (Fraction), dyadic_decimal (Decimal), pi_approx (Decimal))
    """
    # Set decimal precision sufficiently high
    getcontext().prec = n + 20

    # Use a long decimal literal for pi to avoid relying on float rounding
    PI_STR = '3.14159265358979323846264338327950288419716939937510'
    pi_dec = Decimal(PI_STR)

    frac = pi_dec - int(pi_dec)  # fractional part in Decimal
    bits = []
    numerator = 0
    denominator = 1 << n  # 2^n

    for i in range(1, n+1):
        frac *= 2
        if frac >= 1:
            bits.append(1)
            # set corresponding bit in numerator (most-significant-first)
            numerator += 1 << (n - i)
            frac -= 1
        else:
            bits.append(0)

    dyadic_fraction = Fraction(numerator, denominator)
    dyadic_decimal = Decimal(numerator) / Decimal(denominator)
    pi_approx = Decimal(3) + dyadic_decimal

    return tuple(bits), dyadic_fraction, dyadic_decimal, pi_approx

def format_bits(bits):
    return "(" + ", ".join(str(b) for b in bits) + ")"

def main():
    try:
        d = int(input("d  the number of correct digits = "))
        if d < 1:
            print("Please enter a positive integer for d.")
            return
    except Exception:
        print("Invalid input. Please enter an integer.")
        return

    # choose number of bits with small safety margin
    n = required_bits_for_digits(d, safety=3)

    bits, dyadic_frac, dyadic_dec, pi_approx = compute_dyadic_bits_of_pi(n)

    # error bounds
    binary_error = Fraction(1, 1 << n)            # 2^{-n} as Fraction
    decimal_error = Fraction(1, 10**d)            # 10^{-d} as Fraction

    # prepare printable strings
    bits_str = format_bits(bits)
    dyadic_frac_str = f"{dyadic_frac.numerator}/{dyadic_frac.denominator}"
    dyadic_dec_str = f"{dyadic_dec:.20f}".rstrip('0').rstrip('.')
    pi_approx_str = f"{pi_approx:.20f}".rstrip('0').rstrip('.')
    binary_error_tex = rf"$2^{{-{n}}}$"
    decimal_error_tex = rf"$10^{{-{d}}}$"

    # LaTeX table row:
    # (d) & (n) & bits & dyadic fraction & dyadic decimal & pi_approx & binary_error & decimal_error \\
    latex_row = (
        rf"\({d}\) & \({n}\) & {bits_str} & "
        rf"${dyadic_frac_str}\approx {dyadic_dec_str}$ & "
        rf"${pi_approx_str}$ & {binary_error_tex} & {decimal_error_tex} \\\\"
    )

    # Print results
    print("\nResults:")
    print("Requested decimal digits (d):", d)
    print("Number of dyadic bits used (n):", n)
    print("Dyadic bits (fractional part of π):", bits_str)
    print("Dyadic rational:", dyadic_frac_str)
    print("Dyadic decimal value:", dyadic_dec_str)
    print("π approximation (3 + dyadic):", pi_approx_str)
    print("Binary error bound:", f"2^-{n} = {binary_error} (≈ {float(binary_error):.3e})")
    print("Decimal error bound:", f"10^-{d} = {decimal_error} (exact)")

    print("\nLaTeX-ready table row:")
    print(latex_row)
    print("\nPaste the LaTeX row inside a tabular environment (booktabs recommended).")

if __name__ == "__main__":
    main()
