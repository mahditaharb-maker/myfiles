from decimal import Decimal, getcontext

def dyadic_pi_bits(n_bits):
    """
    Compute first n_bits of dyadic expansion of π's fractional part.
    Returns: (bit list, dyadic value as Decimal)
    """
    getcontext().prec = n_bits + 10  # extra precision to avoid rounding errors
    pi = Decimal('3.1415926535897932384626433832795028841971')  # or use math.pi with lower precision
    frac = pi - int(pi)  # fractional part
    bits = []
    value = Decimal(0)
    for i in range(1, n_bits + 1):
        frac *= 2
        if frac >= 1:
            bits.append(1)
            value += Decimal(1) / (2 ** i)
            frac -= 1
        else:
            bits.append(0)
    return bits, value

def main():
    n_bits = 35  # enough to get 10 correct decimal digits
    bits, val = dyadic_pi_bits(n_bits)
    print(f"Dyadic bits of π fractional part (first {n_bits} bits):")
    print(bits)
    print(f"Dyadic value = {val}")
    print(f"π ≈ {int(Decimal('3')) + val}  (first 10 digits: {str(int(Decimal('3') + val))[:11]})")

if __name__ == "__main__":
    main()
