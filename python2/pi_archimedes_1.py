import math

def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2
    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2

def main():
    """
    Try the series
    """
    for n in range(16):
        result = pi_archimedes(n)
        error = result - math.pi
        print("%8d iterations %.10f error %.10f" % (n, result, error))

if __name__ == "__main__":
    main()