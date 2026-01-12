def evaluate_series(coeffs, t, mod):
    """
    Evaluate the polynomial 
        c[0] + c[1]*t + c[2]*t^2 + ... + c[k]*t^k
    under modulus `mod`.
    """
    x = 0
    power = 1
    for c in coeffs:
        x = (x + c * power) % mod
        power = (power * t) % mod
    return x

def solve_quadratic_series(p, t, n):
    """
    Solve x^2 + x ≡ t   (mod t^n),  then reduce solutions mod p.
    
    Preconditions:
      - p is prime
      - t^n < p
    
    Returns:
      A tuple (x1_mod_p, x2_mod_p) giving the two roots mod p.
    """
    assert pow(t, n) < p, "You must have t^n < p"

    # Coefficients of x₁ = ∑ a_i t^i  for i=0..9
    a = [0,  1, -1,   2,  -5,   14,  -42,   132,  -429,   1430]
    # Coefficients of x₂ = ∑ b_i t^i  for i=0..9
    b = [-1, 0,  1,  -2,   5,  -14,    42,  -132,    429,  -1430]

    # Truncate to degree n-1 if n < 10
    a = a[:n]
    b = b[:n]

    x1 = evaluate_series(a, t, p)
    x2 = evaluate_series(b, t, p)
    return x1, x2

# Example usage
if __name__ == "__main__":
    p = 10**9 + 7
    t = 5
    n = 10               # requires t^10 < p
    x1_mod_p, x2_mod_p = solve_quadratic_series(p, t, n)
    print("Solution x1 ≡", x1_mod_p, "mod", p)
    print("Solution x2 ≡", x2_mod_p, "mod", p)
