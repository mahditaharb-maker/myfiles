def find_solutions(p=257):
    sols = []
    for x in range(p):
        x2 = (x * x) % p
        for y in range(p):
            if (x2 + y * y) % p == 0:
                sols.append((x, y))
    return sols

if __name__ == "__main__":
    solutions = find_solutions()
    print(f"Total solutions: {len(solutions)}")
    # Uncomment to see all pairs
    # print(solutions)
