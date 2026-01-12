#!/usr/bin/env python3
import numpy as np

from scipy import integrate
import sys

TOL = 1e-6

#––– 1) Test functions and their known antiderivatives F(x)
tests = [
    {'name': 'x^2+3x+2',
     'f': lambda x: x**2 + 3*x + 2,
     'F': lambda x: x**3/3 + 3*x**2/2 + 2*x},
    {'name': 'sin(x)',
     'f': np.sin,
     'F': lambda x: -np.cos(x)},
    {'name': 'e^(2x)',
     'f': lambda x: np.exp(2*x),
     'F': lambda x: np.exp(2*x)/2},
    {'name': '1/(1+x^2)',
     'f': lambda x: 1/(1+x**2),
     'F': np.arctan},
]

def verify_definite(trials=5):
    """
    Check ∫_a^b f(x) dx ≈ F(b) - F(a) for random [a,b].
    """
    for test in tests:
        f, F, name = test['f'], test['F'], test['name']
        for _ in range(trials):
            a, b = np.random.uniform(-2,2), np.random.uniform(-2,2)
            if a > b: a, b = b, a
            I, _ = integrate.quad(f, a, b)
            diff = F(b) - F(a)
            err = abs(I - diff)
            assert err < TOL*max(1, abs(diff)), (
                f"DefFTC fail for {name} on [{a:.2f},{b:.2f}]: err={err:.2e}"
            )
    print("✔ Definite FTC verified for all test functions.")

def verify_indefinite(points=20, interval=(-2,2), h=1e-5):
    """
    Check d/dx (∫_a0^x f) ≈ f(x) at a grid of points.
    """
    a0 = interval[0]
    for test in tests:
        f, name = test['f'], test['name']
        xs = np.linspace(*interval, points)
        G = lambda x: integrate.quad(f, a0, x)[0]
        for x in xs:
            derivative = (G(x+h) - G(x-h)) / (2*h)
            err = abs(derivative - f(x))
            assert err < TOL*max(1, abs(f(x))), (
                f"IndFTC fail for {name} at x={x:.2f}: err={err:.2e}"
            )
    print("✔ Indefinite FTC verified for all test functions.")

def main():
    # Part A: numeric “proof” on random tests
    verify_definite()
    verify_indefinite()

    # Part B: let user try their own function
    print("\nNow try your own f(x). Use Python syntax (e.g. 'np.sin(x)', 'x**3+1').")
    expr = input("f(x) = ").strip()
    try:
        f = eval("lambda x: " + expr, {'np': np})
    except Exception as e:
        print("Parsing error:", e, file=sys.stderr)
        sys.exit(1)

    print("Enter interval endpoints a, b:")
    a = float(input("a = "))
    b = float(input("b = "))
    I, _ = integrate.quad(f, a, b)
    print(f"\n∫_{a}^ {b} f(x) dx ≈ {I:.6f}")

    # Build F(x)=∫_a^x f(t)dt and compare F'(mid) with f(mid)
    mid = (a + b)/2
    G = lambda x: integrate.quad(f, a, x)[0]
    h = 1e-5
    derivative = (G(mid+h) - G(mid-h)) / (2*h)
    print(f"F'({mid:.6f}) ≈ {derivative:.6f},   f({mid:.6f}) = {f(mid):.6f}")

if __name__ == "__main__":
    main()
