from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import csv
import os
from main import read_csv, Athlete, Score_calculate, json_file


app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/', methods=['GET', 'POST'])
def upload():
      if request.method == 'POST':
         file = request.files['file']
         if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            read_csv(file_path)
            print(json_file)
      return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True)


# python -m flask run