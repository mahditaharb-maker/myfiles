import math

def find_n_float(m: int) -> tuple[int, float]:
    """
    Compute 10^m * (e^π - π - 20) using double precision,
    return n = floor(value) and the value itself.
    """
    # constant = e^π - π - 20
    C = math.e**math.pi - math.pi - 20
    val = (10 ** m) * C
    n = math.floor(val)
    return n, val

if __name__ == "__main__":
    print(" m |      n |      value       | in [n, n+1]?")
    print("---|--------|------------------|-------------")
    for m in range(0, 10):
        n, val = find_n_float(m)
        ok = (n <= val < n + 1)
        print(f"{m:2d} | {n:6d} | {val:16.12f} | {ok}")
