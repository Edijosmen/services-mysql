from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.schema import SchemasModel

@app.route('/schemas', methods=['GET'])
def schemas():
    schemasModel = SchemasModel()
    schemas = schemasModel.listarSchemas()
    return jsonify({"Schemas":schemas})

@app.route('/databasedetalle', methods=['GET'])
def database():
    schemasModel = SchemasModel()
    database = schemasModel.listarDatabase()
    return jsonify({"database":database})

@app.route("/createschemas", methods=["POST"])
def createSchemas():
    schemasModel = SchemasModel()
    request_data = request.get_json()
    nombre_db = request.json['nombre_db']
    schemasModel.crearSchemes(nombre_db)
    return 'OK'
