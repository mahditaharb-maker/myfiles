def nontrivial_euler_triples(p):
    """
    Return all triples (a,b,c) with:
      - p is prime
      - a in [2..p-1]
      - b>1, c>1 such that b*c = (p-1)//2
      - a^(b*c) ≡ -1 (mod p)

    If p is not prime, behavior is undefined.
    """
    m = (p - 1) // 2
    # find all divisors d of m with 1 < d < m
    divisors = []
    for d in range(2, int(m**0.5) + 1):
        if m % d == 0:
            divisors.append(d)
            if d != m // d:
                divisors.append(m // d)
    # also consider m itself only if m>1, but that gives c=1 → skip
    triples = []

    for b in sorted(divisors):
        c = m // b
        if c <= 1:
            continue
        exp = b * c
        for a in range(2, p):
            if pow(a, exp, p) == p - 1:
                triples.append((a, b, c))

    return triples

# Example usage:
if __name__ == "__main__":
    for p in [31, 29]:
        ts = nontrivial_euler_triples(p)
        print(f"p = {p!r}: ", 
              "found" if ts else "none", 
              f"→ {ts}")
