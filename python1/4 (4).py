import math

def test_formula_k_nonzero(x, max_k=100, max_m=10):
    for k in range(1, max_k):  # start from k = 1 to ensure k ≠ 0
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

# Try it on some sample values
x_samples = [0.999, 2.5, math.pi, 7.77]
for x in x_samples:
    result, k_val = test_formula_k_nonzero(x)
    print(f"x = {x:.6f}: Formula {'holds' if result else 'fails'} with k ≠ 0 (k = {k_val})")
