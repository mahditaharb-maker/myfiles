def gen_series_coeffs(p, recurrence_fn):
    """
    Build [a_0, a_1, …, a_{p-1}] in Z_p by a user-supplied recurrence.

    - p: prime modulus
    - recurrence_fn(n, coeffs, p): returns a_n mod p,
      given index n, the list coeffs = [a_0…a_{n-1}], and p.
    """
    coeffs = []
    for n in range(p):
        coeffs.append(recurrence_fn(n, coeffs, p))
    return coeffs


def rec_fact_inv(n, coeffs, p):
    """
    Recurrence for a_n = 1/n! mod p:
      a_0 = 1
      a_n = a_{n-1} * inv(n) mod p
    """
    if n == 0:
        return 1
    inv_n = pow(n, p - 2, p)   # modular inverse of n
    return coeffs[-1] * inv_n % p


def poly_from_coeffs(coeffs, p):
    """
    Interpret the series [a_0…a_{p-1}] as the polynomial
      f(x) = sum_{n=0}^{p-1} a_n * x^n  in Z_p[x].
    """
    return [c % p for c in coeffs]


def eval_poly(coeffs, x, p):
    """
    Evaluate f(x) = sum coeffs[n] * x^n mod p
    via Horner’s method.
    """
    res = 0
    power = 1
    for c in coeffs:
        res = (res + c * power) % p
        power = (power * x) % p
    return res


if __name__ == "__main__":
    p = 7

    # 1) Generate a_n = 1/n! mod p for n = 0..p-1
    a_vals = gen_series_coeffs(p, rec_fact_inv)

    # 2) Build polynomial coefficients f(x) = sum a_n x^n
    coeffs = poly_from_coeffs(a_vals, p)

    # Output
    print(f"p = {p}")
    print("a_n = 1/n! mod p for n=0..p-1 ->", a_vals)
    print("Polynomial coefficients [c_0, c_1, …, c_{p-1}] ->", coeffs)

    # 3) Verify f(n) == a_n for n=0..p-1
    print("\nVerification:")
    for n in range(p):
        fx = eval_poly(coeffs, n, p)
        print(f"f({n}) = {fx} (expected {a_vals[n]})")
