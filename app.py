from main import read_csv, create_download_file, sort, sorted_json_file
from flask import Flask, render_template, request, redirect, url_for, send_file
from flask.helpers import flash
import os, time


app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv'}
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload():
      if request.method == 'POST':
         file = request.files['file']
         if file.filename != '':
            if file and allowed_file(file.filename):
               file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
               file.save(file_path)
               read_csv(file_path)
               sort()
               time.sleep(2)
               create_download_file()
            else:
               flash('wrong file format!')
               return redirect(url_for('index'))
      return redirect(url_for('download'))

@app.route('/download/', methods=['GET', 'POST'])
def download():
   #  uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_file('output.json',
                     mimetype='text/csv',
                     as_attachment=True)

if __name__ == '__main__':
   app.run(debug=True)


# python -m flask run