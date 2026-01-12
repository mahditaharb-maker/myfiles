#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal, getcontext
from fractions import Fraction
import math

# High precision for greedy expansions
getcontext().prec = 200

# High-precision constants for greedy (not IEEE) computations
PI_DEC = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899')
E_DEC  = Decimal('2.71828182845904523536028747135266249775724709369995957496696762772407663035354759')

def int_to_bin(n: int) -> str:
    """Binary without 0b prefix."""
    return format(n, 'b')

def greedy_fixed_binary_decimal(x: Decimal, frac_bits: int) -> str:
    """
    Binary greedy expansion in fixed-point form (integer_part.frac_bits),
    computed from Decimal with high precision.
    """
    # Integer part
    int_part = int(x)  # safe with positive inputs here
    frac = x - Decimal(int_part)

    # Fractional bits via greedy subtraction (equivalently multiply-by-2 method)
    bits = []
    for _ in range(frac_bits):
        frac *= 2
        if frac >= 1:
            bits.append('1')
            frac -= 1
        else:
            bits.append('0')

    return f"{int_to_bin(int_part)}.{''.join(bits)}"

def float_to_exact_fraction(x: float) -> Fraction:
    """
    Exact rational for a binary64 float (no rounding loss).
    Fraction.from_float already does this exactly.
    """
    return Fraction.from_float(x)

def fixed_binary_from_fraction(fr: Fraction, frac_bits: int) -> str:
    """
    Render exact binary of a rational number as fixed-point with frac_bits bits.
    Pads with zeros if expansion terminates early (denominator power-of-two).
    """
    if fr < 0:
        raise ValueError("Negative values not supported in this formatter for this use case.")

    n, d = fr.numerator, fr.denominator
    int_part = n // d
    rem = n - int_part * d

    # Integer bits
    int_bits = int_to_bin(int_part)

    # Fractional bits
    bits = []
    for _ in range(frac_bits):
        rem *= 2
        if rem >= d:
            bits.append('1')
            rem -= d
        else:
            bits.append('0')

    return f"{int_bits}.{''.join(bits)}"

def ieee754_double_fixed_binary(x: float, frac_bits: int = 53) -> str:
    """
    Fixed-point binary string of the exact IEEE 754 double value of x,
    showing exactly frac_bits bits after the point (padded if necessary).
    """
    fr = float_to_exact_fraction(x)  # exact value of the binary64 float
    return fixed_binary_from_fraction(fr, frac_bits)

def main(frac_bits: int = 53):
    # Greedy expansions (Decimal high precision)
    greedy_pi   = greedy_fixed_binary_decimal(PI_DEC, frac_bits)
    greedy_e    = greedy_fixed_binary_decimal(E_DEC, frac_bits)
    greedy_inv_pi = greedy_fixed_binary_decimal(Decimal(1) / PI_DEC, frac_bits)
    greedy_inv_e  = greedy_fixed_binary_decimal(Decimal(1) / E_DEC, frac_bits)

    # IEEE 754 double (binary64) exact values rendered in fixed-point
    ieee_pi     = ieee754_double_fixed_binary(math.pi, frac_bits)
    ieee_e      = ieee754_double_fixed_binary(math.e, frac_bits)
    ieee_inv_pi = ieee754_double_fixed_binary(1.0 / math.pi, frac_bits)
    ieee_inv_e  = ieee754_double_fixed_binary(1.0 / math.e, frac_bits)

    # Print results
    print(f"Greedy π     : {greedy_pi}")
    print(f"IEEE64 π     : {ieee_pi}")
    print(f"Greedy e     : {greedy_e}")
    print(f"IEEE64 e     : {ieee_e}")
    print(f"Greedy 1/π   : {greedy_inv_pi}")
    print(f"IEEE64 1/π   : {ieee_inv_pi}")
    print(f"Greedy 1/e   : {greedy_inv_e}")
    print(f"IEEE64 1/e   : {ieee_inv_e}")

    # Optional: emit LaTeX table rows
    def tex_row(name, greedy, ieee):
        return f"${name}$ & \\texttt{{{greedy}}} & \\texttt{{{ieee}}} \\\\"
    print("\n% LaTeX table rows:")
    print(tex_row("\\pi", greedy_pi, ieee_pi))
    print(tex_row("e", greedy_e, ieee_e))
    print(tex_row("1/\\pi", greedy_inv_pi, ieee_inv_pi))
    print(tex_row("1/e", greedy_inv_e, ieee_inv_e))

if __name__ == "__main__":
    main(frac_bits=53)
