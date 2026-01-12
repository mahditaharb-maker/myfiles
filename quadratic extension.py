#!/usr/bin/env python3
"""
Generate the quadratic extension GF(p^2) = GF(p)[i]/(i^2 + 1)
for a prime p ≡ 3 mod 4, and emit TeX tables for addition
and multiplication in that field.
"""

import sys
from sympy import isprime

def repr_elem(elem):
    """
    Return a TeX‐friendly string for the field element a + b i.
    """
    a, b = elem
    if b == 0:
        return f"{a}"
    if a == 0:
        return "i" if b == 1 else f"{b}i"
    if b == 1:
        return f"{a} + i"
    return f"{a} + {b}i"

def generate_tables(p):
    # 1) Check primality
    if not isprime(p):
        sys.exit(f"Error: {p} is not prime.")
    # 2) Check that –1 is a nonresidue, i.e. p ≡ 3 mod 4
    if p % 4 != 3:
        sys.exit(f"Error: –1 is a square in GF({p}); choose p ≡ 3 mod 4.")

    # 3) Build the list of field elements (a,b) for a+bi
    elements = [(a, b) for a in range(p) for b in range(p)]
    names = [repr_elem(e) for e in elements]

    # 4) Precompute addition and multiplication tables
    #    i^2 = -1 ≡ p−1 modulo p
    add_table = [
        [((a1 + a2) % p, (b1 + b2) % p)
         for (a2, b2) in elements]
        for (a1, b1) in elements
    ]
    mul_table = [
        [(
            (a1 * a2 + (p - 1) * b1 * b2) % p,
            (a1 * b2 + a2 * b1) % p
         )
         for (a2, b2) in elements]
        for (a1, b1) in elements
    ]

    # 5) Emit TeX for the addition table
    print(r"\begin{table}[ht]")
    print(r"  \centering")
    print(f"  \\caption{{Addition in $\\GF({p}^2)$}}")
    print(r"  \begin{tabular}{r|" + "c" * len(elements) + "}")
    # header row
    header = " & ".join(f"${n}$" for n in names)
    print(r"    $+$ & " + header + r" \\ \hline")
    # data rows
    for i, row_name in enumerate(names):
        row_entries = " & ".join(f"${repr_elem(add_table[i][j])}$"
                                 for j in range(len(elements)))
        print(f"    ${row_name}$ & {row_entries} \\\\")
    print(r"  \end{tabular}")
    print(r"\end{table}")
    print()  # blank line between tables

    # 6) Emit TeX for the multiplication table
    print(r"\begin{table}[ht]")
    print(r"  \centering")
    print(f"  \\caption{{Multiplication in $\\GF({p}^2)$}}")
    print(r"  \begin{tabular}{r|" + "c" * len(elements) + "}")
    # header row
    print(r"    $\times$ & " + header + r" \\ \hline")
    # data rows
    for i, row_name in enumerate(names):
        row_entries = " & ".join(f"${repr_elem(mul_table[i][j])}$"
                                 for j in range(len(elements)))
        print(f"    ${row_name}$ & {row_entries} \\\\")
    print(r"  \end{tabular}")
    print(r"\end{table}")


if __name__ == "__main__":
    try:
        p = int(input("Enter an odd prime p ≡ 3 mod 4: ").strip())
    except ValueError:
        sys.exit("Error: please enter a valid integer.")
    generate_tables(p)
