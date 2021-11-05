from flask import render_template
#from flask_socketio import SocketIO

from app import app, socketio
#app.config['SECRET_KEY'] = 'you-never-guess'
#socketio = SocketIo(app)

xyz="El render funciona. Éste párrafo es renderizado y la condición fue procesada por el mismo motor"

@app.route('/')
def home():
    return render_template("index.html", some_text=xyz)

@app.route('/api/')
def api():
    return "Comenzar API..."

@app.route('/socket/')
def sio():
    return render_template("cartas.html", some_text="xyz")


@socketio.event
def first_handler(message):
    emit('server response', {'data': 'got it!'})
