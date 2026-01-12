#!/usr/bin/env python3

import re
import sys

def abbreviate(optional_lbl: str) -> str:
    """
    Turn "Surname(YYYY)" into "SurYY", 
    or fall back to the first 6 alphanumerics.
    """
    m = re.match(r'([^\(]+)\((\d{4})\)', optional_lbl)
    if m:
        surname, year = m.group(1), m.group(2)
        return surname[:3] + year[-2:]
    # fallback: strip non-word chars, limit length
    return re.sub(r'\W+', '', optional_lbl)[:6]

def rewrite_bbl(infile: str, outfile: str):
    # read entire .bbl
    with open(infile, 'r', encoding='utf-8') as f:
        content = f.read()

    # regex to capture [oldLabel]{key}
    pattern = re.compile(r'\\bibitem

\[([^\]

]+)\]

\{([^}]+)\}')

    # replacement callback
    def repl(match):
        old_lbl, key = match.group(1), match.group(2)
        new_lbl = abbreviate(old_lbl)
        return f'\\bibitem[{new_lbl}]' + '{' + key + '}'

    # apply to all bibitems
    new_content = pattern.sub(repl, content)

    # write back
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'Updated .bbl written to: {outfile}')

if __name__ == '__main__':
    if len(sys.argv) not in (2, 3):
        print("Usage: python auto_rename_bbl.py input.bbl [output.bbl]")
        sys.exit(1)
    infile  = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) == 3 else infile
    rewrite_bbl(infile, outfile)
