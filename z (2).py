from math import gcd

# Custom implementation of multiplicative order
def multiplicative_order(a, m):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime")
    n = 1
    power = a % m
    while power != 1:
        power = (power * a) % m
        n += 1
    return n

# Generate small primes using a simple sieve (no sympy)
def get_primes_up_to(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Search for primes p < 50, and powers a = 1 to 3
results = []
for p in get_primes_up_to(50):
    if p == 2:
        continue  # skip 2 since 2 and mod 2^a are tricky
    for a in range(1, 6):
        modulus = p ** a
        try:
            n = multiplicative_order(2, modulus)
            results.append((p, a, n))
        except ValueError:
            continue  # if 2 is not coprime to modulus

# Output the results
for p, a, n in results:
    print(f"p = {p}, a = {a}, n = {n}")
