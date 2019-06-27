from flask import Flask
from flask import render_template, request, flash
from flask import redirect, url_for
import models as coneccion
import sqlite3
app =  Flask(__name__)

##Settings
app.secret_key = 'secreto'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pelicula')
def pelicula():
    return render_template('catalogo.html')

@app.route('/config')
def config():
    datos = coneccion.consulta()
    return render_template('tabla.html', contacts = datos)

@app.route('/add', methods =['POST'])
def add_contact():

    if request.method == 'POST':
        contact_id2 = request.form['contact_id']
        fullname2 = request.form['fullname']
        phone2 = request.form['phone']
        email2 = request.form['email']
        print(contact_id2)
        print(fullname2)
        print(phone2)
        print(email2)
        try:
            coneccion.insertcontactcs(contact_id2, fullname2, phone2, email2)
            flash('El contacto se ha añadido correctamente')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('El contacto no se pudo guardar, ya que este ID ya no esta disponible')
            return redirect(url_for('index'))
    else:
        return render_template('index.html')
@app.route('/edit')
def edit_contact():
    return 'edit'

@app.route('/delete')
def delete_contact():
    return 'delete'

if __name__ == '__main__':
    app.run(debug=True)