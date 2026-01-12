import math
from functools import lru_cache
from typing import Tuple  # ← fixed!

def smallest_prime_divisor(n: int) -> int:
    if n % 2 == 0:
        return 2
    limit = int(math.isqrt(n)) + 1
    for d in range(3, limit, 2):
        if n % d == 0:
            return d
    return n

@lru_cache(maxsize=None)
def prime_factors(n: int) -> Tuple[int, ...]:  # ← use Tuple
    if n == 1:
        return ()
    p = smallest_prime_divisor(n)
    if p == n:
        return (n,)
    rest = prime_factors(n // p)
    return tuple(sorted((p, *rest)))

def verify_unique_factorization(limit: int = 10_000) -> None:
    for n in range(2, limit + 1):
        fac = prime_factors(n)
        prod = 1
        for p in fac:
            prod *= p
        assert prod == n, f"Bad factorization for {n}: {fac}"
        assert fac == prime_factors(n), (
            f"Non-unique factorization for {n}: {fac} vs {prime_factors(n)}"
        )
    print(f"Verified FTA for all n up to {limit:,}!")

if __name__ == "__main__":
    verify_unique_factorization(limit=100_000)
