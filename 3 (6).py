def multiplicative_exponent(n):
    """
    If there is a finite field of order n (i.e. n = p**k), 
    return the exponent of its multiplicative group (= n-1).
    Otherwise return None.
    """
    def is_prime_power(n):
        if n < 2: return False
        for k in range(1, int(n.bit_length())+1):
            p = round(n ** (1.0/k))
            if p**k == n and all(p % d for d in range(2, int(p**0.5)+1)):
                return True
        return False

    return n - 1 if is_prime_power(n) else None

# Examples
print(multiplicative_exponent(8))   # 7, since GF(8)^× is cyclic of order 7
print(multiplicative_exponent(12))  # None, no field of order 12
