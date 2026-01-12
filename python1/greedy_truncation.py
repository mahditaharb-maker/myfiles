def greedy_truncation(x: float, k: int) -> list:
    """
    Return the first k bits of the greedy binary expansion of x in [0,1).
    Each bit b_i is determined by multiplying x by 2 and extracting the integer part.
    """
    if not (0 <= x < 1):
        raise ValueError("Input x must be in the interval [0, 1).")
    
    bits = []
    for _ in range(k):
        x *= 2
        bit = int(x)
        bits.append(bit)
        x -= bit
    return bits

# Examples
print("N ->", greedy_truncation(1/2, 1))          # 1/2 in N -> [1]
print("Z ->", greedy_truncation(3/4, 2))          # 3/4 in Z -> [1,1]
print("Q ->", greedy_truncation(5/8, 4))          # 5/8 in Q -> [1,0,1,0]
print("R ->", greedy_truncation(5/8, 16))    # Real number -> 16-bit truncation
