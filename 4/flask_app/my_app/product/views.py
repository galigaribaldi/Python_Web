from flask import Blueprint, render_template
#from werkzeug import abort
from my_app.product.model.products import PRODUCTS
from my_app.product.model.product import Product
from sqlalchemy.sql.expression import not_, or_

product = Blueprint('product',__name__)

@product.route('/')
@product.route('/home')
def index():
   #print(PRODUCTS.items())
   print(Product.query.all())
   return render_template("product/index.html", products = Product.query.all())

@product.route('/product/<int:id>')
def show(id):
   products = Product.query.get_or_404(id)
   return render_template("product/show.html", products = products)

@product.route('/test')
def test():
   #p = Product.query.limit(2).first()
   #p = Product.query.order_by(Product.id.desc()).limit(2).all()
   #p = Product.query.filter_by(name= "Producto 1").all()
   #p = Product.query.filter(Product.id > 1).all()
   #p = Product.query.filter_by(name = "Producto 1", id=1).all()
   p = Product.query.filter(Product.name.like('P%')).all()
   print(p)
   p = Product.query.filter(not_(Product.id > 1)).all()
   print(p)
   p = Product.query.filter(or_(Product.id > 1, Product.name=="Producto 1")).all()
   print(p)
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