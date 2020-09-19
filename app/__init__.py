from flask import Flask
# from flask_socketio import SocketIO
import os

app = Flask(__name__)

from app import routes, events, database