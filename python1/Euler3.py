def find_abc_optimized(p):
    """
    Faster search using a map from exponent e to one (b,c) pair,
    for 1 < b, c <= (p-1)//2.
    """
    half = (p - 1) // 2
    exp_map = {}

    # Build exponent-to-(b,c) map
    for b in range(2, half + 1):
        for c in range(2, half + 1):
            e = (b * c) % (p - 1)
            # Store first pair that produces exponent e
            if e not in exp_map:
                exp_map[e] = (b, c)

    # Test each a against every unique exponent
    for a in range(2, half + 1):
        for e, (b, c) in exp_map.items():
            if pow(a, e, p) == p - 1:
                return a, b, c
    return None


if __name__ == "__main__":
    p = 17
    sol = find_abc_optimized(p)
    if sol:
        print("Solution:", sol)
    else:
        print("No solution found.")
