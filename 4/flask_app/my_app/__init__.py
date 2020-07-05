from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from my_app.product.views import product
## Importando las vistas
app.register_blueprint(product)
db.create_all()
"""
##SQLite
sqlite://database.db
###MySQL
mysql+pymysql://user:password@ip:3306/db_name
##Postgres
postgresql+psycopg2://user:password@ip:port/db_name
postgresql+psycopg2://postgres:postgres@ip:5432/postgres/base2
##MSSQL
mssql+pyodbc://user:password@dsn_name
##Oracle
oracle+cx_oracle://user:password@ip:port/db_name
"""
@app.template_filter('mydouble')
def mydouble_filter(n:int):
    return n*2