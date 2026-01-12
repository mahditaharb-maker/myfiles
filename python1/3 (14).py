import math

def is_primitive_root(g, p):
    """
    Check if g is a primitive root modulo p.
    """
    seen = {pow(g, e, p) for e in range(1, p)}
    return len(seen) == p - 1

def phi_x(x, p):
    """
    Compute φₓ(x) = –⌊log₂(x)⌋, then clamp into {1,2,…,p−1} by wrapping modulo (p−1).
    Guarantees no zero or ≥p values.
    """
    raw = -math.floor(math.log2(x))
    # wrap into 1..p-1
    return ((raw - 1) % (p - 1)) + 1

def phi_k(k, p):
    """
    Solve for e in 2^(p-1−e) ≡ k (mod p), for e in {1,…,p−1}.
    Raises ValueError if no solution (i.e. k ≡ 0 mod p).
    """
    k_mod = k % p
    for e in range(1, p):
        if pow(2, p - 1 - e, p) == k_mod:
            return e
    raise ValueError(f"No φ(k,p) for k={k_mod} mod {p}")

def phi_iterates(x, p):
    """
    Generate the length-p φ-sequence:
      [φₓ(x), φₖ(φₓ(x)), φₖ(φₖ(φₓ(x))), …]
    """
    seq = []
    n = phi_x(x, p)
    seq.append(n)
    for _ in range(1, p):
        n = phi_k(n, p)
        seq.append(n)
    return seq

def f(x, p):
    """
    Compute f(x) = Σ₂^{-n} over the φ-sequence of length p.
    """
    return sum(2 ** (-n) for n in phi_iterates(x, p))

def main():
    # Candidate primes to test
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29]
    # Sample x values
    x_values = [0.30, 0.10, 0.02]

    for p in primes:
        # Skip degenerate case p<5 where involution breaks
        if p < 5:
            print(f"Skipping p={p}: too small for involution")
            continue

        # Require that base=2 is a primitive root mod p
        if not is_primitive_root(2, p):
            print(f"Skipping p={p}: 2 is not primitive.")
            continue

        print(f"\n=== p = {p} (good) ===")
        for x in x_values:
            fx  = f(x, p)
            ffx = f(fx, p)
            seq = phi_iterates(x, p)

            print(f"x={x:5.3f} → seq={seq}")
            print(f" f(x) = {fx:.6f},  f(f(x)) = {ffx:.6f}")

if __name__ == "__main__":
    main()
