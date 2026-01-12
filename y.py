import sys
import bibtexparser

def format_authors(authors_str):
    """
    Convert "First Middle Last and ..." into
    "F. M. Last and …".
    """
    authors = [a.strip() for a in authors_str.split(" and ")]
    out = []
    for name in authors:
        parts   = name.split()
        initials = " ".join(p[0] + "." for p in parts[:-1])
        surname  = parts[-1]
        out.append(f"{initials} {surname}")
    return " and ".join(out)

def alpha_label(entry):
    """
    Compute a simple label: first three letters of
    the first author’s surname (capitalized) + last two
    digits of the year.
    """
    first_author = entry.get('author', '').split(" and ")[0]
    surname      = first_author.split()[-1]
    year         = entry.get('year', '')
    return surname[:3].capitalize() + year[-2:]

def generate_bbl(bib_path, bbl_path):
    # 1. Load .bib
    with open(bib_path, encoding='utf-8') as bibfile:
        bibdb = bibtexparser.load(bibfile)

    # 2. Prepare labels & find max width for thebibliography env
    labels = [alpha_label(e) for e in bibdb.entries]
    max_label = max(labels, key=len)

    # 3. Write .bbl
    with open(bbl_path, "w", encoding='utf-8') as out:
        out.write(f"\\begin{{thebibliography}}{{{max_label}}}\n\n")

        for entry in bibdb.entries:
            key      = entry.get("ID", "")
            label    = alpha_label(entry)
            authors  = format_authors(entry.get("author", ""))
            title    = entry.get("title", "").rstrip(".,")
            pub      = entry.get("publisher", "")
            year     = entry.get("year", "")

            out.write(f"\\bibitem[{label}]{{{key}}}\n")
            out.write(f"{authors}. {title}. {pub}, {year}.\n\n")

        out.write("\\end{thebibliography}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_bbl.py <input.bib> <output.bbl>")
        sys.exit(1)
    generate_bbl(sys.argv[1], sys.argv[2])
