from flask import Flask
import os

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = "1023912038109823aljksdflkajds"
from app import routes