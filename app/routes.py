from flask import render_template, session, request, redirect
from flask_socketio import SocketIO, emit
from app import app

socketio = SocketIO(app)

@app.route('/',methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        req = request.form
        print(req)
        return redirect("/index")
    else:
        character = {
            "firstName" : "Elysia",
            "lastName" : "Von Lucan",
            "primaryGoal" : "Rid the world of supernatural creatures - its your lifes work afterall and you know waht they say about rest for the wicked. ",
            "secondaryGoal" : "This would be a secondary goal",
            "tertiaryGoal" : "This would be a tertiary goal",
            "winCondition" : "This is your win condition"
        }
        page = {
            "title" : "Welcome to Castle Braumburg",
            "background" : "welcome/enter.jpg"
        }
        return render_template('welcome.html',page = page,character = character)

@app.route('/index')
def index():
    character = {
        "firstName" : "Elysia",
        "lastName" : "Von Lucan",
        "primaryGoal" : "Rid the world of supernatural creatures - its your lifes work afterall and you know waht they say about rest for the wicked. ",
        "secondaryGoal" : "This would be a secondary goal",
        "tertiaryGoal" : "This would be a tertiary goal",
        "winCondition" : "This is your win condition"
    }
    page = {
        "title" : "Home",
        "background" : "home/home.jpg"
    }
    return render_template('index.html',page = page,character = character)

@app.route('/character')
def character():
    character = {
        "firstName" : "Elysia",
        "lastName" : "Von Lucan",
        "primaryGoal" : "Rid the world of supernatural creatures - its your lifes work afterall and you know waht they say about rest for the wicked. ",
        "secondaryGoal" : "This would be a secondary goal",
        "tertiaryGoal" : "This would be a tertiary goal",
        "winCondition" : "This is your win condition"
    }
    page = {
        "title" : "Character",
        "background" : "character/character.jpg"
    }
    return render_template('character.html',page = page,character = character)

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
if __name__ == '__main__':
    socketio.run(app)