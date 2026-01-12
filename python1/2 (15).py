from decimal import Decimal, getcontext

def required_bits_for_digits(d):
    """
    Estimate number of dyadic bits needed to get d correct decimal digits.
    Rule of thumb: log10(2) ≈ 0.301 → need about ceil(d / 0.301) bits.
    """
    return int(d / 0.30103) + 5  # add buffer for safety

def dyadic_pi_bits(digits):
    """
    Compute dyadic expansion of π to enough bits to get 'digits' correct decimal digits.
    Returns: (bit list, Fraction as string, Decimal value)
    """
    n_bits = required_bits_for_digits(digits)
    getcontext().prec = n_bits + 10  # extra precision
    pi = Decimal('3.14159265358979323846264338327950288419716939937510')
    frac = pi - int(pi)  # fractional part
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

# Example usage
if __name__ == "__main__":
    digits = 10  # number of correct decimal digits desired
    bits, frac_str, dec_val = dyadic_pi_bits(digits)
    print(f"Requested digits: {digits}")
    print(f"Dyadic bits (π fractional part): {bits}")
    print(f"Dyadic rational: {frac_str}")
    print(f"Decimal value: {dec_val}")
    print(f"π ≈ {Decimal(3) + dec_val}  (first {digits} digits: {str(Decimal(3) + dec_val)[:digits+2]})")
