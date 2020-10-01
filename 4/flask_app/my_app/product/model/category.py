from my_app import db
##Importaciones para fomrularios
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import InputRequired

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    products = db.relationship('Product', backref='category', lazy='select')
    ##La data es cargada hasta que se consulta = Carga floja
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Category %r>'%(self.name)
        
class CategoryForm(FlaskForm):
    name = StringField('Nombre', validators=[InputRequired()])
    
    