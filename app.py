
from flask import Flask, render_template, request, send_file
import shutil  # shutil.copy(src, dst) can be used for pdf copy
import os
from html_to_xlsx import *
from pdf_to_xlsx import *
from pdf_to_docx import *
from html_to_pdf import *

app = Flask(__name__)

if os.path.exists('uploads'):
    shutil.rmtree('uploads')
os.mkdir('uploads')

if os.path.exists('processed_files'):
    shutil.rmtree('processed_files')
os.mkdir('processed_files')

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        option = request.form['option']
        if option == 'none':
            return render_template('index.html', message='Invalid option selected.')
        elif ('html' in option) or ('link' in option):
            link = request.form['link']
            filename = os.path.basename(link)
            do_the_job(filename, link, option)
            return render_template('index.html', filename_source=filename, filename_output=filename + '.xlsx',
                                   option=option, message='File uploaded successfully.')
        else:
            file = request.files['file']
            filename = file.filename
            pos_of_convert_from = len(filename) - filename.find('.')
            file.save(os.path.join('uploads', filename))
            pos_of_convert_to = option.find('to') + 3
            do_the_job(filename, file, option)
            return render_template('index.html', filename_source=filename, filename_output=filename[:-pos_of_convert_from+1] + option[pos_of_convert_to:], option=option, message='File uploaded successfully.')

    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    file_path = os.path.join('processed_files', filename)
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    return 'File not found.'


@app.route('/close/<filename>', methods=['GET'])
def close(filename):
    option = request.args.get('option')  # Retrieve the 'option' parameter from the URL query string
    file_source = os.getcwd() + '\\uploads\\' + filename
    file_dest_in = os.getcwd() + '\\processed_files\\' + filename
    pos_of_convert_from = len(filename) - filename.find('.')
    pos_of_convert_to = option.find('to') + 3
    file_dest_out = os.getcwd() + '\\processed_files\\' + filename[:-pos_of_convert_from + 1] + option[pos_of_convert_to:]

    os.remove(file_source)
    os.remove(file_dest_in)
    os.remove(file_dest_out)

    return render_template('successful_deletion.html', success_message='File Removed Successfully')

@app.route('/close', methods=['GET'])
def close():
    return (render_template('successful_deletion.html', success_message='No Files To Be Deleted'))



def do_the_job(filename, file, convert_A_to_B=None):

    if convert_A_to_B == 'pdf_to_xlsx':
        shutil.copy(os.getcwd() + '\\uploads\\' + filename, os.getcwd() + '\\processed_files\\' + filename)
        df_list = pdf_to_xlsx(filename) ## this gives list of different tables in the pdf
    elif convert_A_to_B == 'xlsx_to_pdf':
        shutil.copy(os.getcwd() + '\\uploads\\' + filename, os.getcwd() + '\\processed_files\\' + filename)
        xlsx_to_pdf(file_name)
    elif convert_A_to_B == 'html_to_xlsx':
        df_list = html_to_xlsx(file, filename)
    elif convert_A_to_B == 'html_to_pdf':
        html_to_pdf(file)
    elif convert_A_to_B == 'pdf_to_docx':
        shutil.copy(os.getcwd() + '\\uploads\\' + filename, os.getcwd() + '\\processed_files\\' + filename)
        pdf_to_docx(filename)
    elif convert_A_to_B == 'docx_to_pdf':
        shutil.copy(os.getcwd() + '\\uploads\\' + filename, os.getcwd() + '\\processed_files\\' + filename)
        docx_to_pdf(filename)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    # app.run(debug=True)