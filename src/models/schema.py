
from src.config.db import mysql

class SchemasModel():
    def listarSchemas(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('show databases')
        schemas = cursor.fetchall()
        cursor.close()
        return schemas

    def listarDatabase(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('DESCRIBE persona')
        database = cursor.fetchall()
        cursor.close()
        return database

    def crearSchemes(serlf,nombre_db):
        cursor = mysql.get_db().cursor()
        cursor.execute('CREATE SCHEMA '+ nombre_db)
        mysql.get_db().commit()
        cursor.close()
   
