import psycopg2, psycopg2.extras, os, string, random

# host = os.environ['DBHOST']
# database = os.environ['DATABASE']
# user = os.environ['DBUSER']
# password = os.environ['DBPASSWORD']


conn = psycopg2.connect(host=host, database=database, user=user, password=password)

def createCode():
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(5))
    return result_str

def checkGame(strings):
    stmt = f"SELECT * FROM game_instances WHERE code = '{strings}'"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    return result
    
def createGame(name):
    strings = createCode()
    unique = checkGame(strings)
    if len(unique) != 0:
        createGame()
    else:
        stmt = f"INSERT INTO game_instances(code,name) VALUES ('{strings}','{name}')"
        cur = conn.cursor()
        cur.execute(stmt)
        cur.close()
        conn.commit()
        return strings

