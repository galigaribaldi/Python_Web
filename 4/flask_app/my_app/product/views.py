from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
#from werkzeug import abort
from sqlalchemy.sql.expression import not_, or_
###Propias
from my_app import db
from my_app.product.model.products import PRODUCTS
from my_app.product.model.product import Product
from my_app.product.model.product import ProductForm


product = Blueprint('product',__name__)

#@product.route('/')
@product.route('/product')
@product.route('/product/<int:page>')
def index(page=1):
   #print(PRODUCTS.items())
   #print(Product.query.all())
   return render_template("product/index.html", products = Product.query.paginate(page, 5))

@product.route('/product/<int:id>')
def show(id):
   products = Product.query.get_or_404(id)
   return render_template("product/show.html", products = products)

@product.route('/product-delete/<int:id>')
def delete(id):
   products = Product.query.get_or_404(id)
   db.session.delete(products)
   db.session.commit()
   flash("Producto eliminado con Exito")
   return redirect(url_for("product.index"))

@product.route('/product-update/<int:id>', methods = ['GET','POST'])
def update(id):
   product = Product.query.get_or_404(id)
   form = ProductForm(meta={'csrf':False})
   if request.method == 'GET':
      form.name.data = product.name
      form.price.data = product.price

   if form.validate_on_submit():
      print("Entro")
      #Actualizar
      product.name = form.name.data
      product.price = form.price.data
      db.session.add(product) ## Creacion de un registro en la base
      db.session.commit()
      flash('Producto Actualizado con exito')   
      return redirect(url_for('product.update', id=product.id))
   if form.errors:
          flash(form.errors,'danger')
   return render_template('product/update.html', product=product, form=form)

@product.route('/product-create', methods = ('GET', 'POST'))
def create():
   form = ProductForm(meta={'csrf': False})
   if form.validate_on_submit():
      p = Product(request.form['name'],request.form['price']) ##Crear un producto
      db.session.add(p) ## Creacion de un registro en la base
      db.session.commit()
      flash('Producto Creado con exito')
      return redirect(url_for('product.create'))
   if form.errors:
      flash(form.errors,'danger')
   return render_template('product/create.html', form=form)


@product.route('/test')
def test():
   #p = Product.query.limit(2).first()
   #p = Product.query.order_by(Product.id.desc()).limit(2).all()
   #p = Product.query.filter_by(name= "Producto 1").all()
   #p = Product.query.filter(Product.id > 1).all()
   #p = Product.query.filter_by(name = "Producto 1", id=1).all()
   #p = Product.query.filter(Product.name.like('P%')).all()
   #print(p)
   #p = Product.query.filter(not_(Product.id > 1)).all()
   #print(p)
   #print(p)
   ##p = Product.query.filter(or_(Product.id > 1, Product.name=="Producto 1")).all()
   #p = Product("P5", 60.8) ##Crear un producto
   #db.session.add(p) ## Creacion de un registro en la base
   #db.session.commit()
   
   #Actualizar
   """
   p = Product.query.filter_by(name = "Producto 1", id=1).first()
   p.name = "UP1"
   db.session.add(p)
   db.session.commit()
   """
   ##Eliminar registro
   p = Product.query.filter_by(id=1).first()
   db.session.delete(p)
   db.session.commit()
   return "Flask"

@product.route('/filter/<int:id>')
def filter(id):
   product = PRODUCTS.get(id)
   return render_template("product/filter.html", products = product)

@product.app_template_filter('iva')
def iva_filter(product):
   if product['price']:
      return product["price"] * .20 + product["price"]
   return "Sin Precio"