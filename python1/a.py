<<<<<<< HEAD
﻿import re
import argparse

def shorten_names(text: str) -> str:
    pattern = re.compile(r'\b([A-Z])[a-z]+\s+([A-Z][a-z]+)\b')
    return pattern.sub(r'\1. \2', text)

def process_bbl(in_path: str, out_path: str):
    with open(in_path, 'r', encoding='utf-8') as f:
        data = f.read()
    new_data = shorten_names(data)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(new_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Convert 'Firstname Lastname' → 'F. Lastname' in a .bbl file"
    )
    parser.add_argument('input', help="Path to your .bbl file")
    parser.add_argument('output', help="Where to write the modified .bbl")
    args = parser.parse_args()

    process_bbl(args.input, args.output)
    print(f"Written shortened names to {args.output}")
=======

>>>>>>> origin/main
