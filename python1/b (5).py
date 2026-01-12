import math

def dyadic_pi(n):
    """
    Compute the first n dyadic bits of π using its fractional part.
    Returns: (bit list, dyadic value as float)
    """
    pi = math.pi
    frac = pi - int(pi)  # fractional part of π
    bits = []
    value = 0.0
    for i in range(1, n+1):
        frac *= 2
        if frac >= 1:
            bits.append(1)
            value += 1 / (2**i)
            frac -= 1
        else:
            bits.append(0)
    return bits, value

# Example usage
if __name__ == "__main__":
    n = 67  # number of dyadic bits
    bits, val = dyadic_pi(n)

    print(f"Dyadic expansion of π (first {n} bits):")
    print("Bits:", bits)
    print("Binary vector:", "(" + ", ".join(str(b) for b in bits) + ")")
    print("Decimal value of dyadic truncation:", val)
