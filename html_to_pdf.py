import pdfkit

def html_to_pdf(link):
    # Set the path to the `wkhtmltopdf` executable
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')

    # Convert website to PDF
    pdfkit.from_url('http://example.com', '/path/to/output.pdf', configuration=pdfkit_config)