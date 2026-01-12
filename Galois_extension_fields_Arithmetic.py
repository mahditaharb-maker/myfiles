#!/usr/bin/env python3
"""
Galois Field (2^m) addition and multiplication tables.
This script builds full addition and multiplication tables
for GF(2^m) using bitwise XOR for addition and
polynomial reduction for multiplication.
"""

# irreducible polynomials for GF(2^m), keyed by m
IRREDUCIBLE_POLY = {
    1:  0b11,      # x + 1
    4:  0b1_0011,  # x^4 + x + 1
    8:  0x11B,     # x^8 + x^4 + x^3 + x + 1
    16: 0x1_100B,  # x^16 + x^12 + x^3 + x + 1
}

def gf_add(a: int, b: int) -> int:
    """Addition in GF(2^m) is bitwise XOR."""
    return a ^ b

def gf_multiply(a: int, b: int, mod_poly: int, m: int) -> int:
    """
    Multiply two elements in GF(2^m).
    Uses shift-and-add plus reduction by the irreducible polynomial.
    """
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        # if a has grown to degree m, reduce it
        if a & (1 << m):
            a ^= mod_poly
    return result

def build_tables(m: int):
    """
    Builds and returns two 2D lists:
      - add_table[i][j] = i + j in GF(2^m)
      - mul_table[i][j] = i * j in GF(2^m)
    """
    size = 1 << m
    mod_poly = IRREDUCIBLE_POLY[m]

    # build addition table
    add_table = [
        [gf_add(i, j) for j in range(size)]
        for i in range(size)
    ]

    # build multiplication table
    mul_table = [
        [gf_multiply(i, j, mod_poly, m) for j in range(size)]
        for i in range(size)
    ]

    return add_table, mul_table

def main():
    # choose the extension degrees you care about
    for m in [1, 4, 8, 16]:
        add_tab, mul_tab = build_tables(m)
        size = 1 << m

        # guard the example so we never index out of bounds
        if size > 8:
            a, b = 5, 7
        else:
            a, b = 0, 1

        print(f"=== GF(2^{m}) tables ===")
        print(f"Size: {size} elements. Example: {a}+{b} = {add_tab[a][b]}, "
              f"{a}*{b} = {mul_tab[a][b]}\n")

if __name__ == "__main__":
    main()
