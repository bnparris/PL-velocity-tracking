from flask import Flask
from jinja2 import StrictUndefined
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.undefined = StrictUndefined


from app import views