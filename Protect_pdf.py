# protect pdf with password
from PyPDF2 import PdfFileWriter,PdfFileReader

def secure_pdf(file,password):
    parser= PdfFileWriter()
    pdf= PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)

    with open(f"encrypted_{file}","wb") as f:
        parser.write(f)
        f.close()

    print(f"encrypted{file} created....")


if __name__=="__main__":
    file= "file_1.pdf"
    password="thisismypassword"
    secure_pdf(file,password)

