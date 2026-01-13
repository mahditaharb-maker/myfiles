import sympy

# Start with n values to check for 2^n + 1 > 1,000,000
n = 1
found_prime = None

# Check for 2^n + 1 being prime
while True:
    candidate = 2**n + 1
    if candidate > 255 and sympy.isprime(candidate):
        found_prime = candidate
        break
    n += 1

print(found_prime)
