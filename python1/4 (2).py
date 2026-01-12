from fractions import Fraction

# 1) build Q17_nonzero = {k/8: k = -7..-1,1..7}
Q17 = [Fraction(k, 8) for k in range(-8, 9)]
Q17_nonzero = [x for x in Q17 if x != 0]

# 2) build R257_nonzero = all u+v*sqrt(1/8) with u,v != 0
R257_nonzero = [(u, v) for u in Q17_nonzero for v in Q17_nonzero]

# 3) build C65537 elements = zero + all (a,b) with a,b in R257_nonzero
elements = [((0, 0), (0, 0))] + [
    (a, b) for a in R257_nonzero for b in R257_nonzero
]

# 4) table parameters
cols = 256

# 5) print LaTeX tabular header
print(r"\begin{tabular}{" + "|c" * cols + "|}")
print(r"\hline")
print(
    r"\multicolumn{" + str(cols) +
    r"}{|c|}{\bf Elements of \(C_{65537}\)} \\"
)
print(r"\hline")

# 6) the zero element on its own row
print(r"\multicolumn{" + str(cols) + r"}{|c|}{$0$} \\ \hline")

# 7) print all nonzero elements in 256-column rows
for idx, ((u1, v1), (u2, v2)) in enumerate(elements[1:], start=1):
    real_part = (
        f"\\frac{{{u1.numerator}}}{{{u1.denominator}}}"
        f" + \\frac{{{v1.numerator}}}{{{v1.denominator}}}"
        f"\\,\\sqrt{{\\tfrac18}}"
    )
    imag_part = (
        f"\\frac{{{u2.numerator}}}{{{u2.denominator}}}"
        f" + \\frac{{{v2.numerator}}}{{{v2.denominator}}}"
        f"\\,\\sqrt{{\\tfrac18}}"
    )
    entry = f"${real_part} + ({imag_part})\,i$"
    if idx % cols:
        print(entry, end=" & ")
    else:
        print(entry + r" \\ \hline")

# 8) close the environment
print(r"\end{tabular}")
