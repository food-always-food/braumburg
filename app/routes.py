from flask import render_template, session, request, redirect, Flask
from flask_socketio import SocketIO, emit, send, join_room
# from app import app
import eventlet
eventlet.monkey_patch()
app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = "1023912038109823aljksdflkajds"
socketio = SocketIO(app,async_mode=None)
import database as database

@app.route('/',methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        req = request.form
        result = database.joinGame(req['code'],req['email'])
        if result != False :
            session['game'] = result['game']
            session['email'] = result['email']
            session['character_id'] = result['character_id']
            session['player_id'] = result['id']
            return redirect("/waiting")
        else:
            return redirect("/")

    else:
        page = {
            "title" : "Welcome to Castle Braumburg",
            "background" : "welcome/enter.jpg"
        }
        return render_template('welcome.html',page = page)

@app.route('/waiting')
def waiting():
    if session.get('game'):
        otherPlayers = database.allPlayers(session.get('game'))
        print("after emit")
        page = {
            "title" : "Waiting for players",
            "background" : "home/home.jpg"
        }
        return render_template('waiting.html',page = page,players=otherPlayers)
    else:
        return redirect("/")

@app.route('/index')
def index():
    if session.get('game'):
        character = database.getCharacter(session.get('character_id'))
        print(character)
        page = {
            "title" : "home",
            "background" : "home/home.jpg"
        }
        return render_template('index.html',page = page,character = character)
    else:
        return redirect("/")

@app.route('/character')
def character():
    if session.get('game'):
        character = database.getCharacter(session.get('character_id'))
        print(character)
        page = {
            "title" : "Character",
            "background" : "character/character.jpg"
        }
        return render_template('character.html',page = page,character = character)
    else:
        return redirect("/")

@app.route('/map')
def map():
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
    return render_template('map.html',page = page,character = character)

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

@app.route('/items')
def items():
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
    return render_template('items.html',page = page,character = character)

@app.route('/conversations')
def conversations():
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
    return render_template('conversations.html',page = page,character = character)

@app.route('/suspects')
def suspects():
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
    return render_template('suspects.html',page = page,character = character)

@app.route('/help')
def help():
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
    return render_template('help.html',page = page,character = character)

@socketio.on('joined')
def send_character(data):
    print(data)
    # if data['data'] =='/waiting':
        # check = 
    character = database.getCharacter(session.get('character_id'))
    socketio.emit("new-player",character,room='waiting',include_self=False)

@socketio.on('connect')
def test_connect():
    print("connected")
    join_room('waiting')
    

if __name__ == '__main__':
    socketio.run(app, debug=True)