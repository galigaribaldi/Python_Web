from flask import Blueprint

hello2 = Blueprint('hello2',__name__)


@hello2.route('/hello2')
def hello1():
   return "Hola mundo desde el modulo 2 en la carpeta 3"