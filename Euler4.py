def find_abc_bruteforce(p):
    """
    Find any (a,b,c) with
      (p-1)//4 < a, b, c <= (p-1)//2
    such that (a**(b*c) + 1) % p == 0.
    Returns (a, b, c) or None.
    """
    quarter = (p - 1) // 4
    half    = (p - 1) // 2

    for a in range(quarter + 1, half + 1):
        for b in range(quarter + 1, half + 1):
            for c in range(quarter + 1, half + 1):
                # pow(x, y, p) computes x**y % p efficiently
                if pow(a, b * c, p) == p - 1:
                    return a, b, c

    return None


if __name__ == "__main__":
    p = 5  # example prime
    sol = find_abc_bruteforce(p)
    if sol:
        print(f"Found solution: a={sol[0]}, b={sol[1]}, c={sol[2]}")
    else:
        print("No solution in the given range.")
