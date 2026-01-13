import math

def finite_field_pi_fraction_polygon(p):
    """
    Approximate π using the area of a polygon with p points in the finite field Z_p
    and represent it as a fraction modulo p.
    """
    if p <= 2:
        raise ValueError("p must be greater than 2 to form a meaningful polygon")

    # Coordinates of points on the unit circle (geometric interpretation)
    points = [(math.cos(2 * math.pi * i / p), math.sin(2 * math.pi * i / p)) for i in range(p)]

    # Calculate the area of the polygon using the Shoelace formula
    area = 0
    for i in range(p):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % p]  # Wrap around to the first point
        area += x1 * y2 - y1 * x2
    area = abs(area) / 2  # Area of the polygon

    # Approximate π using the polygon's area
    approx_pi = p * math.sin(2 * math.pi / p) / 2  # Approximation

    # Scale π to create a fraction in Z_p
    numerator = round(approx_pi * (p - 1))  # Scale by (p - 1) instead of p
    denominator = p - 1  # Use p - 1 to avoid zero modulo p

    # Reduce numerator and denominator modulo p
    numerator_mod = numerator % p
    denominator_mod = denominator % p

    # Check if the denominator is invertible in Z_p
    try:
        denominator_inverse = pow(denominator_mod, -1, p)  # Modular inverse
    except ValueError:
        raise ValueError(f"Denominator {denominator_mod} is not invertible in Z_{p}.")

    # Compute π as a fraction in Z_p
    pi_mod_p = (numerator_mod * denominator_inverse) % p

    return (numerator_mod, denominator_mod, pi_mod_p)

# Example usage:
p = 65537  # Finite field Z_p
result = finite_field_pi_fraction_polygon(p)
print(f"Numerator: {result[0]}, Denominator: {result[1]}, π (mod {p}): {result[2]}")
