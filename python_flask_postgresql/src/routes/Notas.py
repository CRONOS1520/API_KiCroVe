from flask import Blueprint, jsonify, request, json
from pprint import pprint
import traceback

#Entities
from models.entities.Notas import Nota

#Models
from models.NotasModel import NotaModel

main = Blueprint('notas_blueprint', __name__)

@main.route('/<nombreusuario>/<fecha>')
def get_nota(nombreusuario = None, fecha = None):
    try:

        nota = NotaModel.get_nota(nombreusuario, fecha)
        print(nota)
        if nota != None:
            return jsonify(nota)
            
        else:
            return jsonify({}), 404
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_nota():
    try:
        print(request.get_data())
        requestData= request.get_data().decode("utf-8").replace("'", '"')
        requestJson = json.loads(json.loads(requestData))
                    
        titulo = requestJson[0]["titulo"]
        duracion = requestJson[0]['duracion']
        fkestado = requestJson[0]['fkestado']
        fechanota = requestJson[0]['fechanota']
        fkusuario = requestJson[0]['fkusuario']
        nota = Nota("", titulo, duracion, fechanota,None, fkestado, fkusuario)

        affected_rows = NotaModel.add_nota(nota)

        if affected_rows == 1:
            return jsonify(nota.titulo)
        else:
            return jsonify({'message' : "Error on insert"}), 500
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_nota(id):
    try:
        requestData= request.get_data().decode("utf-8").replace("'", '"')
        requestJson = json.loads(json.loads(requestData))
        
        titulo = requestJson[0]["titulo"]
        duracion = requestJson[0]['duracion']
        fkestado = requestJson[0]['fkestado']
        fechanota = requestJson[0]['fechanota']
        fechafinalizacion = requestJson[0]['fechafinalizacion']
        nota = Nota(id, titulo, duracion, fechanota, fechafinalizacion, fkestado)

        affected_rows = NotaModel.update_nota(nota)

        if affected_rows == 1:
            return jsonify(nota.id)
        else:
            return jsonify({'message' : "No nota update"}), 404
    except BaseException as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_nota(id):
    try:
        nota = Nota(id)

        affected_rows = NotaModel.delete_nota(nota)

        if affected_rows == 1:
            return jsonify(nota.id)
        else:
            return jsonify({'message' : "No nota delete"}), 404
    except BaseException as ex:
        print(traceback.format_exc())
        return jsonify({'message': str(traceback.format_exc())}), 500
