import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(k):
    lower = 2 ** k
    upper = 2 ** (k + 1)
    count = 0
    for n in range(lower + 1, upper):
        if is_prime(n):
            count += 1
    return count

# Example usage
k = int(input("Enter k: "))
print(f"Number of primes between 2^{k} and 2^{k+1}:", count_primes_in_range(k))
