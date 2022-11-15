from flask import Blueprint, jsonify, request
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

@main.route('/<id>')
def get_usauario(id):
    try:
        usuario = UsuarioModel.get_usuario(id)

        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_usauario():
    try:
        nombre = request.json['nombre']
        email = request.json['email']
        clave = request.json['clave']
        fkusuario = request.json['fkusuario']
        usuario = Usuario("", nombre, email, clave, fkusuario)

        affected_rows = UsuarioModel.add_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id)
        else:
            return jsonify({'message' : "Error on insert"}), 500
    except BaseException as ex:
        print(traceback.format_exc())
        return jsonify({'message': str(traceback.format_exc())}), 500