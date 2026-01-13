import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0:
            return False
    return True

def find_pythagorean_prime_triples(limit):
    triples = []
    for p in range(5, limit + 1):
        if not is_prime(p):
            continue
        p_sq = p * p
        for a in range(1, p):
            b_sq = p_sq - a*a
            b = int(math.isqrt(b_sq))
            if b < a:  # avoid duplicates like (3,4,5) vs (4,3,5)
                continue
            if b*b == b_sq:
                triples.append((a, b, p))
    return triples

triples = find_pythagorean_prime_triples(1000)
for trip in triples:
    print(trip)
