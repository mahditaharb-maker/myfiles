import math
import matplotlib.pyplot as plt

def n_from_m(m: int) -> int:
    """
    Given an integer m, compute
        x = 10**m * (20 - pi - e**pi)
    and return n = floor(x).
    """
    alpha = -20 +math.pi + math.exp(math.pi)
    x = (10**m) * alpha
    return math.floor(x)

if __name__ == "__main__":
    # Choose a range of m values to explore
    m_values = list(range(0, 100))
    n_values = [n_from_m(m) for m in m_values]

    # Print results
    for m, n in zip(m_values, n_values):
        print(f"m = {m:2d}  →  n = {n}")

    # Plot n versus m
    plt.figure(figsize=(8, 5))
    plt.plot(m_values, n_values, marker='o', linestyle='-')
    plt.xlabel("m", fontsize=12)
    plt.ylabel("n = ⌊10ᵐ·(20 − π − eᵖⁱ)⌋", fontsize=12)
    plt.title("Plot of n versus m", fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
