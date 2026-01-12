import math

def find_all_triples(p):
    """
    Return a list of all nontrivial (a, b, c) with a, b, c > 1
    such that a^(b·c) ≡ -1 (mod p).
    """
    target = p - 1         # -1 mod p
    cycle  = p - 1         # exponent cycle by Fermat
    triples = []

    for a in range(2, p):
        if math.gcd(a, p) != 1:
            continue
        for b in range(2, p):
            bm = b % cycle
            for c in range(2, p):
                e = (bm * (c % cycle)) % cycle
                if pow(a, e, p) == target:
                    triples.append((a, b, c))
    return triples

def main():
    p = int(input("Enter a prime p: "))
    triples = find_all_triples(p)

    if triples:
        print(f"Found {len(triples)} nontrivial triples for p = {p}:")
        for a, b, c in triples:
            print(f"  (a={a}, b={b}, c={c})")
    else:
        print(f"No nontrivial triples found for p = {p}.")

if __name__ == "__main__":
    main()
