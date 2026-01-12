from sympy import primerange, factorint
from math import gcd

def multiplicative_order(a, p):
    """
    Smallest d>0 such that a^d ≡ 1 (mod p), assuming gcd(a,p)=1.
    We factor p-1 and strip off divisors.
    """
    if gcd(a, p) != 1:
        return None
    d = p - 1
    for q in factorint(d):
        while d % q == 0 and pow(a, d // q, p) == 1:
            d //= q
    return d

def has_neg_one_power(p):
    """
    Return True if ∃ a,b,c ∈ ℕ with a^(b·c) ≡ −1 (mod p).
    For p=2 we know 1^1 ≡ 1 ≡ −1 (mod 2), so return True.
    Otherwise check for any 'a' whose multiplicative order is even.
    """
    if p == 2:
        return True

    for a in range(1, p):
        ord_a = multiplicative_order(a, p)
        if ord_a and ord_a % 2 == 0:
            # then a^(ord_a/2) ≡ -1 mod p
            return True

    return False

def max_k_with_property(limit):
    """
    Return the largest k ≤ limit such that for every prime p < k,
    ∃ a,b,c ∈ ℕ with a^(b*c) ≡ −1 (mod p).
    """
    primes = list(primerange(2, limit+1))
    good_up_to = 1

    for k in range(2, limit+1):
        if all(has_neg_one_power(p) for p in primes if p < k):
            good_up_to = k
        else:
            break

    return good_up_to

if __name__ == "__main__":
    LIMIT = 50
    print("Maximum k with the property (up to 50):", max_k_with_property(LIMIT))
