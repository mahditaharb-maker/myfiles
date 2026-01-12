import math
import sys

# approximate maximum number of iterations we allow (a·b·c loops ~ p³)
MAX_OPS = 1e7

def compute_safe_limit():
    """
    Compute the largest p such that p³ ≤ MAX_OPS.
    """
    return int(MAX_OPS ** (1/3))

def sieve_primes(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def exists_nontrivial_abc(p):
    target = p - 1
    cycle = p - 1

    for a in range(2, p):
        if math.gcd(a, p) != 1:
            continue
        for b in range(2, cycle):
            bm = b % cycle
            for c in range(2, cycle):
                if pow(a, (bm * (c % cycle)) % cycle, p) == target:
                    return True
    return False

def test_interval(start, end):
    if start < 2:
        start = 2

    safe_limit = compute_safe_limit()
    if end > safe_limit:
        print(f"Complexity overflow: your `end` = {end} exceeds")
        print(f"the safe bound {safe_limit}. Don't exceed this value.")
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
