import sympy

def is_prime_form(n, form="+"):
    """
    Check if the number of form 2^n ± 1 is prime.
    
    Args:
    - n (int): exponent
    - form (str): "+" or "-" to choose between 2^n + 1 or 2^n - 1
    
    Returns:
    - tuple (n, number, True/False) if number is prime
    """
    if form == "+":
        num = 2**n + 1
    elif form == "-":
        num = 2**n - 1
    else:
        raise ValueError("form must be '+' or '-'")

    return (n, num, sympy.isprime(num))

# Example: Check for primes for n in range 1 to 100
def find_special_primes(start=1, end=100):
    plus_primes = []
    minus_primes = []

    for n in range(start, end + 1):
        if (res := is_prime_form(n, "+"))[2]:
            plus_primes.append(res)
        if (res := is_prime_form(n, "-"))[2]:
            minus_primes.append(res)

    return plus_primes, minus_primes

# Run and print
plus_form_primes, minus_form_primes = find_special_primes(1,129 )

print("Primes of the form 2^n + 1:")
for n, val, _ in plus_form_primes:
    print(f"n={n}, 2^{n}+1 = {val}")

print("\nPrimes of the form 2^n - 1:")
for n, val, _ in minus_form_primes:
    print(f"n={n}, 2^{n}-1 = {val}")
