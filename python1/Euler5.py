from sympy import isprime, primerange
from itertools import product

def find_max_prime(limit=1000):
    max_p = 0
    for p in reversed(list(primerange(3, limit))):  # Start from higher primes
        for a, b, c in product(range(1, p), repeat=3):
            if pow(a, b * c, p) == p - 1:  # Since -1 mod p ≡ p - 1
                max_p = p
                print(f"Found: a={a}, b={b}, c={c}, p={p}")
                return p
    return None

# Run it
#result = find_max_prime(2700) a=2, b=1, c=1349, p=2699
result = find_max_prime(2700)
print(f"Maximum prime p: {result}")
