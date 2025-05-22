from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("Files/*.txt")
# Create a pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=8, txt=name, ln=1)

# Produce the output pdf
pdf.output("output.pdf")

