import random

def legendre_symbol(a: int, p: int) -> int:
    """
    Compute the Legendre symbol (a|p) using Euler’s criterion:
      (a|p) ≡ a^((p-1)/2) mod p
    Returns  1 if a is a quadratic residue mod p (and a != 0),
            -1 if it is a non-residue,
             0 if a ≡ 0 mod p.
    """
    ls = pow(a % p, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls

def tonelli_shanks(n: int, p: int) -> int:
    """
    Solve x^2 ≡ n mod p via Tonelli–Shanks.
    Returns one root x, or raises ValueError if no root exists.
    Precondition: p is an odd prime, and (n|p) = 1.
    """
    assert legendre_symbol(n, p) == 1, "No square root exists"
    # Simple cases
    if n == 0:
        return 0
    if p == 2:
        return n

    # Factor out powers of 2 from p-1: p-1 = q * 2^s
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Find a quadratic non-residue z
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    # Initialize
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    # Loop until t == 1
    while t != 1:
        # Find least i (0 < i < m) such that t^(2^i) ≡ 1
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break

        # Update values
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return r

def solve_mod_eq_bruteforce(p: int):
    """
    Brute‐force all pairs (x,y) in [0..p-1]^2 such that x^2 + y^2 ≡ 1 (mod p).
    Time: O(p^2)
    """
    sols = []
    for x in range(p):
        for y in range(p):
            if (x*x + y*y) % p == 1:
                sols.append((x, y))
    return sols

def solve_mod_eq_fast(p: int):
    """
    For each x compute rhs = 1 - x^2 (mod p).  If rhs is a QR, take its sqrt
    (two solutions ±y).  Uses Tonelli–Shanks under the hood.
    Time: O(p · log^3 p) roughly.
    """
    sols = []
    for x in range(p):
        rhs = (1 - x*x) % p
        if rhs == 0:
            sols.append((x, 0))
            continue

        if legendre_symbol(rhs, p) == 1:
            y = tonelli_shanks(rhs, p)
            sols.append((x, y))
            if y != 0:
                sols.append((x, (-y) % p))
    return sols

if __name__ == "__main__":
    p = int(input("Enter an odd prime p: "))
    print(f"Brute‐force solutions (count = {p*p} checks):")
    bf = solve_mod_eq_bruteforce(p)
    print(sorted(bf))

    print("\nOptimized solutions using Tonelli–Shanks:")
    fast = solve_mod_eq_fast(p)
    print(sorted(fast))
