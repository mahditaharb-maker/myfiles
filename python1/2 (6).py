import math
from typing import Optional

def is_prime(n: int) -> bool:
    """
    Check if n is prime using trial division.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def field_characteristic(order: int) -> Optional[int]:
    """
    Return the characteristic p of the finite field of size `order` (i.e. order = p**k),
    or None if no such field exists.
    """
    if order < 2:
        return None

    # Try prime divisors up to √order
    limit = int(math.isqrt(order))
    for p in range(2, limit + 1):
        if order % p != 0:
            continue
        if not is_prime(p):
            continue

        # count exponent k so that p**k divides order
        k = 0
        m = order
        while m % p == 0:
            m //= p
            k += 1

        # if p**k == order then order is a pure prime power
        if p ** k == order:
            return p
        else:
            return None

    # if no small divisor found, maybe order itself is prime
    if is_prime(order):
        return order

    return None

if __name__ == "__main__":
    try:
        n = int(input("Enter the order n of the finite field: ").strip())
    except ValueError:
        print("Invalid input; please enter an integer ≥ 2.")
    else:
        p = field_characteristic(n)
        if p is None:
            print(f"No finite field of order {n} exists.")
        else:
            print(f"The characteristic of F_{n} is {p}.")
