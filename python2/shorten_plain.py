from datetime import datetime

def generate_bibtex(entry_type, author, title, publisher, year):
    # Parse author name
    parts = author.split()
    last_name = parts[-1]
    initials = '. '.join([p[0] for p in parts[:-1]]) + '.'
    short_author = f"{initials} {last_name}"

    # Generate citation key like Gou97
    key = f"{last_name[:3]}{str(year)[-2:]}"  # e.g., Gou97

    # Format BibTeX entry
    bibtex = f"""@{entry_type}{{{key},
  author    = {{{short_author}}},
  title     = {{{title}}},
  publisher = {{{publisher}}},
  year      = {{{year}}},
}}"""
    return bibtex


print(entry)
