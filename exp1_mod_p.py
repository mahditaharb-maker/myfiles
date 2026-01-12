def exp1_mod_p(p):
    """
    Compute exp(1) = sum_{i=0}^{p-1} 1/i!  in the finite field F_p.

    Input:
      p : a prime integer

    Returns:
      e : the value of exp(1) mod p
    """
    # 0! = 1, so start with term for i=0
    e = 1
    fact = 1

    # Loop from i = 1 to p-1
    for i in range(1, p):
        fact = (fact * i) % p        # i! mod p
        inv_fact = pow(fact, p-2, p)  # Fermat's little theorem: (i!)^(−1) mod p
        e = (e + inv_fact) % p

    return e


if __name__ == "__main__":
    for p in [2, 3, 5, 7, 11]:
        print(f"exp(1) mod {p} = {exp1_mod_p(p)}")
