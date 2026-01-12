from math import gcd

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Fast modular exponentiation: 2^n % m
def mod_pow_2(n, m):
    result = 1
    base = 2 % m
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        n //= 2
    return result

# Main logic: Find smallest p and a such that 2^n + 1 ≡ 0 mod (p^a)
def find_smallest_p_a_neg1(n, p_limit=1000000, a_limit=100):
    for p in range(2, p_limit):
        if not is_prime(p):
            continue
        for a in range(1, a_limit + 1):
            modulus = p ** a
            if gcd(2, modulus) != 1:
                continue
            if (mod_pow_2(n, modulus) + 1) % modulus == 0:
                return p, a
    return None, None

# -------- USER INPUT --------
n = int(input("Enter a value for n: "))

p, a = find_smallest_p_a_neg1(n)

if p:
    print(f"Smallest p and a such that 2^{n} ≡ -1 mod (p^{a}) is: p = {p}, a = {a}")
else:
    print("No such prime and exponent found within search limits.")
