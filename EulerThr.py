# EulerThr.py
# 🚀 Symbolic, Numeric & Visual Exploration of Euler’s Theorem

from sympy import symbols, Function, Eq, Mod, totient, Integer
from sympy.abc import a, n
import matplotlib.pyplot as plt
import math

# --- 1. Symbolic Representation ---

phi = Function('phi')
euler_expr = Eq(Mod(a**phi(n), n), 1)

print("🔢 Symbolic form of Euler's Theorem:")
print(euler_expr)

# Plug in specific values symbolically
a_val = Integer(3)
n_val = Integer(10)
phi_val = totient(n_val)  # Sympy.Integer

lhs = Mod(a_val**phi_val, n_val)
rhs = Integer(1)

print(f"\n🧠 Symbolic verification for a = {a_val}, n = {n_val}:")
print(f"{a_val}^{phi_val} mod {n_val} = {lhs} → {'✅' if lhs == rhs else '❌'}")


# --- 2. Numeric Verification for 1 ≤ a < n ≤ 20 ---

def euler_theorem_holds(a: int, n: int) -> bool:
    """
    Check if a^φ(n) ≡ 1 (mod n) when gcd(a,n)=1.
    Cast φ(n) to int so that built-in pow() works.
    """
    if math.gcd(a, n) != 1:
        return False
    phi_n = int(totient(n))   # ← cast Sympy.Integer to native int
    return pow(a, phi_n, n) == 1

print("\n🔍 Verifying Euler's Theorem for values 1 ≤ a < n ≤ 20:")
for N in range(2, 21):
    for A in range(1, N):
        if math.gcd(A, N) == 1:
            ok = euler_theorem_holds(A, N)
            print(f"a = {A:2}, n = {N:2}, φ(n) = {totient(N):2} → {'✅' if ok else '❌'}")


# --- 3. Visualization ---

def plot_euler_mod(n: int):
    """
    Plot a^φ(n) mod n for all a with gcd(a,n)=1.
    """
    phi_n = int(totient(n))
    a_values = [A for A in range(1, n) if math.gcd(A, n) == 1]
    mod_results = [pow(A, phi_n, n) for A in a_values]

    plt.figure(figsize=(10, 5))
    plt.bar(a_values, mod_results, color='skyblue')
    plt.axhline(1, color='red', linestyle='--', label='Expected: 1')
    plt.title(f"Euler's Theorem: $a^{{\\phi({n})}} \\bmod {n}$ for coprime a")
    plt.xlabel("a (coprime to n)")
    plt.ylabel(f"$a^{{\\phi({n})}} \\bmod {n}$")
    plt.xticks(a_values)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example: visualize for n = 15
print("\n📊 Visualizing Euler's Theorem for n = 15...")
plot_euler_mod(15)
