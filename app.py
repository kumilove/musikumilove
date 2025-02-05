from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'About Page'


if __name__ == '__main__':
    app.run()

app.config['UPLOAD_FOLDER'] = './testcases/uploaded_pdfs'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}


def allowed_file(filename):
    if not '.' in filename:
        return False
    ext = filename.rsplit('.', 1)[1]
    if ext in app.config['ALLOWED_EXTENSIONS']:
        return True
    else:
        return False


@app.route('/upload-pdf', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files:
            pdf = request.files['pdfFile']
            if pdf.filename == '':
                print('--------------------IMAGE MUST HAVE A FILE NAME--------------------')
                return redirect(request.url)
            if not allowed_file(pdf.filename):
                print('--------------------ONLY PDF FILES ARE ALLOWED--------------------')
                return redirect(request.url)
            pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))
            print('--------------------IMAGED SAVED--------------------')
            return redirect(request.url)
    return render_template('index.html')
