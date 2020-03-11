from flask import Flask,request,render_template,session,jsonify
import json
from flask_socketio import SocketIO, send,emit
from DBHandler import DBHandler
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
#app.debug = False
#FLASK_DEBUG = True
app.config.from_object('config')

@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template("index.html")

'''def test():
    return "My Hello"
abc.add_url_rule("/test","tt",test)'''


@app.route('/login.html')
def login():
    return render_template('login.html', error=' ')
@app.route('/signin', methods=['POST', 'GET'])
def signin():
    error = None
    db = None
    try:
        print("Test")
        email = request.form['email']
        password = request.form['password']
        print(app.config["DATABASEIP"])
       # db = DBHandler(app.config["DATABASEIP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        db = DBHandler('ec2-3-230-106-126.compute-1.amazonaws.com', 'rjdqdaixwfulmb','b43a475916746b10cce21e133f699cb2477aaf138ecfe422b97542b34242d9e5','d7vaaedjhcibvb')
        #db = DBHandler('localhost','postgres', 'tomhanks11','postgres')
        resulte=db.isAlreadyTaken(email)
        resultp=db.existPass(password)
        if(resulte==False and resultp==True):
            done = db.signin(email, password)
            session['name'] = done
            session['email'] = email
            print(done)
            session['wins']=db.getWins(session['email'])
            session['lose']=db.getLoses(session['email'])
            return render_template('profile.html',error=' ')
        else:
            return render_template('login.html', error='Email or Password is Wrong ')
    except Exception as e:
        print(e)
        error = str(e)
        return render_template('login.html', error=error)





@app.route('/login.html')
@app.route('/signup', methods=['POST','GET'])
def signup():
    error = None
    db = None
    try:
        print("Test")

        email = request.form['email']
        password = request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        print(app.config["DATABASEIP"])
        print("ussama")

       # db = DBHandler(app.config["DATABASEIP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        db = DBHandler('ec2-3-230-106-126.compute-1.amazonaws.com', 'rjdqdaixwfulmb','b43a475916746b10cce21e133f699cb2477aaf138ecfe422b97542b34242d9e5','d7vaaedjhcibvb')
        #db = DBHandler('localhost', 'postgres', 'tomhanks11', 'postgres')
        result=db.isAlreadyTaken(email)
        if(result==True):
            done = db.signup(email,password,fname,lname)
            print(done)
            return render_template('login.html',error=' ')
        else:
            return render_template('login.html',error='Email Already Taken')


    except Exception as e:
        print(e)
        error = str(e)
        return render_template('login.html', error=error)
socketio = SocketIO(app)
clients=[]
players=[]
playerscount=0
@app.route('/play')
def sessions():
    global playerscount
    playerscount=playerscount+1
    if(playerscount<=4):
        players.append(session['email'])
        return render_template('Ludo-game.html', name=session['name'])
    else:
        errorMessange = "Sorry the game is full."
        playerscount=playerscount-1
        return render_template('profile.html', error= errorMessange)


@socketio.on('message')
def handleMessage(arg1, arg2, arg3, arg4, arg5,arg6):
    print('Message: ',arg1,arg2,arg3,arg4,arg5,arg6)
    print(arg4)
    #db = DBHandler(app.config["DATABASEIP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    db = DBHandler('ec2-3-230-106-126.compute-1.amazonaws.com', 'rjdqdaixwfulmb','b43a475916746b10cce21e133f699cb2477aaf138ecfe422b97542b34242d9e5','d7vaaedjhcibvb')
    #db = DBHandler('localhost', 'postgres', 'tomhanks11', 'postgres')
    if (arg5):
        clients.append(arg5)
    if(arg6<5):
        if(arg6==0):
            db.winlose(players[0],players[1],players[2],players[3])
        if (arg6 == 1):
            db.winlose(players[1], players[0], players[2], players[3])
        if (arg6 == 2):
            db.winlose(players[2], players[1], players[0], players[3])
        if (arg6 == 3):
            db.winlose(players[3], players[1], players[2], players[0])
    x = {
        "dice": arg1,
        "color": arg2,
        "pawnno": arg3,
        "text": arg4,
        "socketid":clients,
        "playerscount":playerscount
    }
    y=json.dumps(x)

    send(y, broadcast=True)



if __name__ == '__main__':
    socketio.run(app)
    #socketio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
