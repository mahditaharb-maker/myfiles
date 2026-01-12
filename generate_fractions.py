#!/usr/bin/env python3
"""
Generate all 'fractions' [a:b] in Z_p x Z_p as projective points.
Each class is given by pairs (x,y) satisfying x b - a y = 0 mod p.
We group them by the canonical ratio a/b in F_p, with b != 0,
and the 'point at infinity' when b == 0.
"""

def generate_fractions(p: int):
    if p < 2:
        raise ValueError("p must be a prime ≥ 2.")
    # We'll represent each fraction by:
    #   - an integer 0 <= r < p if it's r = a * inv(b) mod p
    #   - the string 'inf' for b == 0
    fracs = {}

    # Ratio classes indexed by r in 0..p-1
    for r in range(p):
        # all (x,y) with x = r*y mod p
        pts = [((r * y) % p, y) for y in range(p)]
        fracs[r] = pts

    # The 'point at infinity' [1:0], i.e. all (x,0)
    fracs['inf'] = [(x, 0) for x in range(p)]

    return fracs


def main():
    p = int(input("Enter a prime p: ").strip())
    fracs = generate_fractions(p)

    # Print out
    for key in sorted(fracs, key=lambda v: (v=='inf', v)):
        label = f"{key}" if key != 'inf' else "∞"
        print(f"\nFraction [{label}] has {len(fracs[key])} points:")
        print(fracs[key])


if __name__ == "__main__":
    main()
