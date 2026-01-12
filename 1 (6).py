import math

def is_prime_power(n):
    if n < 2:
        return False

    # Try all possible exponents k from 1 up to log2(n)
    max_k = int(math.log(n, 2)) + 1
    for k in range(1, max_k + 1):
        # approximate p = n**(1/k)
        p = round(n ** (1.0 / k))
        if p ** k == n and is_prime(p):
            return True
    return False

def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def number_of_fields(n):
    return 1 if is_prime_power(n) else 0

if __name__ == "__main__":
    n = int(input("Enter n: ").strip())
    print(f"Number of finite fields of order {n}: {number_of_fields(n)}")
