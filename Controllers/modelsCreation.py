# -*- coding: utf-8 -*-
import psycopg2
###################     Credenciales de la base       #####################
host = 'ec2-3-224-97-209.compute-1.amazonaws.com'
database = 'dene0v98k37avo'
user = 'ksjonfrbmgzqnj'
password = 'e7ee067d0498d23210a9f46e979961ac80a034ddd6d7038e321b581cfddc750d'
def creacion_base():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE pelicula(
	                    movie_id serial PRIMARY KEY,
                    	movie_name character varying(100),
                    	director_name character varying(100),
                        principals_actors character varying(200),
                        movie_year character varying(100),
                        trama_movie character varying(400)
                    );
                   """)
    conexion.commit()
    cursor.close()
    conexion.close()
    
def insercion_datos(tupla):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("""INSERT INTO pelicula(movie_name,director_name, principals_actors,movie_year,trama_movie)
                   VALUES """+str((tupla)))
    conexion.commit()
    cursor.close()
    conexion.close()
    
def eliminar_Tablas():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("""DROP TABLE pelicula;
                   """)
    conexion.commit()
    cursor.close()
    conexion.close()