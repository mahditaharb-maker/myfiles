def is_quadratic_residue_minus1(p):
    # Check if -1 is a quadratic residue modulo p
    return p % 4 == 1

def find_sqrt_minus1(p):
    if not is_quadratic_residue_minus1(p):
        return None  # No solution if p ≡ 3 mod 4

    # Try all values in Z_p to find a square root of -1
    for x in range(1, p):
        if (x * x) % p == (p - 1):  # Since -1 ≡ p - 1 mod p
            return x
    return None  # Shouldn't happen if p ≡ 1 mod 4

# Example usage
prime = 3
result = find_sqrt_minus1(prime)

if result:
    print(f"The square root of -1 modulo {prime} is {result}")
else:
    print(f"-1 has no square root in Z_{prime}")
