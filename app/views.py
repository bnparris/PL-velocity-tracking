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
    if form.validate_on_submit():
        unique_str = str(uuid4())
        filename = secure_filename(f'{unique_str}-{form.video.data.filename}')
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        form.video.data.save(filepath)
        return redirect(url_for('analyse_video', filename = filename))
    return render_template('upload_video.html', title='Upload Video', form = form)

@app.route('/analyse_video/<filename>', methods = ['GET', 'POST'])
def analyse_video(filename):
    return render_template('analyse_video.html', filename= filename)


@app.route('/video_path/<filename>')
def video_path(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)

