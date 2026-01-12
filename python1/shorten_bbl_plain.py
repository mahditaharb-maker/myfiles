#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shorten_bbl_plain.py

Reads a .bbl (or any text) file, shortens capitalized first names (including hyphenated)
to their initials, and writes the result to a new file.

Usage:
    python shorten_bbl_plain.py input.bbl output.bbl
"""

import sys
import re

def shorten_names(text: str) -> str:
    """
    Replace patterns like "Jean-Pierre Serre" → "J.-P. Serre"
    and "Marie Curie" → "M. Curie" throughout the text.
    """
    pattern = re.compile(
        r'\b'                      # word boundary
        r'([A-Z][a-z]+(?:-[A-Z][a-z]+)*)'  # first name, possibly hyphenated
        r'\s+'                     # whitespace
        r'([A-Z][a-z]+)'           # last name
        r'\b'
    )

    def replacer(match: re.Match) -> str:
        first_names = match.group(1).split('-')
        initials = '-'.join(f"{name[0]}." for name in first_names)
        last_name = match.group(2)
        return f"{initials} {last_name}"

    return pattern.sub(replacer, text)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.bbl> <output.bbl>")
        sys.exit(1)

    in_path, out_path = sys.argv[1], sys.argv[2]

    try:
        with open(in_path, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
    except FileNotFoundError:
        print(f"Error: File not found → {in_path}")
        sys.exit(2)

    new_content = shorten_names(content)

    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(new_content)

    print(f"Processed `{in_path}` → `{out_path}` successfully.")


if __name__ == "__main__":
    main()
