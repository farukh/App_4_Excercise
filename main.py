import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Text+Files/*.txt")
print(filepaths)

pdf = FPDF(orientation='P', format='A4')
for filepath in filepaths:
    filename = Path(filepath).stem
    print(filename)
    pdf.add_page()
    pdf.set_font(family='Times',size=12,style='B')
    pdf.cell(w=50, h=10, txt=filename)


pdf.output('PDFs/Output.pdf')