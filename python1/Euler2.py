def find_abc_bruteforce(p):
    """
    Find integers a, b, c with
      1 < a, b, c <= (p-1)//2
    such that (a**(b*c) + 1) % p == 0.
    Returns (a, b, c) or None.
    """
    half = (p - 1) // 2

    for a in range(2, half + 1):
        for b in range(2, half + 1):
            for c in range(2, half + 1):
                # pow does modular exponentiation efficiently
                if pow(a, b * c, p) == p - 1:
                    return a, b, c
    return None


if __name__ == "__main__":
    p = 31
    sol = find_abc_bruteforce(p)
    if sol:
        print(f"Found solution: a={sol[0]}, b={sol[1]}, c={sol[2]}")
    else:
        print("No solution in the given range.")
