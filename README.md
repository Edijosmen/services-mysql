# services-mysql
crear el entorno virtual

Flask-MySQL es una extensión de Flask que le permite acceder a una base de datos MySQL.
# command
pip install flask-mysql

# rutas
listas tablas
http://127.0.0.1:5000/schemas       method GET

crear tablas
http://127.0.0.1:5000/createschemas method POST

{
	"nombre_db": "nombre_tabla"
}

listar detalle tabla
http://127.0.0.1:5000/databasedetalle
