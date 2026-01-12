from mpmath import mp, floor

def compute_n(m: int) -> int:
    """
    For a given nonnegative integer m, compute
    n = floor(10^m * (e^π - π - 20))
    using mpmath at precision m+10 digits.
    """
    # Set decimal precision to m+10 significant digits
    mp.dps = m + 10

    # Compute the constant e^π - π - 20
    const = mp.e**mp.pi - mp.pi - 20

    # Scale by 10^m and take the floor
    scaled = const * mp.mpf(10) ** m
    return int(floor(scaled))

# Example usage
if __name__ == "__main__":
    for m in [ 50, 70]:
        print(f"m = {m:2d} → n = {compute_n(m)}")
