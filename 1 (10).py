def find_nontrivial_abc(p):
    """
    Find nontrivial a, b, c in ℕ, all >1, such that
        a^(b*c) ≡ −1 (mod p),
    where p is prime. Returns a tuple (a, b, c) or None if no solution found.
    """
    # Loop over possible a, b, c
    for a in range(2, p):
        for b in range(2, p):
            for c in range(2, p):
                if pow(a, b * c, p) == p - 1:
                    return a, b, c
    return None

if __name__ == "__main__":
    p = 7  # example prime
    sol = find_nontrivial_abc(p)
    if sol:
        a, b, c = sol
        print(f"Found solution for p={p}: a={a}, b={b}, c={c}")
    else:
        print(f"No solution found for p={p}")
