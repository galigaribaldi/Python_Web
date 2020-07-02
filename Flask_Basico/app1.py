"""
Primeros intentso con flask
Aplicaicon senccilla sin chiste
"""

from flask import Flask
## pip3 install -U Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo!"

##FLASK_APP=app1.()
##FLASK_ENV=development
##flask run

if __name__ == "__main__":
    app.run()