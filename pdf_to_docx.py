import fitz  # PyMuPDF
from docx2pdf import convert
import os

def pdf_to_docx(file_name):

    src = os.getcwd() + '\\uploads\\' + file_name
    dest = os.getcwd() + '\\processed_files\\' + file_name[:-3] + 'docx'

    # Open the PDF file
    pdf_document = fitz.open(src)

    # Create a new Word document
    doc = Document()

    # Loop through each page in the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)

        # Extract text from the PDF page
        page_text = page.get_text()

        # Add the extracted text to the Word document
        doc.add_paragraph(page_text)

    # Save the Word document
    doc.save(dest)



def docx_to_pdf(file_name):
    src = os.getcwd() + '\\uploads\\' + file_name
    dest = os.getcwd() + '\\processed_files\\' + file_name[:-3] + 'pdf'
    # Specify the path of the input Word document
    word_file = 'src'

    # Specify the path for the output PDF file
    pdf_file = 'dest'

    # Convert Word to PDF and save to the specified location
    convert(word_file, pdf_file)

if __name__ == '__main__':
    pdf_to_docx('')
