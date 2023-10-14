import os

import pandas as pd

def html_to_xlsx(link, filename):

    cdf = pd.read_html(link)

    excel_writer = pd.ExcelWriter(os.getcwd() + '\\processed_files\\' + filename + '.xlsx')
    for i, df in enumerate(cdf):
        df.to_excel(excel_writer, sheet_name='Table_' + str(i), index=False)
    excel_writer.close()

    return cdf

