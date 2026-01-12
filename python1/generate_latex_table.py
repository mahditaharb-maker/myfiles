def generate_latex_table(p):
    if p < 2 or any(p % i == 0 for i in range(2, int(p**0.5) + 1)):
        raise ValueError("Input must be a prime number.")

    # Header row
    header = "a \\backslash b & " + " & ".join(str(b) for b in range(p)) + " \\\\\n\\hline"

    # Body rows
    rows = []
    for a in range(p):
        row_vals = [(a**2 + b**2) % p for b in range(p)]
        row = f"{a} & " + " & ".join(str(val) for val in row_vals) + " \\\\"
        rows.append(row)

    # Combine into LaTeX array environment
    latex_code = "\\begin{array}{c|" + "c" * p + "}\n"
    latex_code += header + "\n" + "\n".join(rows) + "\n\\end{array}"

    return latex_code

# Example usage
p = 7
print(generate_latex_table(p))
