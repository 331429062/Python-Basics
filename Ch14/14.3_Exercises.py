#%%
#Problem 1

from PyPDF2 import PdfMerger
from pathlib import Path

merge_dir = Path(r"C:\Study\Coding\Real_Python Basic\Ch14\Practice_Folder")
merge_file = list(merge_dir.glob("merge[12].pdf"))
merge_file.sort()
output_path = Path.home()/'concatenated.pdf'

pdf_meger = PdfMerger()

for path in merge_file:
    pdf_meger.append(str(path))

with output_path.open(mode='wb') as output_file:
    pdf_meger.write(output_file)

# %%
merge_path = Path.home()/'merged.pdf'
concatenated_path = output_path
merge3_path = merge_dir/'merge3.pdf'

pdf_meger1 = PdfMerger()

pdf_meger1.append(str(concatenated_path))
pdf_meger1.merge(1, str(merge3_path))

with merge_path.open(mode='wb') as output_file:
    pdf_meger1.write(output_file)

