from flask import render_template
from app import app

xyz="El render funciona. Éste párrafo es renderizado y la condición fue procesada por el mismo motor"

@app.route('/')
def home():
    return render_template("index.html", some_text=xyz)

@app.route('/api/')
def api():
    return "Comenzar API..."
