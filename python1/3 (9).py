import math
import sys

# Maximum allowed prime bound to avoid O(p^3) blow-up
MAX_LIMIT = 500

def sieve_primes(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def exists_nontrivial_abc(p):
    target = p - 1
    cycle  = p - 1

    for a in range(2, p):
        if math.gcd(a, p) != 1:
            continue
        for b in range(2, cycle):
            bm = b % cycle
            for c in range(2, cycle):
                e = (bm * (c % cycle)) % cycle
                if pow(a, e, p) == target:
                    return True
    return False

def test_interval(start, end):
    if start < 2:
        start = 2

    # Warn / abort if user requested too large an interval
    if end > MAX_LIMIT:
        print(f"Error: end={end} exceeds complexity‐safe limit of {MAX_LIMIT}.")
        print("Please choose a smaller end value to avoid computational overflow.")
        return False

    primes = sieve_primes(end + 1)
    primes = [p for p in primes if p >= start]

    for p in primes:
        if p < 3 or not exists_nontrivial_abc(p):
            return False
    return True

if __name__ == "__main__":
    try:
        start, end = map(int, input("Enter start and end primes: ").split())
    except ValueError:
        print("Invalid input. Please enter two integers separated by space.")
        sys.exit(1)

    result = test_interval(start, end)
    print(result)
