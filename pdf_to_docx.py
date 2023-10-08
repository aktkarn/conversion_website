from pdf2docx import Converter
import win32com.client as win32
from docx import Document
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
    dest = os.getcwd() +  file_name[:-3] + 'docx'
    # Create a new Word application instance
    word_app = win32.gencache.EnsureDispatch('Word.Application')

    # Open the Word document
    doc = word_app.Documents.Open(src)

    # Save the document as PDF
    doc.SaveAs(dest, FileFormat=17)

    # Close the document and quit the Word application
    doc.Close()
    word_app.Quit()

if __name__ == '__main__':
    pdf_to_docx('')
