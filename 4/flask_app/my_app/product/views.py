from flask import Blueprint, render_template
#from werkzeug import abort
from my_app.product.model.products import PRODUCTS

product = Blueprint('product',__name__)

@product.route('/')
@product.route('/home')
def index():
   #print(PRODUCTS.items())
   #print(PRODUCTS.get(1))
   return render_template("product/index.html", products = PRODUCTS)

@product.route('/product/<int:id>')
def show(id):
   product = PRODUCTS.get(id)
   if not product:
      return "No existe"
   return render_template("product/show.html", products = product)

@product.route('/filter/<int:id>')
def filter(id):
   product = PRODUCTS.get(id)
   return render_template("product/filter.html", products = product)

@product.app_template_filter('iva')
def iva_filter(product):
   if product['price']:
      return product["price"] * .20 + product["price"]
   return "Sin Precio"