from fractions import Fraction

# 1) Build Q17 = {k/8 : k = -8 … +8}, split off nonzero units
Q17 = [Fraction(k, 8) for k in range(-8, 9)]
Q17_nonzero = [x for x in Q17 if x != 0]

# 2) Build R257 = [(0,0)] + all (u,v) with u,v≠0
elements = [(Fraction(0), Fraction(0))] + [
    (u, v) for u in Q17_nonzero for v in Q17_nonzero
]

# 3) Table parameters
cols = 16

# 4) Print the tabular environment header
print(r"\begin{tabular}{" + "|c" * cols + "|}")
print(r"\hline")
print(r"\multicolumn{" + str(cols) + r"}{|c|}{\bf Elements of \(R_{257}\)} \\")
print(r"\hline")

# 5) Row 1: the zero element
print(r"\multicolumn{" + str(cols) + r"}{|c|}{$0$} \\ \hline")

# 6) The 256 non-zero elements in rows of 16
for idx, (u, v) in enumerate(elements[1:], start=1):
    entry = (
        f"$\\frac{{{u.numerator}}}{{{u.denominator}}}"
        f" + \\frac{{{v.numerator}}}{{{v.denominator}}}\\,\\sqrt{{\\tfrac18}}$"
    )
    # end-of-row when idx%cols==0
    if idx % cols:
        print(entry, end=" & ")
    else:
        print(entry + r" \\ \hline")

# 7) Close the tabular
print(r"\end{tabular}")
