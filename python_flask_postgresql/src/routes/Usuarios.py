from flask import Blueprint, jsonify, request, json
from pprint import pprint
import traceback

#Entities
from models.entities.Usuario import Usuario

#Models
from models.UsuariosModel import UsuarioModel

main = Blueprint('usuarios_blueprint', __name__)

@main.route('/')
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<nombre>')
def get_usauario(nombre):
    try:
        usuario = UsuarioModel.get_usuario(str(nombre))

        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_usauario():
    try:
        requestData= request.get_data().decode("utf-8").replace("'", '"')
        requestJson = json.loads(json.loads(requestData))
                    
        nombre = requestJson[0]["nombre"]
        email = requestJson[0]['email']
        clave = requestJson[0]['clave']
        usuario = Usuario("", nombre, email, clave)

        affected_rows = UsuarioModel.add_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.nombre)
        else:
            return jsonify({'message' : "Error on insert"}), 500
    except BaseException as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_usauario(id):
    try:
        requestData= request.get_data().decode("utf-8").replace("'", '"')
        requestJson = json.loads(json.loads(requestData))
        
        nombre = requestJson[0]["nombre"]
        email = requestJson[0]['email']
        clave = requestJson[0]['clave']
        usuario = Usuario(id, nombre, email, clave)

        affected_rows = UsuarioModel.update_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message' : "No usuario update"}), 404
    except BaseException as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario(id)

        affected_rows = UsuarioModel.delete_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message' : "No usuario delete"}), 404
    except BaseException as ex:
        return jsonify({'message': str(ex)}), 500