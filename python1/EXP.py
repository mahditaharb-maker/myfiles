def mod_inverse(a, p):
    # Computes modular inverse of a mod p using Fermat's Little Theorem
    return pow(a, p - 2, p)

def sum_inverse_factorials_mod_p(p):
    total = 0
    factorial = 1
    for k in range(p):
        if k > 0:
            factorial = (factorial * k) % p
        inverse = mod_inverse(factorial, p)
        total = (total + inverse) % p
    return total

# Example usage:
prime = 13
print(sum_inverse_factorials_mod_p(prime))
