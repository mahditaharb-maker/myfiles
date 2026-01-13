def find_abc(p):
    """
    Find integers a, b, c (1 <= a,b,c <= (p-1)//2) such that
    (a**(b*c) + 1) % p == 0.
    Returns a tuple (a,b,c) or None if no solution is found.
    """
    half = (p - 1) // 2

    # brute-force search
    for a in range(1, half + 1):
        for b in range(1, half + 1):
            for c in range(1, half + 1):
                if pow(a, b * c, p) == p - 1:  # same as (a**(b*c)+1) % p == 0
                    return a, b, c

    return None


if __name__ == "__main__":
    p = 46  # example prime
    res = find_abc(p)
    if res:
        a, b, c = res
        print(f"Found a={a}, b={b}, c={c}: (a^(b*c)+1) % p == 0")
    else:
        print("No solution exists for this p.")
