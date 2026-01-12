from random import randint
from fractions import Fraction

def modular_pi_approximation(modulus, radius, samples):
    inside_circle = 0
    
    for _ in range(samples):
        # Random point (x, y) in Z_modulus
        x = randint(0, modulus - 1)
        y = randint(0, modulus - 1)
        
        # Check if the point is inside the circle
        if (x**2 + y**2) % modulus <= radius**2 % modulus:
            inside_circle += 1
    
    # Fractional approximation of pi
    approx_pi = Fraction(inside_circle, samples) * 4
    
    # Ensure the result lies between 3 and 4
    if approx_pi < 3:
        approx_pi = Fraction(3, 1)
    elif approx_pi > 4:
        approx_pi = Fraction(4, 1)
    
    return approx_pi

# Parameters
modulus = 65537  # Z_65537
radius = 10000   # Choose a suitable radius
samples = 100000 # Number of random samples

approximation = modular_pi_approximation(modulus, radius, samples)
print(f"Approximation of pi in Z_{modulus} as fraction (between 3 and 4): {approximation}")
