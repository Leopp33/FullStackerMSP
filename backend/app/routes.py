from app import app

@app.route('/')
def home():
    return "Hola desde Flask"