from sympy import isprime, legendre_symbol

def primes_with_solutions(limit):
    solution_primes = []
    # start at 3, step by 2: only odd numbers
    for p in range(3, limit + 1, 2):
        if not isprime(p):
            continue
        # now p is an odd prime: safe to call legendre_symbol
        if legendre_symbol(-3, p) == 1:
            solution_primes.append(p)
    return solution_primes

# Example
print(primes_with_solutions(20))
