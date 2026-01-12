# file: plot_mod_parabola.py
import numpy as np
import matplotlib.pyplot as plt

def bal_mod(y, p):
    """Map y mod p into the balanced range [-(p-1)//2, (p-1)//2]."""
    r = y % p
    half = (p - 1) // 2
    return r - p if r > half else r

def unwrap_parabola(p, x_grid):
    """
    Phase-unwrap the modular outputs r_i = bal_mod(x_i^2, p) so that
    successive differences are chosen with minimal jump (±p adjustment).
    """
    r = np.array([bal_mod(x * x, p) for x in x_grid], dtype=int)
    Y = [int(r[0])]
    halfp = p / 2
    for i in range(1, len(r)):
        d = int(r[i] - r[i - 1])
        if d > halfp:
            d -= p
        elif d < -halfp:
            d += p
        Y.append(Y[-1] + d)
    return np.array(Y, dtype=int)

def main():
    p = 257
    # With step = 1, unwrapping is exact while |2x+1| < p/2.
    # For p=257, choose |x| <= 63 to be safe.
    X = 63
    step = 1

    x = np.arange(-X, X + 1, step, dtype=int)

    # Raw modular values in 0..p-1
    y_mod = np.array([(xi * xi) % p for xi in x], dtype=int)

    # Balanced residues in [-(p-1)//2, (p-1)//2]
    y_bal = np.array([bal_mod(int(yi), p) for yi in y_mod], dtype=int)

    # Unwrapped sequence (recovers x^2 exactly on this range)
    y_unwrap = unwrap_parabola(p, x)

    # True parabola for reference
    y_true = x * x

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(12, 4), dpi=150)

    axs[0].scatter(x % p, y_mod, s=10, color='tab:blue')
    axs[0].set_title('Raw mod p (0..p-1)')
    axs[0].set_xlim(-5, p + 5); axs[0].set_ylim(-5, p + 5)
    axs[0].set_xlabel('x (mod p)'); axs[0].set_ylabel('y (mod p)')

    axs[1].plot(x, y_bal, '.', ms=6, color='tab:orange')
    axs[1].set_title('Balanced residues (folded)')
    axs[1].grid(True, alpha=0.3)
    axs[1].set_xlabel('x'); axs[1].set_ylabel('balanced y')

    axs[2].plot(x, y_unwrap, '-', lw=1.8, label='unwrapped', color='tab:green')
    axs[2].plot(x, y_true, '--', lw=1.2, label='true x^2', color='tab:red')
    axs[2].set_title('Unwrapped vs true parabola')
    axs[2].legend()
    axs[2].grid(True, alpha=0.3)
    axs[2].set_xlabel('x'); axs[2].set_ylabel('y')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
