from sympy import primerange, isprime

def find_safe_primes(limit):
    """
    Return all primes p ≤ limit for which (p-1)/2 is prime.
    These are exactly the counterexamples with no nontrivial (b,c)>1.
    """
    safes = []
    for p in primerange(3, limit + 1):
        m = (p - 1) // 2
        if isprime(m):
            safes.append(p)
    return safes

if __name__ == "__main__":
    LIMIT = 1000
    safe_primes = find_safe_primes(LIMIT)
    print("Safe primes (no nontrivial b,c):", safe_primes)
