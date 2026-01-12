import sympy

def is_prime(n):
    return sympy.isprime(n)

def generate_special_primes(limit):
    special_primes = []
    for p in sympy.primerange(2, limit):
        expression = p**2 - 2*p + 2
        if is_prime(expression):
            special_primes.append(p)
    return special_primes

# Set a reasonable upper limit for primes to check
upper_limit = 10000
sequence = generate_special_primes(upper_limit)

# Display results
print("Special prime sequence:")
print(sequence)
print(f"\nTotal number of elements: {len(sequence)}")
