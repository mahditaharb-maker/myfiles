def gen_series_coeffs(p, recurrence_fn):
    """
    Build [a_0, a_1, …, a_{p-1}] in Z_p by a user-supplied recurrence.
      - p: prime modulus
      - recurrence_fn(n, coeffs, p): returns a_n mod p,
        given index n and list coeffs = [a_0…a_{n-1}].
    """
    coeffs = []
    for n in range(p):
        coeffs.append(recurrence_fn(n, coeffs, p))
    return coeffs


def poly_from_coeffs(coeffs, p):
    """Interpret [a_0…a_{p-1}] as f(x)=∑ a_n x^n in Z_p[x]."""
    return [c % p for c in coeffs]


def eval_poly(coeffs, x, p):
    """Evaluate f(x)=∑ coeffs[n]·x^n mod p."""
    res, power = 0, 1
    for c in coeffs:
        res = (res + c * power) % p
        power = (power * x) % p
    return res


if __name__ == "__main__":
    # 1) Read prime modulus
    p = int(input("Enter a prime number p: ").strip())

    # 2) Read and validate a_0 as an integer
    while True:
        a0_str = input("Enter a_0 (integer mod p): ").strip()
        try:
            a0 = int(a0_str) % p
            break
        except ValueError:
            print("  → Please enter a valid integer.")

    # 3) Read the recursive formula for a_n (n > 0)
    print("Enter recursive formula for a_n (use 'n', 'prev', 'p'),")
    print("for example: prev * pow(n, p-2, p) % p")
    while True:
        rec_expr = input("a_n = ").strip()
        if not rec_expr:
            print("  → Formula cannot be empty.")
            continue
        # quick syntax check
        try:
            compile(rec_expr, "<string>", "eval")
            break
        except SyntaxError as e:
            print(f"  → Syntax error: {e.msg}")

    # 4) Build recurrence function
    def recurrence_fn(n, coeffs, p):
        if n == 0:
            return a0
        prev = coeffs[-1]
        # safe eval: only n, prev, p in locals
        return eval(rec_expr, {}, {"n": n, "prev": prev, "p": p})

    # 5) Generate the series and polynomial
    a_vals = gen_series_coeffs(p, recurrence_fn)
    coeffs = poly_from_coeffs(a_vals, p)

    # 6) Print results
    print(f"\np = {p}")
    print("a_n sequence:", a_vals)
    print("Polynomial coefficients [c_0…c_{p-1}]:", coeffs)

    # 7) Optional verification
    print("\nVerification:")
    for n in range(p):
        print(f" f({n}) = {eval_poly(coeffs, n, p)}  (expected {a_vals[n]})")
