from flask import Blueprint

hello = Blueprint('hello',__name__)

@hello.route('/')
@hello.route('/hello')
def fhello():
   return "Hola mundo 3"