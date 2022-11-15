from flask import Blueprint, jsonify

main = Blueprint('notas_blueprint', __name__)

@main.route('/')
def get_notas():
    return jsonify({'message': "KiCroVe"})
