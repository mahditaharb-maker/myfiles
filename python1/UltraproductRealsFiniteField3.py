from fractions import Fraction
from sympy import primerange
from math import prod

def distinct_legendre_sequence(rational_str: str, max_prime: int):
    """
    Takes r = 'm/n' in lowest terms, with n < prod(p <= max_prime) 
    and returns the unique symbol-vector (ε_p) for p <= max_prime.
    """
    # parse and reduce
    frac = Fraction(rational_str)
    m, n = frac.numerator, frac.denominator

    # compute P = product of primes <= max_prime
    primes = list(primerange(2, max_prime+1))
    P = prod(primes)

    if n >= P:
        raise ValueError(
            f"Denominator n={n} must be < product of primes P={P} "
            f"for uniqueness."
        )

    seq = {}
    for p in primes:
        # inverse exists since gcd(n,p)=1
        inv_n = pow(n, p-2, p)
        a_p = (m * inv_n) % p

        # Legendre symbol
        ls = pow(a_p, (p-1)//2, p)
        if a_p == 0:
            seq[p] = 0
        else:
            seq[p] =  1 if ls == 1 else -1

    return seq

# Example usage:
if __name__ == "__main__":
    max_p = int(input("Max prime: "))
    rstr  = input("Enter rational m/n (in lowest terms): ")
    seq   = distinct_legendre_sequence(rstr, max_p)
    print(seq)
