#%%
#Problem 1
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pdf_path = Path(r"C:\Study\Coding\Real_Python Basic\Ch14\Practice_Folder\Pride_and_Prejudice.pdf")
input_pdf = PdfReader(str(pdf_path))

pdf_writer = PdfWriter()
last_page = input_pdf.pages[-1]
pdf_writer.add_page(last_page)


with Path('last_page.pdf').open(mode='wb') as output_file:
    pdf_writer.write(output_file)

# %%
#Problem 2
pdf_path = Path(r"C:\Study\Coding\Real_Python Basic\Ch14\Practice_Folder\Pride_and_Prejudice.pdf")
input_pdf = PdfReader(str(pdf_path))
output_pdf = Path.home()/'every_other_page.pdf'

pdf_writer = PdfWriter()

for page in input_pdf.pages[::2]:
    pdf_writer.add_page(page)

with output_pdf.open(mode='wb') as output_file:
    pdf_writer.write(output_file)
# %%
# Problem 3

pdf_path = Path(r"C:\Study\Coding\Real_Python Basic\Ch14\Practice_Folder\Pride_and_Prejudice.pdf")
pdf = PdfReader(str(pdf_path))
pdf_writer1 = PdfWriter()
pdf_writer2 = PdfWriter()

for page in pdf.pages[:(len(pdf.pages)//2)]:
    pdf_writer1.add_page(page)

with (Path.home()/'part_1.pdf').open(mode='wb') as output_file1:
    pdf_writer1.write(output_file1)

for page in pdf.pages[(len(pdf.pages)//2):]:
    pdf_writer2.add_page(page)

with (Path.home()/'part_2.pdf').open(mode='wb') as output_file2:
    pdf_writer2.write(output_file2)
# %%
