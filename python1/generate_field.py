# generate_field.py

import itertools
from sympy import Poly, symbols

# parameters: prime p, extension degree n, irreducible modulus over GF(p)
p = 2
n = 4
x = symbols('x')
modulus_poly = x**2 + x + 1
modulus = Poly(modulus_poly, x, modulus=p)

# enumerate all field elements as polynomials of degree < n
elements = [
    sum(coeff * x**i for i, coeff in enumerate(coeffs))
    for coeffs in itertools.product(range(p), repeat=n)
]

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

def write_latex_table(op, func, filename):
    """Emit a LaTeX tabular for '+' or '*' using func(a,b)."""
    with open(filename, 'w', encoding='utf-8') as f:
        # header
        f.write("\\begin{tabular}{c|" + "c" * len(elements) + "}\n")
        f.write(f"{op} & " + " & ".join(f"${e}$" for e in elements) + " \\\\\n")
        f.write("\\midrule\n")
        # rows
        for a in elements:
            row = [f"${a}$"] + [f"${func(a, b)}$" for b in elements]
            f.write(" & ".join(row) + " \\\\\n")
        f.write("\\end{tabular}\n")

if __name__ == "__main__":
    write_latex_table('+', ff_add, "add_table.tex")
    write_latex_table('*', ff_mul, "mul_table.tex")
    print("Generated add_table.tex and mul_table.tex")
