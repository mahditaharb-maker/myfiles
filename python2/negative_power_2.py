def negative_power_2(p: int, q: int) -> int:
    """
    Return the smallest nonnegative n < p-1 satisfying
        2^(-n) ≡ q  (mod p).
    Raises ValueError if p<=2, q not in [1..p-1], or no solution is found.
    """
    if p <= 2 or not (1 <= q < p):
        raise ValueError("Require prime p>2 and 1 <= q < p.")
    # 2^(-n) ≡ q  <=>  2^n ≡ q^{-1} mod p
    target = pow(q, -1, p)
    # BSGS parameters
    from math import isqrt
    m = isqrt(p - 1) + 1

    # Baby steps: store 2^(j*m) → j
    baby = {pow(2, j * m, p): j for j in range(m)}

    # Giant steps: iterate i from 0 to m-1 looking for collision
    curr = target
    for i in range(m):
        if curr in baby:
            j = baby[curr]
            n = j * m - i
            return n % (p - 1)
        # multiply by the base (2) to shift exponent by –1 each time
        curr = (curr * 2) % p

    raise ValueError("No solution: 2 might not be primitive modulo p.")

# Example
if __name__ == "__main__":
    p, q = 131, 29
    n = negative_power_2(p, q)
    print(n)               # 11
    print(pow(2, -n, p))   # verifies: 20
