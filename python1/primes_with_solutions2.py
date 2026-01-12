from sympy import isprime, legendre_symbol

def primes_with_solutions(limit):
    solution_primes = []
    for p in range(2, limit + 1):
        if not isprime(p):
            continue
        try:
            if legendre_symbol(-3, p) == 1:
                solution_primes.append(p)
        except ValueError:
            # gets triggered for p=2 or any non-odd prime,
            # just skip it
            continue
    return solution_primes

# Example
print(primes_with_solutions(70000))
