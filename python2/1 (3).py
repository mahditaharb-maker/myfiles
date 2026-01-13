m = 2
# irreducible polynomial x³ + x + 1 → binary 0b1011
mod_poly = 0b1011  
size     = 1 << m  # 8

# build addition (xor) and multiplication tables
add_tab = [[i ^ j for j in range(size)] for i in range(size)]
mul_tab = []
for i in range(size):
    row = []
    for j in range(size):
        # multiply as polynomials over GF(2) then reduce mod p(x)
        prod = 0
        a, b = i, j
        while b:
            if b & 1:
                prod ^= a
            a <<= 1
            # whenever a hits degree m, reduce
            if a & (1 << m):
                a ^= mod_poly
            b >>= 1
        row.append(prod)
    mul_tab.append(row)

print(f"GF(2^3) has {size} elements")
print(f"5 + 7 = {add_tab[5][7]},  5 * 7 = {mul_tab[5][7]}")
