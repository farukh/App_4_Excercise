from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Text+Files/*.txt")
print(filepaths)

pdf = FPDF(orientation='P', format='A4')
for filepath in filepaths:
    filename = Path(filepath).stem.title()
    print(filename)
    pdf.add_page()
    pdf.set_font(family='Times',size=12,style='B')
    pdf.cell(w=50, h=10, txt=filename,ln=1)
    with open(filepath,'r') as file:
        file_content = file.read()

    pdf.set_font(family='Times', size=10)
    pdf.multi_cell(w=0,h=6, txt=file_content)


pdf.output('PDFs/Output.pdf')
