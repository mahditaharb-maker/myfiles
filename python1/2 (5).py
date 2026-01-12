from fractions import Fraction

# 1) Build Q17 = {k/8 : k = -8 … +8}, split off nonzero units
Q17 = [Fraction(k, 8) for k in range(-8, 9)]
Q17_nonzero = [x for x in Q17 if x != 0]

# 2) Build R257 = {0} ∪ {u + v·√(1/8) : u,v ∈ Q17_nonzero}
elements = [(Fraction(0), Fraction(0))] + [
    (u, v) for u in Q17_nonzero for v in Q17_nonzero
]

# 3) Table parameters
cols = 16

# 4) Print LaTeX tabular header
print(r"\begin{tabular}{" + "|c" * cols + "|}")
print(r"\hline")

# 5) Zero element as a full-width centered row
print(r"\multicolumn{" + str(cols) + r"}{|c|}{$0$} \\ \hline")

# 6) Loop through the 256 nonzero elements in rows of 16
for idx, (u, v) in enumerate(elements[1:], start=1):
    # format the fraction entries
    entry = (
        f"$\\frac{{{u.numerator}}}{{{u.denominator}}}"
        f" + \\frac{{{v.numerator}}}{{{v.denominator}}}\\sqrt{{\\tfrac18}}$"
    )
    # end of column or end of row?
    if idx % cols:
        print(entry, end=" & ")
    else:
        print(entry + r" \\ \hline")

# 7) Close the tabular
print(r"\end{tabular}")
