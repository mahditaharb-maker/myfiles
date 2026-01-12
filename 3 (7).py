import math

def test_formula(x, max_k=100, max_m=10):
    for k in range(max_k):  # Try different values of k
        valid_for_all_m = True
        for m in range(max_m):
            value = abs(10**m * (x - k))
            n = math.floor(value)
            if not (n <= value <= n + 1):
                valid_for_all_m = False
                break
        if valid_for_all_m:
            return True, k
    return False, None

# Example usage
x_values = [2**0.5, 2.718, 0.123456]
for x in x_values:
    result, k_val = test_formula(x)
    print(f"x = {x:.6f}: Formula {'holds' if result else 'fails'} (k = {k_val})")
