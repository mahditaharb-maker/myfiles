from fpdf import FPDF

def sanitize(text):
    # replace any characters not supported by latin‐1
    replacements = {
        "’": "'",
        "–": "-",
        "“": '"',
        "”": '"',
        "•": "-",
        "π": "pi",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, sanitize("Algebraic Calculus One - Wildberger/Anna Tomskova"), ln=True, align="C")
pdf.ln(5)

content = [
    ("1. Introduction to Algebraic Calculus", [
        ("Invitation to a more logical, solid and careful analysis", "https://www.youtube.com/watch?v=rTw6XbmO8Nc")
    ]),
    # … (other sections truncated for brevity)
]

pdf.set_font("Arial", 'B', 14)
for section, items in content:
    pdf.cell(0, 10, sanitize(section), ln=True)
    pdf.set_font("Arial", 'B', 12)
    for title, url in items:
        # 1) Print the title (wrapped if needed)
        pdf.set_x(10)
        pdf.multi_cell(0, 8, sanitize(f"- {title}:"), align="L")
        # 2) Now insert the URL via write(); this will make it clickable
        pdf.set_text_color(0, 0, 255)
        pdf.write(8, sanitize(url), url)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(8)
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 14)

pdf.output("Algebraic_Calculus_Index_fixed.pdf")
