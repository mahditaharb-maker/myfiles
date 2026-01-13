import math

def modular_square(x, modulus):
    """
    Compute x^2 modulo modulus.
    """
    return (x * x) % modulus

def quadrance(point1, point2, modulus):
    """
    Compute the quadrance (squared distance) between two points 
    in the finite field F_modulus.
    """
    return modular_square(point2 - point1, modulus)

def polygon_area(n, modulus):
    """
    Calculate a crude approximation of the area of a regular polygon with n sides
    using quadrances in the finite field F_modulus. 

    Here we imagine splitting the circle into n segments.
    The area is approximated by summing the quadrances of adjacent vertices 
    (interpreted as chord lengths) and halving the result.
    """
    if n < 3 or modulus <= n:
        raise ValueError("Ensure n >= 3 and modulus > n.")
    
    total_quadrance = 0
    # Define a step that partitions our 'circle' into n arcs
    step = modulus // n

    for k in range(n):
        point1 = (k * step) % modulus
        point2 = ((k + 1) * step) % modulus
        total_quadrance += quadrance(point1, point2, modulus)
    
    # Use half the total quadrance as our area approximation.
    area = (total_quadrance // 2) % modulus
    return area

def calculate_radius_and_pi(n, modulus):
    """
    Calculate both the "radius" and the approximation of pi using the
    formula pi = area / (radius^2). 

    We define the radius as the distance (via quadrance) from the center (0)
    to an assumed point on the circle (here, modulus//2). Since quadrance returns
    an integer modulo modulus, we use math.sqrt to get a real-valued approximation
    for the radius.
    """
    area = polygon_area(n, modulus)
    # Here we compute the quadrance (i.e. squared distance) from 0 to modulus//2.
    radius_squared = quadrance(0, modulus // 2, modulus)
    radius = math.sqrt(radius_squared)
    
    # Compute pi as the ratio of the area to the squared radius.
    pi_approximation = area / radius_squared
    return radius, pi_approximation

if __name__ == "__main__":
    n = 65536        # polygon with 65536 sides
    modulus = 65537  # finite field prime
    radius, pi_approximation = calculate_radius_and_pi(n, modulus)
    print(f"Radius: {radius}")
    print(f"Approximation of pi: {pi_approximation}")
