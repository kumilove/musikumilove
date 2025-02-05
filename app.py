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

app.config['UPLOAD_FOLDER'] = './testcases/uploaded_images'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.lower() in app.config['ALLOWED_EXTENSIONS']:
        return True
    else:
        return False


@app.route('/upload-image', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        if request.files:

            image = request.files['image']

            if image.filename == '':
                print('--------------------IMAGE MUST HAVE A FILE NAME--------------------')
                return redirect(request.url)

            if not allowed_file(image.filename):
                print('--------------------ONLY PDF, PNG, JPG, AND JPEG ARE ALLOWED--------------------')
                return redirect(request.url)

            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

            print('--------------------IMAGED SAVED--------------------')
            
            return redirect(request.url)

    return render_template('index.html')
