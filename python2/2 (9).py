import math
from decimal import Decimal, getcontext

# Set precision for large exponentiation
getcontext().prec = 100  # Can increase if needed for larger k

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_dyadic_primes(k):
    try:
        lower = int(Decimal(2) ** k)
        upper = int(Decimal(2) ** (k + 1))
    except OverflowError:
        print("⚠️ k is too large for safe computation.")
        return None

    primes = []
    for n in range(lower + 1, upper):
        if is_prime(n):
            primes.append(n)
    return primes

# Example usage
k = int(input("Enter k (try up to 50 safely): "))
dyadic_primes = count_dyadic_primes(k)
if dyadic_primes is not None:
    print(f"Primes between 2^{k} and 2^{k+1}:")
    print(dyadic_primes)
    print(f"Total count: {len(dyadic_primes)}")
