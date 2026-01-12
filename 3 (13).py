from decimal import Decimal, getcontext

def required_bits_for_digits(d):
    """Estimate number of dyadic bits needed for d correct decimal digits."""
    return int(d / 0.30103) + 5  # log10(2) ≈ 0.30103

def dyadic_pi_bits(digits):
    """Compute dyadic expansion of π's fractional part for given digits."""
    n_bits = required_bits_for_digits(digits)
    getcontext().prec = n_bits + 10  # extra precision
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    frac = pi - int(pi)
    bits = []
    numerator = 0
    denominator = 1 << n_bits  # 2^n_bits
    for i in range(1, n_bits + 1):
        frac *= 2
        if frac >= 1:
            bits.append(1)
            numerator += 1 << (n_bits - i)
            frac -= 1
        else:
            bits.append(0)
    dyadic_decimal = Decimal(numerator) / Decimal(denominator)
    return bits, f"{numerator}/{denominator}", dyadic_decimal

# Interactive prompt
if __name__ == "__main__":
    try:
        d = int(input("d  the number of correct digits = "))
        bits, frac_str, dec_val = dyadic_pi_bits(d)
        pi_approx = Decimal(3) + dec_val
        print("\nDyadic bits of π fractional part:")
        print(bits)
        print(f"Dyadic rational: {frac_str}")
        print(f"Decimal value: {dec_val}")
        print(f"π ≈ {pi_approx}  (first {d} digits: {str(pi_approx)[:d+2]})")
    except Exception as e:
        print("Invalid input. Please enter an integer.")
