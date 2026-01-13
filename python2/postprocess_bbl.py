import re
import sys

def rewrite_bbl(infile: str, outfile: str):
    # Read original .bbl
    with open(infile, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: (\bibitem[ ... ]{cohen1993})
    pattern = r'(\\bibitem

\[)[^\]

]+(\]

\{cohen1993\})'
    replacement = r'\1Coh93\2'

    # Perform replacement
    new_content = re.sub(pattern, replacement, content)

    # Write out updated .bbl
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Written updated bibliography to {outfile}")

if __name__ == '__main__':
    if len(sys.argv) not in (2, 3):
        print("Usage: python update_bbl.py input.bbl [output.bbl]")
        sys.exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) == 3 else infile
    rewrite_bbl(infile, outfile)
