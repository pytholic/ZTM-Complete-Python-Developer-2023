import PyPDF2

with open("./dummy.pdf", "rb") as f:  # read binary
    reader = PyPDF2.PdfFileReader(f)
    # print(reader.numPages)
    # print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    # add the modifed page
    writer.addPage(page)
    with open("tilt.pdf", "wb") as f_out:
        writer.write(f_out)
