import math

def approximate_pi(n):
    """
    Approximates the value of pi using the area of a regular polygon with n sides.
    The polygon is inscribed in a unit circle.
    
    Parameters:
    n (int): Number of sides in the polygon
    
    Returns:
    float: Approximation of pi
    tuple: Fractional approximation of pi as (numerator, denominator)
    """
    if n < 3:
        raise ValueError("n must be at least 3 (minimum sides for a polygon).")
    
    # Calculate the side length of the polygon
    side_length = 2 * math.sin(math.pi / n)
    
    # Calculate the area of the polygon
    polygon_area = 0.5 * n * side_length * math.cos(math.pi / n)
    
    # Approximate pi as a fraction
    numerator = round(polygon_area * (10 ** 6))  # Scale up for precision
    denominator = 10 ** 6
    return polygon_area, (numerator, denominator)


# Example usage:
n = 65536  # Replace with your desired number of sides
pi_approx, pi_fraction = approximate_pi(n)
print(f"Approximation of pi: {pi_approx}")
print(f"Fractional approximation of pi: {pi_fraction[0]}/{pi_fraction[1]}")
