def find_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit):
        for b in range(a, limit):  # start from a to avoid duplicate pairs
            c_sq = a**2 + b**2
            c = int(c_sq**0.5)
            if c >= limit:
                continue
            if c*c == c_sq:
                triples.append((a, b, c))
    return triples

# Find and print triples where c < 100
triples = find_pythagorean_triples(10000000000)
for t in triples:
    print(t)
