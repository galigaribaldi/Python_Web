from flask import Flask
from flask import request, render_template, url_for

app = Flask(__name__)

@app.route('/primer_html')
@app.route('/primer_html/<name>')

def primer_html(name="Flaskito"):
   return '''
<h1> hola mundo desde flask %s </h1>
''' %name
@app.route('/statics')
def static_f():
   #return "<img src='/static/img/IT.jpg'>"
   return "<img src='"+url_for("static", filename="img/IT.jpg")+"'>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

@app.route('/peliculas')
def peliculas():
    return render_template('pelicula.html')


if __name__ == '__main__':
    app.run(debug = True)