from sympy import symbols, Poly
from sympy.polys.domains import GF
from itertools import product

def irreducible_polynomials(p, max_degree):
    """
    Return a dict mapping degree d to the list of all monic irreducible
    polynomials of degree d over GF(p), for 1 <= d <= max_degree.
    """
    x = symbols('x')
    F = GF(p)

    irreducibles = {}
    for d in range(1, max_degree+1):
        irreducibles[d] = []
        # iterate over all possible coefficient tuples for x^(d-1)...x^0
        for coeffs in product(range(p), repeat=d):
            # build f(x) = x^d + coeffs[d-1]*x^(d-1) + ... + coeffs[0]
            poly = Poly(x**d + sum(coeffs[i]*x**i for i in range(d)), x, domain=F)
            if poly.is_irreducible:
                irreducibles[d].append(poly)

        print(f"Degree {d}: found {len(irreducibles[d])} irreducible polynomials")

    return irreducibles

if __name__ == "__main__":
    p = 7
    max_deg = 4    # adjust as needed (degree 4: ~840 polynomials)
    irr = irreducible_polynomials(p, max_deg)

    # Example: print all monic irreducible quadratics
    print("\nMonic irreducible quadratics over GF(7):")
    for q in irr[2]:
        print("  ", q.as_expr())
