from pdf2docx import Converter

def pdf_to_docx(file_name):

    src = 'uploads\\' + file_name
    dest = 'processed_files\\' + file_name[:-3] + 'docx'
    # Create a PDF to Word converter object
    cv = Converter(src)

    # Convert the PDF to Word
    cv.convert(dest, start=0, end=None)

    # Close the converter
    cv.close()

if __name__ == '__main__':
    # Specify the path of the input PDF file
    pdf_file = 'abc.pdf'

    # Specify the path for the output Word file
    word_file = 'processed_files/abc.docx'

    # Convert PDF to Word
    pdf_to_docx(pdf_file)
