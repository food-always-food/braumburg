import psycopg2, psycopg2.extras, os, string, random

# host = os.environ['DBHOST']
# database = os.environ['DATABASE']
# user = os.environ['DBUSER']
# password = os.environ['DBPASSWORD']
host = "kandula.db.elephantsql.com"
database = "fitzqquu"
user = "fitzqquu"
password = "NGdqfudlPXsoy9IJoeQPvN_TrYggqtLY"

conn = psycopg2.connect(host=host, database=database, user=user, password=password)


def createCode():
    letters = string.ascii_uppercase
    result_str = "".join(random.choice(letters) for i in range(5))
    return result_str


def checkGame(strings):
    stmt = f"SELECT * FROM game_instances WHERE code = '{strings}'"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    return result


def checkPlayer(castleCode, email):
    stmt = f"SELECT * FROM player_characters WHERE game = '{castleCode}' AND email='{email}'"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    return result


def createGame(name, length, email):
    strings = createCode()
    unique = checkGame(strings)
    if len(unique) != 0:
        createGame(name, length, email)
    else:
        stmt = f"INSERT INTO game_instances(code,name,status,length) VALUES ('{strings}','{name}','waiting','{length}')"
        cur = conn.cursor()
        cur.execute(stmt)
        cur.close()
        conn.commit()
        result = joinGame(
            strings, email, "TRUE"
        )  # Identify Primary user on the creation.
        return result


def getCharacter(charId):
    stmt = f"SELECT * FROM characters WHERE id = '{charId}'"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    return result


def addPlayer(castleCode, email, primary):
    options = [1, 2, 3, 4, 5, 6]
    taken = [0]
    stmt = f"SELECT character_id FROM player_characters WHERE game = '{castleCode}'"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    if len(result) != 0:
        for x in result:
            taken.append(int(x["character_id"]))
    available = list(set(options) - set(taken))
    if len(available) != 0:
        choice = random.choice(available)
        stmt = f"INSERT INTO player_characters(game,email,character_id,primary_player) VALUES ('{castleCode}','{email}',{choice},{primary})"
        cur = conn.cursor()
        cur.execute(stmt)
        cur.close()
        conn.commit()
        result = checkPlayer(castleCode, email)
        return result
    else:
        return False


def joinGame(castleCode, email, primary):
    castleCode = castleCode.upper()
    check_game = checkGame(castleCode)
    if len(check_game) == 0:
        print("Game Doesn't Exist")
        return False
    elif check_game[0]["status"] == "waiting":
        check_player = checkPlayer(castleCode, email)
        if len(check_player) == 0:
            add = addPlayer(castleCode, email, primary)
            if add == False:
                print("Game is full")
                return False
            else:
                return add[0]
        else:
            print("player is already in the game")
            return check_player[0]  # Return the player in the game

    else:
        print("Game is no longer accepting players")
        return False


def allPlayers(code):
    stmt = f"SELECT c.id, c.title, c.first_name, c.last_name, c.public_description FROM player_characters pc LEFT JOIN characters c ON c.id = pc.character_id WHERE pc.game = '{code}'"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    return result


def sendChat(code, room, message, player):
    cur = conn.cursor()
    cleaned = psycopg2.extensions.QuotedString(message)
    stmt = f"INSERT INTO chat (game, room, message, player) VALUES ('{code}','{room}',{cleaned},'{player}')"
    cur.execute(stmt)
    cur.close()
    conn.commit()
    return True


def retrieveChatState(code, room):
    stmt = f"SELECT * FROM chat WHERE game = '{code}' AND room = '{room}' ORDER BY created_at"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    return result
