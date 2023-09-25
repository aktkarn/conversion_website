from pdf2docx import Converter
from docx2pdf import convert
import os

def pdf_to_docx(file_name):

    src = os.getcwd() + '\\uploads\\' + file_name
    dest = os.getcwd() +  file_name[:-3] + 'docx'
    print(dest)
    # Create a PDF to Word converter object
    cv = Converter(src)

    # Convert the PDF to Word
    cv.convert(dest, start=0, end=None)

    # Close the converter
    cv.close()


def docx_to_pdf(file_name):
    src = os.getcwd() + '\\uploads\\' + file_name
    dest = os.getcwd() +  file_name[:-3] + 'pdf'




    # Convert Word to PDF
    convert(src, dest)

if __name__ == '__main__':
    pdf_to_docx("C:\\Users\\Acer\\OneDrive\\Desktop\\Btech_Project_2021_.pdf")
