import math

def find_n(x: float, k: int, m: int) -> int:
    """
    Compute an integer n such that
      |10**m * (x - k)| ∈ [n, n+1).

    Parameters:
      x (float): the real number
      k (int): an integer (e.g. floor(x))
      m (int): a non-negative integer power

    Returns:
      n (int): floor of |10**m * (x - k)|
    """
    scaled = abs((x - k) * 10**m)
    n = math.floor(scaled)
    return n


# Example usage
if __name__ == "__main__":
    x = 3.14159
    k = math.floor(x)    # 3
    m = 2                # look at the 2nd decimal place
    print(find_n(x, k, m))  # prints 14, since 10^2*(.14159)=14.159 → floor→14
