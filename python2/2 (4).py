def is_prime(k):
    """Return True if k is a prime number."""
    if k < 2:
        return False
    if k in (2, 3):
        return True
    if k % 2 == 0 or k % 3 == 0:
        return False
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
    return True

def find_special_primes(n):
    """
    Yield all primes p < n such that p^2 - 2*p + 2 is also prime.
    """
    for p in range(2, n):
        if is_prime(p):
            q = p*p - 2*p + 2
            if is_prime(q):
                yield p

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Primes p < {n} with p^2 - 2p + 2 prime:")
    for p in find_special_primes(n):
        print(p)
