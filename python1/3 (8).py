import math
import matplotlib.pyplot as plt
from typing import Optional

def is_prime(n: int) -> bool:
    """
    Check whether n is prime by trial division up to sqrt(n).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_between_powers(k: int) -> Optional[int]:
    """
    Return the smallest prime n with 2**k < n < 2**(k+1),
    or None if none is found.
    """
    low = 2**k + 1
    high = 2**(k + 1)
    for n in range(low, high):
        if is_prime(n):
            return n
    return None

def main():
    # Read k from user
    k = int(input("Enter k (nonnegative integer): ").strip())
    
    # Find and print a prime between 2^k and 2^(k+1)
    n = find_prime_between_powers(k)
    if n is not None:
        print(f"Prime n such that 2^{k} < n < 2^{k+1} is: {n}")
    else:
        print(f"No prime found between 2^{k} and 2^{k+1}.")

    # Now plot the smallest such prime for all 1 ≤ i ≤ k
    ks = list(range(1, k + 1))
    ns = [find_prime_between_powers(i) for i in ks]

    plt.figure(figsize=(8, 5))
    plt.plot(ks, ns, marker='o', linestyle='-')
    plt.title("Smallest Prime between $2^k$ and $2^{k+1}$")
    plt.xlabel("k")
    plt.ylabel("Prime n")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
