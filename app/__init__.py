from flask import Flask
import os

# Get the directory where this file (__init__.py) is located
basedir = os.path.abspath(os.path.dirname(__file__))
# Go up one level to the project root, then to the templates folder
template_dir = os.path.join(os.path.dirname(basedir), 'templates')

app = Flask(__name__, template_folder=template_dir)

from app import routes