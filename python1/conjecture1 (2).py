from typing import Tuple
from decimal import Decimal, getcontext, ROUND_FLOOR
import math

def find_n_decimal(m: int, prec_extra: int = 10) -> Tuple[int, Decimal]:
    """
    Compute 10^m * (e^π - π - 20) with arbitrary precision.
    """
    # set precision: m digits for the scale + guard digits
    getcontext().prec = m + prec_extra

    # approximate pi and compute e^π in Decimal
    D_pi = Decimal(str(math.pi))
    D_e  = Decimal(1).exp()  # this is e
    D_ep = D_e ** D_pi        # e^π

    C = D_ep - D_pi - Decimal(20)
    val = (Decimal(10) ** m) * C
    n = int(val.to_integral_value(rounding=ROUND_FLOOR))
    return n, val

if __name__ == "__main__":
    for m in [10, 20, 30]:
        n, val = find_n_decimal(m)
        print(f"m={m}, n={n}, starts with {str(val)[:20]}…, in interval: {n <= val < n+1}")
