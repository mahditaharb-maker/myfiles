import math
from fractions import Fraction

def near_equal(a, b, tol=1e-12):
    return abs(a - b) <= tol

def case_classify(x, y, z):
    c = math.sqrt(x*x + y*y)
    if near_equal(c, z): 
        return 'c=z'
    return 'c<z' if c < z else 'c>z'

def verify_normalization(x, y, z, n):
    """Return A,B and booleans for normalized identities."""
    A = x / z
    B = y / z
    lhs_n     = (A**n + B**n)
    lhs_nplus = (A**(n+2) + B**(n+2))
    return A, B, lhs_n, lhs_nplus

def case2_signs(x, y, z, n):
    """Compute LHS and RHS in Case 2 identity:
       1 - sin^2 a - sin^2 b  vs  sin^2 a (sin^n a - 1) + sin^2 b (sin^n b - 1)
       with sin a = x/z, sin b = y/z."""
    sa = x / z
    sb = y / z
    lhs = 1 - sa*sa - sb*sb
    rhs = (sa*sa) * (sa**n - 1) + (sb*sb) * (sb**n - 1)
    return lhs, rhs

def case3_growth(x, y, z, n):
    """Check the arithmetic growth contradiction:
       If c > z, then for n>=3: x^(n+2) + y^(n+2) > z^(n+2)."""
    c2 = x*x + y*y
    z2 = z*z
    return (c2 > z2), (x**(n+2) + y**(n+2)) > (z**(n+2))

def search_near_misses(limit_x=20, limit_y=20, limit_z=40, exponents=(3,4,5)):
    """Enumerate small triples to illustrate the checks."""
    results = []
    for n in exponents:
        for x in range(1, limit_x+1):
            for y in range(1, limit_y+1):
                for z in range(1, limit_z+1):
                    # Skip trivial/degenerate
                    if x == 0 or y == 0 or z == 0:
                        continue
                    # True equality would contradict FLT; we expect none.
                    eq = (x**n + y**n == z**n)
                    if eq:
                        # We record but note this should not occur for n>2.
                        results.append(('equality', n, x, y, z))
                        continue

                    # Classify case by c vs z
                    case = case_classify(x, y, z)
                    A, B, lhs_n, lhs_nplus = verify_normalization(x, y, z, n)

                    if case == 'c<z':
                        lhs, rhs = case2_signs(x, y, z, n)
                        # Case 2 signature: lhs > 0 and rhs < 0
                        if lhs > 0 and rhs < 0:
                            results.append(('case2_sign_contradiction', n, x, y, z, lhs, rhs))

                    elif case == 'c>z':
                        c_gt_z, growth = case3_growth(x, y, z, n)
                        # Case 3 signature: c>z and growth inequality holds
                        if c_gt_z and growth:
                            results.append(('case3_growth_contradiction', n, x, y, z))

                    elif case == 'c=z':
                        # Case 1 algebraic contradiction indicator:
                        # sin^n a < 1 and cos^n a < 1 for n>=1 when angles in (0,pi/2)
                        sa = x / z
                        ca = y / z
                        if 0 < sa < 1 and 0 < ca < 1 and n >= 1:
                            results.append(('case1_algebraic_contradiction', n, x, y, z))

    return results

def demo():
    results = search_near_misses(limit_x=12, limit_y=12, limit_z=24, exponents=(3,4))
    # Summarize
    c1 = [r for r in results if r[0] == 'case1_algebraic_contradiction']
    c2 = [r for r in results if r[0] == 'case2_sign_contradiction']
    c3 = [r for r in results if r[0] == 'case3_growth_contradiction']
    eq = [r for r in results if r[0] == 'equality']

    print('Case 1 hits (algebraic contradiction indicators):', len(c1))
    print('Case 2 hits (sign contradiction examples):', len(c2))
    print('Case 3 hits (growth contradiction examples):', len(c3))
    print('Accidental equalities x^n + y^n = z^n found (should be 0 for n>2):', len(eq))

    # Print a few illustrative examples
    for tag, arr in [('case2_sign_contradiction', c2),
                     ('case3_growth_contradiction', c3)]:
        print(f'\nExamples for {tag}:')
        for ex in arr[:5]:
            if tag == 'case2_sign_contradiction':
                _, n, x, y, z, lhs, rhs = ex
                c = math.sqrt(x*x + y*y)
                print(f'  n={n}, (x,y,z)=({x},{y},{z}), c={c:.4f} < z={z}')
                print(f'    LHS=1-(x/z)^2-(y/z)^2={lhs:.6f} > 0,  RHS={rhs:.6f} < 0')
            else:
                _, n, x, y, z = ex
                c = math.sqrt(x*x + y*y)
                print(f'  n={n}, (x,y,z)=({x},{y},{z}), c={c:.4f} > z={z}')
                print(f'    x^(n+2)+y^(n+2)={x**(n+2)+y**(n+2)} > z^(n+2)={z**(n+2)}')

if __name__ == '__main__':
    demo()
