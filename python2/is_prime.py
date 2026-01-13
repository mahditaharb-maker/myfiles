import random
import sys
import math

def is_prime(n, trials=10):
    """
    Miller–Rabin probabilistic primality test.
    Returns True if n is very likely prime, False if composite.
    """
    if n < 2:
        return False
    # small primes to filter out trivial cases
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    # write n-1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # perform trials
    for _ in range(trials):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def count_fermat_primes_bruteforce(N):
    """
    Brute-force: test every k from 17 to N.
    """
    count = 0
    for k in range(17, N + 1):
        p = pow(2, k) + 1
        if is_prime(p):
            count += 1
    return count

def count_fermat_primes_optimized(N):
    """
    Optimized: only test k that are powers of two,
    because if 2^k + 1 is prime then k must be a power of 2.
    """
    count = 0
    # find the range of i such that 2^i is between 17 and N
    i_min = math.ceil(math.log2(17))
    i_max = math.floor(math.log2(N))
    for i in range(i_min, i_max + 1):
        k = 1 << i   # 2**i
        p = (1 << k) + 1   # 2**k + 1
        if is_prime(p):
            count += 1
    return count

if __name__ == "__main__":
    try:
        N = int(input("Enter N (must be > 16): ").strip())
    except ValueError:
        print("Please enter a valid integer for N.")
        sys.exit(1)

    if N <= 16:
        print("No exponents satisfy 16 < k ≤ N.")
        sys.exit(0)

    # Choose one of the two functions:
    total = count_fermat_primes_bruteforce(N)
    # total = count_fermat_primes_optimized(N)

    print(f"Number of primes of the form 2^k + 1 for 16 < k ≤ {N}: {total}")
