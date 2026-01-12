from sympy import mod_inverse, sqrt_mod

def compute_spread(k, p, n):
    """
    Compute the spread s = sin^2(2pi/n) in Z_p.
    For our chosen examples we use:
      - n = 4: s = 1
      - n = 8: s = 1/2  (since sin^2(pi/4) = 1/2)
      - n = 16: s = (2 - sqrt(2)) / 4 (with a square root computed modulo p)
    For other cases we default to s = 1.
    """
    if n == 4:
        s = 1
    elif n == 8:
        s = mod_inverse(2, p)  # 1/2 mod p
    elif n == 16:
        # For n=16, 2pi/16 = pi/8 so sin^2(pi/8) = (2 - sqrt2)/4.
        # Compute a square root of 2 mod p; sqrt_mod returns one solution.
        sol = sqrt_mod(2, p, all_roots=False)
        if sol is None:
            raise ValueError("No square root for 2 in Z_{}".format(p))
        inv4 = mod_inverse(4, p)
        s = ((2 - sol) * inv4) % p
    else:
        # Fallback for unsupported n
        s = 1
    return s

def regular_polygon_area(k):
    """
    For a given k, set
        p = 2^k + 1   (should be prime)
        n = 2^k       (number of sides)
    Then compute a finite-field analogue of the polygon area.
    
    We assume the polygon is decomposed into n isosceles central triangles 
    with legs of length 1 (so quadrances of 1) and vertex (central) angle 2pi/n.
    In our model, the triangle "area" is:
        triangle_area = (s / 2)  mod p,
    where s is the spread, s = sin^2(2pi/n).
    The polygon area is then n times triangle_area.
    """
    p = 2**k + 1
    n = 2**k
    print(f"Using k = {k}, p = {p}, n = {n}")
    
    inv2 = mod_inverse(2, p)
    s = compute_spread(k, p, n)
    
    triangle_area = (s * inv2) % p
    polygon_area = (n * triangle_area) % p
    return polygon_area

if __name__ == "__main__":
    # You can test for a few values of k.
    # For example, k=2 gives p=5 and n=4;
    # k=3 gives p=9 (but note 9 is composite, so use caution);
    # k=4 gives p=17 and n=16 (17 is prime, a Fermat prime).
    
    # Let's use k=4:
    k = 17
    area = regular_polygon_area(k)
    print("Regular polygon area in Z_p:", area)
