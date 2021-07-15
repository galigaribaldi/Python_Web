# -*- coding: utf-8 -*-
import psycopg2
import pandas as pd
###################     Credenciales de la base       #####################
host = 'ec2-3-224-97-209.compute-1.amazonaws.com'
database = 'dene0v98k37avo'
user = 'ksjonfrbmgzqnj'
password = 'e7ee067d0498d23210a9f46e979961ac80a034ddd6d7038e321b581cfddc750d'

def consulta():
    query = "SELECT * FROM pelicula;"
    datos = pd.read_sql(query, con=psycopg2.connect(host=host, database=database, user=user, password=password))
    datosJson = datos.to_json()
    print(datosJson)
    return datos, datosJson