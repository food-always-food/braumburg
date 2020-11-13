from flask import Flask
from flask_socketio import SocketIO
import os

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = "1023912038109823aljksdflkajds"
socketio = SocketIO(app,async_mode=None)
app = Flask(__name__)

import app.routes, app.database, app.playerActions

# from app import routes, events, database