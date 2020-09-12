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
    background = 'castle.jpg'
    return render_template('index.html', title="Library", user=user, posts=posts, background=background)

# @app.route('/character')
# def character():
#     return "char info"

# @app.route('/map')

@app.route('/goals')
def goals():
    character = {
        "firstName" : "Elysia",
        "lastName" : "Von Lucan",
        "primaryGoal" : "Rid the world of supernatural creatures - its your lifes work afterall and you know waht they say about rest for the wicked. ",
        "secondaryGoal" : "This would be a secondary goal",
        "tertiaryGoal" : "This would be a tertiary goal",
        "winCondition" : "This is your win condition"
    }
    page = {
        "title" : "Goals",
        "background" : "goals/castle.jpg"
    }
    return render_template('goals.html',page = page,character = character)
# @app.route('/items')

# @app.route('/conversations')

# @app.route('/suspects')

@app.route('/help')
def help():
    return 'help'
if __name__ == '__main__':
    socketio.run(app)