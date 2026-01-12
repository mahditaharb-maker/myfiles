import re

def aligned_to_tabular(aligned_text):
    # Remove begin/end markers
    content = re.sub(r'\\begin\{aligned\}|\\end\{aligned\}', '', aligned_text).strip()

    # Split lines by &
    lines = [line.strip() for line in content.split('&') if line.strip()]

    # Prepare tabular rows
    rows = []
    for line in lines:
        # Split by colon or quad (common separator)
        parts = re.split(r':\\quad|:\s*|\\quad', line, maxsplit=1)
        if len(parts) == 2:
            left, right = parts
            rows.append((left.strip(), right.strip()))
        else:
            # Fallback: treat entire line as right side
            rows.append(('', parts[0].strip()))

    # Build LaTeX tabular
    tabular = "\\begin{tabular}{|l|l|}\n\\hline\n"
    for left, right in rows:
        tabular += f"${left}$ & ${right}$ \\\\\n\\hline\n"
    tabular += "\\end{tabular}"

    return tabular

# Example usage
aligned_input = r"""
\begin{aligned}
&\forall\,x,y,z\in A:\;(x+y)+z = x+(y+z),\\
&\forall\,x,y\in A:\;x+y = y+x,\\
&\forall\,x\in A:\;x+0 = x,\quad x+(-x)=0,\\
&\forall\,\lambda,\mu\in\mathbb F_p,\;\forall\,x,y\in A:\\
&\quad (\lambda+\mu)\bullet x = \lambda\bullet x + \mu\bullet x,\\
&\quad \lambda\bullet(x+y) = \lambda\bullet x + \lambda\bullet y,\\
&\quad (\lambda\cdot\mu)\bullet x = \lambda\bullet(\mu\bullet x),\\
&\quad 1\bullet x = x
\end{aligned}
"""

print(aligned_to_tabular(aligned_input))
