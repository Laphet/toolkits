from PyPDF2 import PdfFileMerger
import string
import glob

pdfname_list = glob.glob('*.pdf')
pdfname_dict = dict(zip(list(string.ascii_letters), pdfname_list))

for key, name in pdfname_dict.items():
    print("{0}:\t{1}".format(key, name))

input_str = input("Set the order of the PDF files (default abcdefg...):")
if (len(input_str) == 0):
    input_str = ''.join(pdfname_dict.keys())

pdfs = []
for key in list(input_str):
    pdfs.append(pdfname_dict.get(key))

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
