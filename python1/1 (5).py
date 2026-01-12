from fractions import Fraction

# 1) Build Q17 = { k/8 : k = -8 … +8 }
Q17 = [Fraction(k, 8) for k in range(-8, 9)]

# 2) Split off the nonzero elements (16 of them)
Q17_nonzero = [x for x in Q17 if x != 0]

# 3) Build R257 = {0} ∪ { u + v·√(1/8) : u,v ∈ Q17_nonzero }
R257 = [(Fraction(0), Fraction(0))] + [
    (u, v)
    for u in Q17_nonzero
    for v in Q17_nonzero
]

# 4) Pretty‐printer
def show(elem):
    u, v = elem
    if u == 0 and v == 0:
        return "0"
    return f"{u} + {v}·√(1/8)"

# 5) Display all 257 elements
for e in R257:
    print(show(e))
