from flask import Flask
##Importamos la librería Flask
from flask import request, render_template, url_for,redirect
from flask import jsonify
##
import Controllers.modelsCreation as crear
##@
import Controllers.modelsOperations as operaciones
app = Flask(__name__)
##Creamos nuestro primer decorador, lo que nos permite crear la ruta principal "/
@app.route("/")
def hello():
    ##Le decimos a nuestra función que retorne "Hola mundo"
    return render_template("index.html")

@app.route("/api")
def api():
    dicccionario = operaciones.consulta()
    return dicccionario

@app.route("/api/CreacionTabla")
def creacion():
    crear.creacion_base()
    return "Tablas Creadas Listo!"

@app.route("/api/EliminarTablas")
def eliminar():
    crear.eliminar_Tablas()
    return "Tablas Eliminadas"

##/api/Insert/register/Amelie/Jean_Pierre_Jeunet/Audrey_Totou/2001/El_fabuloso_destino_de_Amelie
##/api/Insert/register/Requiem_for_a_dream/Darren_Afronosky/Jared_Leto/2001/_
##/api/Insert/register/It/Darren_Afronosky/Jared_Leto/2001/_
@app.route("/api/Insert/register/<movie_name>/<director_name>/<principals_actors>/<movie_year>/<trama_movie>")
def inserts(movie_name,director_name, principals_actors,movie_year,trama_movie):
    ###Leer datos
    movie_name = request.args.get('movie_name',movie_name)
    director_name = request.args.get('director_name',director_name)
    principals_actors = request.args.get('principals_actors',principals_actors)
    movie_year = request.args.get('movie_year',movie_year)
    trama_movie = request.args.get('trama_movie',trama_movie)
    ####CConvertir datos a tuplas
    tupla = (movie_name,director_name, principals_actors,movie_year,trama_movie)
    ###Meter datos
    crear.insercion_datos(tupla,)
    return redirect(url_for('api'))  
if __name__ == "__main__":
    app.run(debug=True,port=5003)