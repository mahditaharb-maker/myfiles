# Define the value of t
t = 2
modulus = t**10

# Check all values of x modulo t^2
print(f"Solutions to x^2 + x ≡ {t} mod {modulus}:\n")
for x in range(modulus):
    lhs = (x**2 + x) % modulus
    if lhs == t:
        print(f"x = {x} is a solution since {x}^2 + {x} ≡ {lhs} mod {modulus}")
