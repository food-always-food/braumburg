from flask import render_template
from flask_socketio import SocketIO, emit
from app import app

socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Elysia Von Lucan"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Library", user=user, posts=posts)

if __name__ == '__main__':
    socketio.run(app)