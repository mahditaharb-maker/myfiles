def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    """Find the next prime number greater than n."""
    current = n + 1
    while not is_prime(current):
        current += 1
    return current

# Example usage
current_number =12
print(f"The next prime after {current_number} is {next_prime(current_number)}")
