import tabula
import pandas as pd

def pdf_to_excel(file_name):
    src = 'uploads\\' + file_name
    dest = 'processed_files\\' + file_name[:-3] + 'xlsx'

    csv = tabula.read_pdf(src, pages='all')

    excel_writer = pd.ExcelWriter(dest)
    for i, df in enumerate(csv):
        df.to_excel(excel_writer, sheet_name='Table_' + str(i), index=False)
    excel_writer.close()

    return csv

if __name__ == '__main__':
    file_name = 'abc.pdf'

    pdf_to_excel(file_name)