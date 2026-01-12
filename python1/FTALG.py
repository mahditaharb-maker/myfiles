#!/usr/bin/env python3
import numpy as np
import sys

def verify_fta_algebra(max_deg: int = 10, trials: int = 50, tol: float = 1e-6):
    """
    For each degree 1..max_deg, generate `trials` random monic polynomials
    with complex coefficients, find all roots via numpy.roots, and check
    that P(root) ≈ 0 for each root.
    """
    for deg in range(1, max_deg+1):
        for t in range(trials):
            # Random complex coefficients, force leading coeff = 1
            coeffs = (np.random.randn(deg+1) + 1j*np.random.randn(deg+1))
            coeffs[0] = 1
            roots = np.roots(coeffs)
            residuals = np.abs(np.polyval(coeffs, roots))
            if np.max(residuals) > tol:
                raise RuntimeError(
                    f"Bad residual for deg={deg}: max|P(r)|={residuals.max():.2e}"
                )
    print(f"✔ Verified (numerically) every non-constant poly up to degree {max_deg}")

def parse_coeffs(line: str) -> np.ndarray:
    """
    Parse a space-separated list of real or complex literals into a 1D array.
    """
    tokens = line.strip().split()
    try:
        return np.array([complex(tok) for tok in tokens], dtype=complex)
    except ValueError:
        print("Error: could not parse some coefficients as complex numbers.", file=sys.stderr)
        sys.exit(1)

def main():
    # Step 1: Numeric “proof” for random polynomials
    verify_fta_algebra(max_deg=10, trials=50)

    # Step 2: Let user query an arbitrary polynomial
    print()
    print("Now enter your polynomial’s coefficients (highest degree first).")
    print("E.g. for 2x^3 + (1−i)x + 5, type: 2 0 (1-1j) 5")
    line = input("Coeffs> ")
    coeffs = parse_coeffs(line)
    if coeffs.ndim != 1 or len(coeffs) < 2:
        print("Need at least two coefficients (constant + at least one higher term).", file=sys.stderr)
        sys.exit(1)

    roots = np.roots(coeffs)
    print(f"\nFound {len(roots)} root(s):")
    for i, r in enumerate(roots, 1):
        print(f"  root[{i}]: {r.real:.6f} {'+' if r.imag>=0 else '-'} {abs(r.imag):.6f}j")

if __name__ == "__main__":
    main()
