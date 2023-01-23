import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_merge(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged.pdf")


pdf_merge(inputs)
