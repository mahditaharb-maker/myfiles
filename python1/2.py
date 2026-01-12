#!/usr/bin/env python3
import sys
import math
from fractions import Fraction
from typing import List, Tuple, Union

# Safe names for eval’ing expressions like "pi/4" or "e-2"
_ALLOWED_NAMES = {
    'pi': math.pi,
    'e': math.e
}

def parse_x(raw_x: str) -> Fraction:
    """
    Parse raw_x as one of:
      - a rational “a/b”
      - a float literal “0.625”
      - a math expression using pi, e (e.g. “pi/4”, “e-2”)
    Return its Fraction in (0,1), reducing to the fractional part if ≥1.
    """
    # Try rational directly
    try:
        x = Fraction(raw_x)
    except ValueError:
        # Fallback to a restricted eval for pi and e
        try:
            val = eval(raw_x, {"__builtins__": None}, _ALLOWED_NAMES)
            x = Fraction(val).limit_denominator()
        except Exception:
            raise ValueError(f"could not parse x = {raw_x!r}")
    # Reduce to fractional part if >= 1
    if x >= 1:
        x = x - (x.numerator // x.denominator)
    if not (0 < x < 1):
        raise ValueError("x must lie strictly between 0 and 1 after fractional part")
    return x

def binary_exponents(x: Fraction, n: int) -> List[int]:
    """
    Compute up to n greedy-binary exponents m_k for x.
    Stops early if the remainder becomes zero.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    exponents: List[int] = []
    rem = x

    for _ in range(n):
        # If we’ve exactly represented x already, stop
        if rem == 0:
            break

        # inv = 1/rem
        inv = Fraction(1, 1) / rem
        p, q = inv.numerator, inv.denominator

        # Compute floor_log2(inv) exactly using bit lengths:
        # candidate = floor(log2(p/q)) + 1  or 0 adjustments
        bits_p = p.bit_length()
        bits_q = q.bit_length()
        candidate = bits_p - bits_q
        # Adjust down if p < q * 2^candidate
        floor_log2 = candidate - 1 if (p < (q << candidate)) else candidate

        # ceil_log2 = floor_log2 if inv == 2**floor_log2 else floor_log2 + 1
        if p == (q << floor_log2):
            m = floor_log2
        else:
            m = floor_log2 + 1

        # Update remainder: rem = 2**m * rem - 1
        rem = rem * (1 << m) - 1
        exponents.append(m)

    return exponents

def partial_binary_sum(exps: List[int]) -> Fraction:
    """
    Given exponents [m1, m2, …], compute
      sum_{k=1..len(exps)} 2^{-(m1+…+mk)}.
    """
    total = Fraction(0)
    cum = 0
    for m in exps:
        cum += m
        total += Fraction(1, 1 << cum)
    return total

def prompt_inputs() -> Tuple[Fraction, int]:
    """
    Interactively prompt the user for x and n.
    """
    print("This program calculates the greedy binary expansion of x ∈ (0,1).")
    raw_x = input("Enter x (e.g. 0.625, 5/8, pi/4): ").strip()
    raw_n = input("Enter n (positive integer): ").strip()

    x = parse_x(raw_x)
    try:
        n = int(raw_n)
    except ValueError:
        raise ValueError(f"n must be an integer (you gave {raw_n!r})")
    return x, n

def main():
    # Decide between command-line args or interactive prompt
    if len(sys.argv) == 3:
        raw_x, raw_n = sys.argv[1], sys.argv[2]
        try:
            x = parse_x(raw_x)
            n = int(raw_n)
        except Exception as e:
            print("Error:", e)
            sys.exit(1)
    else:
        try:
            x, n = prompt_inputs()
        except Exception as e:
            print("Error:", e)
            sys.exit(1)

    # Compute the exponents
    exps = binary_exponents(x, n)
    # Notify if the expansion terminated early
    if len(exps) < n:
        print(f"\nnote: exact binary expansion terminated after {len(exps)} "
              f"term{'s' if len(exps) != 1 else ''}.")

    # Compute the partial sum (approximation)
    approx = partial_binary_sum(exps)

    # Display results
    print()
    print(f"Input x = {x}   n = {n}")
    print(f"The first {len(exps)} exponents are: {exps}")
    print(f"Binary approximation = {approx}   (≈ {float(approx)})")


if __name__ == "__main__":
    main()
