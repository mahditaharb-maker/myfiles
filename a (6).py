from fractions import Fraction
import math

# ---------- parameters ----------
p = 65537          # choose your p
n = 300          # number of dyadic bits to compare
q_limit = p + 500  # search primes q in (p, q_limit]

# ---------- small helpers ----------
def is_prime(m):
    if m < 2: return False
    if m % 2 == 0: return m == 2
    r = int(math.isqrt(m))
    for i in range(3, r+1, 2):
        if m % i == 0:
            return False
    return True

def leibniz_sum(q):
    s = Fraction(0,1)
    for k in range(q):
        s += Fraction(1, 4*k+1) - Fraction(1, 4*k+3)
    return s

def fractional_part(frac):
    # frac is a Fraction; return its fractional part in [0,1)
    return frac - (frac.numerator // frac.denominator)

def dyadic_bits(frac, n):
    # return tuple of n bits (b1..bn) for fractional part of frac (truncation)
    f = fractional_part(frac)
    bits = []
    for _ in range(n):
        f = f * 2
        if f >= 1:
            bits.append(1)
            f -= 1
        else:
            bits.append(0)
    return tuple(bits)

# ---------- compute dyadic for T_p ----------
Tp = 4 * leibniz_sum(p)            # exact Fraction
bits_p = dyadic_bits(Tp, n)

print("p =", p, "n =", n)
print("T_p (exact) =", Tp, "≈", float(Tp))
print("dyadic_n(T_p) bits =", bits_p)

# ---------- search for q > p with same dyadic bits ----------
found = []
for q in range(p+1, q_limit+1):
    if not is_prime(q):
        continue
    Tq = 4 * leibniz_sum(q)
    if dyadic_bits(Tq, n) == bits_p:
        found.append((q, Tq, dyadic_bits(Tq, n)))

if found:
    print("\nMatches found (q, dyadic bits):")
    for q, Tq, bits in found:
        print(" q =", q, " T_q ≈", float(Tq), " bits =", bits)
else:
    print("\nNo match for q in (p, {}]. Try increasing q_limit or reducing n.".format(q_limit))
