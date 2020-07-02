from my_app import app

@app.route('/hello2')
def hello():
   return "Hola mundo desde el modulo 2"