import math
import matplotlib.pyplot as plt

def sieve_primes(n):
    """Return a boolean list `is_prime[0..n]` marking primality by the Sieve of Eratosthenes."""
    is_prime = [False, False] + [True] * (n - 1)
    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return is_prime

def count_primes_interval(k, is_prime=None):
    """
    Count primes in the interval [2^k, 2^(k+1)].
    If you pass a precomputed `is_prime` sieve up to 2^(k+1), it reuses it.
    """
    a = 2**k
    b = 2**(k + 1)
    if is_prime is None or len(is_prime) <= b:
        is_prime = sieve_primes(b)
    # sum up True values in [a..b]
    return sum(is_prime[a : b + 1])

def plot_f_upto(K):
    """
    Plot f(k) = number of primes in [2^k, 2^(k+1)] for k = 1..K.
    """
    max_b = 2**(K + 1)
    is_prime = sieve_primes(max_b)
    ks = list(range(1, K + 1))
    counts = [count_primes_interval(k, is_prime) for k in ks]

    plt.figure(figsize=(8, 5))
    plt.plot(ks, counts, marker='o', linestyle='-')
    plt.title("Number of Primes in Dyadic Intervals [2^k, 2^{k+1}]")
    plt.xlabel("k")
    plt.ylabel("f(k) = # of primes in [2^k, 2^{k+1}]")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Part 1: single input
    k = int(input("Enter an integer k (e.g. 1,2,3...): "))
    num = count_primes_interval(k)
    print(f"Number of primes between 2^{k} and 2^{k+1}: {num}")

    # Part 2: optional plot
    resp = input("Plot f(k) for k=1..K? (y/n): ").strip().lower()
    if resp == 'y':
        K = int(input("Enter maximum K to plot (e.g. 10 or 15): "))
        plot_f_upto(K)
