import math
from typing import List

def binary_exponents(x: float, n: int) -> List[int]:
    """
    Compute the first n exponents m_k in the expansion
        x = sum_{k=1..∞} 2^{-sum_{i=1..k} m_i}
    using the greedy rule:
        m_k = floor(-log2(x_{k-1})) + 1,
        x_k = 2^{m_k} * x_{k-1} - 1.
    
    Args:
        x: a float in (0, 1)
        n: number of exponents to produce (n >= 1)
    
    Returns:
        A list of length n with the exponents [m1, m2, ..., mn].
    
    Raises:
        ValueError: if x is not in (0,1) or n < 1.
    """
    if not (0.0 < x < 1.0):
        raise ValueError("x must lie in the interval (0,1)")
    if n < 1:
        raise ValueError("n must be at least 1")
    
    exponents: List[int] = []
    x_k = x
    
    for _ in range(n):
        # compute m_k so that 2^{-m_k} < x_k <= 2^{1-m_k}
        m_k = math.floor(-math.log2(x_k)) + 1
        
        # update the “remainder” x_{k} -> x_{k+1}
        x_k = (2 ** m_k) * x_k - 1
        
        exponents.append(m_k)
    
    return exponents

# Example usage:
if __name__ == "__main__":
    x_val = 0.625
    num_terms = 5
    ms = binary_exponents(x_val, num_terms)
    print(f"First {num_terms} exponents for x={x_val} → {ms}")
