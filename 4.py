import sympy

def generate_prime_chain(p):
    """
    Starting from prime p, repeatedly apply
      f(x) = x^2 – 2*x + 2
    until the result is either
      1) composite, or
      2) equal to the previous term (fixed point).
    Return the full chain.
    """
    chain = [p]
    while True:
        prev = chain[-1]
        nxt = prev**2 - 2*prev + 2

        # Stop if nxt is not prime
        if not sympy.isprime(nxt):
            break

        chain.append(nxt)

        # Stop if we've hit a fixed point (e.g. 2 → 2)
        if nxt == prev:
            break

    return chain

def find_prime_chains(limit):
    """
    For each prime p < limit, check
      f(p) = p^2 – 2*p + 2.
    If that's prime, build its chain.
    """
    chains = []
    for p in sympy.primerange(2, limit):
        if sympy.isprime(p**2 - 2*p + 2):
            chains.append(generate_prime_chain(p))
    return chains

if __name__ == '__main__':
    LIMIT = 10_000
    chains = find_prime_chains(LIMIT)

    # Display each chain and its length
    for chain in chains:
        print(" -> ".join(map(str, chain)), f"(length = {len(chain)})")
    print(f"\nTotal chains found (p < {LIMIT}): {len(chains)}")
