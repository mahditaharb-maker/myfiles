# Python script to search for primes p admitting a "Euler identity" in F_p:
#   find e, i, pi in {0,...,p-1} with e^(i·pi) + 1 ≡ 0 mod p.

from sympy import primerange

def find_euler_triple(p):
    # Solve i^2 ≡ -1 mod p
    targets = [i for i in range(p) if (i * i) % p == p - 1]
    if not targets:
        return None

    for i in targets:
        for e in range(2, p):      # skip trivial e=0,1
            for pi in range(1, p): # skip π=0 trivializes exponent
                if pow(e, i * pi, p) == p - 1:  # e^(i·π) ≡ -1 mod p
                    return (e, i, pi)
    return None

def main(limit=200):
    print(f"{'p':>3}  ⇒  (e, i, π) or None")
    print("-" * 28)
    for p in primerange(2, limit):
        triple = find_euler_triple(p)
        print(f"{p:3d}  ⇒  {triple}")

if __name__ == "__main__":
    main(101)
