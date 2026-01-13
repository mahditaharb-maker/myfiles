import math

def sieve_primes(limit):
    """
    Return a list of all primes less than `limit`
    using the Sieve of Eratosthenes.
    """
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def exists_nontrivial_abc(p):
    """
    Return True if there exist a,b,c > 1 satisfying
    a^(b*c) ≡ -1 (mod p), else False.
    """
    target = p - 1        # -1 mod p
    cycle  = p - 1        # exponent cycle by Fermat

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
    """
    Check every prime p in [start, end] for a nontrivial (a,b,c).
    Returns True if all primes in the interval pass, False otherwise.
    """
    if start < 2:
        start = 2
    primes = sieve_primes(end + 1)
    primes = [p for p in primes if p >= start]

    for p in primes:
        # skip p < 3 since no a>1 invertible class
        if p < 3 or not exists_nontrivial_abc(p):
            return False

    return True

if __name__ == "__main__":
    # Read interval bounds from user
    start, end = map(int, input("Enter start and end primes: ").split())
    result = test_interval(start, end)
    print(result)
 # 10 1000