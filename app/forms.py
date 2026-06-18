from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField


class VideoUploadForm(FlaskForm):
    video = FileField('Upload a video', validators = [FileRequired(), FileAllowed(['mp4', 'mov', 'webm', 'png'],
                'MP4, MOV, or WebM videos only.')])
    submit = SubmitField('Upload')

