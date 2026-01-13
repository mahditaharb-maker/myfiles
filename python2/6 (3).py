import math

# maximum total loop operations we’re willing to do (~ a·b·c ≈ p³)
MAX_OPS = 1e7

def compute_safe_limit():
    """
    Compute the largest prime p such that p³ ≤ MAX_OPS.
    """
    return int(MAX_OPS ** (1/3))

def find_all_triples(p, max_triples=None):
    """
    Return (triples_list, aborted_flag)
    - triples_list: collected (a,b,c) tuples
    - aborted_flag: True if search stopped early (overflow or limit hit)
    """
    safe_limit = compute_safe_limit()
    if p > safe_limit:
        print(f"Complexity overflow: p = {p} exceeds safe bound {safe_limit}.")
        return [], True

    target = p - 1
    cycle  = p - 1
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
                    # respect user‐defined tolerance
                    if max_triples and len(triples) >= max_triples:
                        print(f"Limit reached: collected {max_triples} triples; stopping early.")
                        return triples, True

    return triples, False

def main():
    p = int(input("Enter a prime p: "))
    raw = int(input("Enter max triples to collect (0 = no limit): "))
    max_triples = raw if raw > 0 else None

    triples, aborted = find_all_triples(p, max_triples)

    if not triples and aborted:
        # either p was too large or limit was zero and no triples found
        return

    print(f"\nFound {len(triples)} nontrivial triples for p = {p}:")
    for a, b, c in triples:
        print(f"  (a={a}, b={b}, c={c})")

    if aborted:
        print("\nNote: search stopped early due to limit tolerance or complexity bound.")

if __name__ == "__main__":
    main()
