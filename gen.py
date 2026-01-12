# field_tables_with_labels.py

import itertools
from sympy import Poly, symbols

# ─── Configuration ─────────────────────────────────────────────
p = 2                       # prime characteristic
n = 8                       # extension degree
x = symbols('x')           
modulus_poly = x**2 + x + 1  # irreducible polynomial over GF(p)
modulus = Poly(modulus_poly, x, modulus=p)
# ───────────────────────────────────────────────────────────────

# Generate all field elements as polynomials of degree < n
raw_elements = [
    sum(c * x**i for i, c in enumerate(coeffs))
    for coeffs in itertools.product(range(p), repeat=n)
]

# Map each element to a number label
element_map = {i: raw_elements[i] for i in range(len(raw_elements))}

def ff_add(a, b):
    pa = Poly(a, x, modulus=p)
    pb = Poly(b, x, modulus=p)
    return (pa + pb).set_modulus(p).as_expr()

def ff_mul(a, b):
    pa = Poly(a, x, modulus=p)
    pb = Poly(b, x, modulus=p)
    product = pa * pb
    _, remainder = product.div(modulus)
    return remainder.as_expr()

def find_index(expr):
    """Find the index of a polynomial expression in element_map."""
    for i, poly in element_map.items():
        if Poly(poly, x, modulus=p).as_expr() == Poly(expr, x, modulus=p).as_expr():
            return i
    return None

def write_latex_table(op, func, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\\begin{tabular}{c|" + "c" * len(element_map) + "}\n")
        header = f"{op} & " + " & ".join([f"{i}" for i in element_map]) + " \\\\\n"
        f.write(header)
        f.write("\\midrule\n")
        for i in element_map:
            row = [f"{i}"]
            for j in element_map:
                result = func(element_map[i], element_map[j])
                idx = find_index(result)
                row.append(str(idx) if idx is not None else "?")
            f.write(" & ".join(row) + " \\\\\n")
        f.write("\\end{tabular}\n")

def write_polynomial_list(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\\begin{tabular}{c|l}\n")
        f.write("Number & Polynomial \\\\\n")
        f.write("\\midrule\n")
        for i, poly in element_map.items():
            f.write(f"{i} & ${poly}$ \\\\\n")
        f.write("\\end{tabular}\n")

if __name__ == "__main__":
    write_polynomial_list("poly_list.tex")
    write_latex_table('+', ff_add, "add_table.tex")
    write_latex_table('*', ff_mul, "mul_table.tex")
    print("✓ Generated poly_list.tex, add_table.tex, and mul_table.tex")
