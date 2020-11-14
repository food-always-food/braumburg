from flask import render_template, session, request, redirect, Flask
from flask_socketio import SocketIO, emit, send, join_room

# from app import app, socketio
import eventlet

eventlet.monkey_patch()
app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config["SECRET_KEY"] = "1023912038109823aljksdflkajds"
socketio = SocketIO(app, async_mode=None)
import database


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        req = request.form
        result = database.joinGame(req["code"], req["email"], False)
        if result != False:
            session["game"] = result["game"]
            session["email"] = result["email"]
            session["character_id"] = result["character_id"]
            session["player_id"] = result["id"]
            return redirect("/conversations")
        else:
            return redirect("/")
    else:
        page = {
            "title": "Welcome to Castle Braumburg",
            "background": "welcome/castle.jpg",
        }
        return render_template("welcome.html", page=page)


@app.route("/create-game", methods=["GET", "POST"])
def create_game():
    if request.method == "POST":
        req = request.form
        result = database.createGame(req["name"], req["length"], req["email"])
        session
        print(req)
        # result = database.joinGame(req['code'],req['email'])
        if result != False:
            session["game"] = result["game"]
            session["email"] = result["email"]
            session["character_id"] = result["character_id"]
            session["player_id"] = result["id"]
            return redirect("/conversations")
        else:
            return redirect("/")
        return "hello"

    else:
        page = {
            "title": "Welcome to Castle Braumburg",
            "background": "welcome/enter.jpg",
        }
        return render_template("create_game.html", page=page)


@app.route("/waiting")
def waiting():
    if session.get("game"):
        otherPlayers = database.allPlayers(session.get("game"))
        page = {"title": "Waiting for players", "background": "home/home.jpg"}
        return render_template("waiting.html", page=page, players=otherPlayers)
    else:
        return redirect("/")


@app.route("/index")
def index():
    if session.get("game"):
        character = database.getCharacter(session.get("character_id"))
        print(character)
        page = {"title": "home", "background": "home/home.jpg"}
        return render_template("index.html", page=page, character=character)
    else:
        return redirect("/")


@app.route("/character")
def character():
    if session.get("game"):
        character = database.getCharacter(session.get("character_id"))
        print(character)
        page = {"title": "Character", "background": "character/character.jpg"}
        return render_template("character.html", page=page, character=character)
    else:
        return redirect("/")


@app.route("/map")
def map():
    page = {"title": "Goals", "background": "goals/castle.jpg"}
    return render_template("map.html", page=page)


@app.route("/goals")
def goals():
    page = {"title": "Goals", "background": "goals/castle.jpg"}
    return render_template("goals.html", page=page)


@app.route("/items")
def items():
    page = {"title": "Goals", "background": "goals/castle.jpg"}
    return render_template("items.html", page=page, character=character)


@app.route("/conversations")
def conversations():
    if session.get("game"):
        playerId = session.get("character_id")
        you = database.getCharacter(playerId)
        players = database.allPlayers(session.get("game"))
        links = []
        index = 0
        for x in players:
            if x["id"] != playerId:
                order = [int(x["id"]), int(playerId)]
                print(order)
                ordered = sorted(order)
                print(ordered)
                link = f"{ordered[0]}-{ordered[1]}"
                links.append(link)
                players[index]["link"] = link
            index += 1
        print(links)
        page = {"title": "Conversations", "background": "conversations/chat.jpg"}
        return render_template(
            "conversations.html",
            page=page,
            players=players,
            localPlayer=playerId,
            you=you,
        )
    else:
        return redirect("/")


@app.route("/chat<id>")
def chat(id):
    if session.get("game"):
        playerId = session.get("character_id")
        you = database.getCharacter(playerId)
        step1 = id.replace(str(playerId), "")
        otherPlayerId = step1.replace("-", "")
        otherPlayer = database.getCharacter(int(otherPlayerId))
        session["player_name"] = you[0]["first_name"] + " " + you[0]["last_name"]
        print(session["player_name"])
        session["other_player_name"] = (
            otherPlayer[0]["first_name"] + " " + otherPlayer[0]["last_name"]
        )
        print(session["other_player_name"])
        chatState = database.retrieveChatState(session.get("game"), id)
        session["room"] = id
        page = {
            "title": "Chat With "
            + otherPlayer[0]["first_name"]
            + " "
            + otherPlayer[0]["last_name"],
            "background": "conversations/chat.jpg",
        }
        return render_template(
            "chat.html",
            page=page,
            chats=chatState,
            localPlayer=session.get("character_id"),
            you=you,
            them=otherPlayer,
        )
    else:
        return redirect("/")


@app.route("/suspects")
def suspects():
    if session.get("game"):
        you = database.getCharacter(session.get("character_id"))
        players = database.allPlayers(session.get("game"))
        page = {"title": "Suspects", "background": "goals/castle.jpg"}
        return render_template(
            "suspects.html",
            page=page,
            you=you,
            players=players,
            localPlayer=session.get("character_id"),
        )
    else:
        return redirect("/")


@app.route("/help")
def help():
    if session.get("game"):
        you = database.getCharacter(session.get("character_id"))
        page = {"title": "Help", "background": "goals/castle.jpg"}
        return render_template("help.html", page=page, you=you)
    else:
        return redirect("/")


@socketio.on("joined")
def send_character(data):
    print(data)
    if data["data"] == "/waiting":
        join_room(data["data"])
        character = database.getCharacter(session.get("character_id"))
        socketio.emit("new-player", character, room=data["data"], include_self=False)
    else:
        join_room(data["data"])
        character = database.getCharacter(session.get("character_id"))
        socketio.emit("chatJoin", character, room=request.sid)


@socketio.on("connect")
def test_connect():
    print("connected")


@socketio.on("chatSent")
def chat_sent(data):
    print(session.get("room"))
    database.sendChat(
        session.get("game"), session.get("room"), data["data"], data["player"]
    )
    data["sender"] = session.get("player_name")
    emit("chat", data, room=("/chat" + session.get("room")))
    print(data)


@socketio.on("chatJoined")
def chat_joined(data):
    pass


if __name__ == "__main__":
    socketio.run(app, debug=True)
