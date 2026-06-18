#from email_validator import validate_email, EmailNotValidError
from flask import render_template, send_from_directory, redirect, url_for
from app.forms import VideoUploadForm
#, redirect, url_for, request, flash, send_from_directory)

from uuid import uuid4
from werkzeug.utils import secure_filename
from app import app
#from app.forms import RegistrationForm, ImageUploadForm, CSVUploadForm, ItemForm
import os
from config import Config


#import csv

def silent_remove(filepath):
    try:
        os.remove(filepath)
    except:
        pass


@app.route('/', methods = ['GET', 'POST'])
def home():
    form = VideoUploadForm()
    vid_exists = None
    filename=None
    if form.validate_on_submit():
        unique_str = str(uuid4())
        filename = secure_filename(f'{unique_str}-{form.video.data.filename}')
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        form.video.data.save(filepath)
        vid_exists = True
    return render_template('upload_video.html', title='Upload Video', form = form, vid_exists = vid_exists, filename = filename)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory("data/uploads", filename)



@app.route('/menu')
def menu():
    return render_template('menu.html', title ='Menu')
