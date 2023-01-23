"""
Program that can watermark all the pages of a pdf.
"""
import sys
import PyPDF2

template_path = sys.argv[1]
watermark_path = sys.argv[2]
output_path = sys.argv[3]

template = PyPDF2.PdfReader(open(template_path, "rb"))
watermark = PyPDF2.PdfReader(open(watermark_path, "rb"))
output = PyPDF2.PdfWriter()

for page in template.pages:
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open(output_path, "wb") as f:
        output.write(f)

print("Completed!")
