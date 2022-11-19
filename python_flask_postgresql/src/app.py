from flask import Flask
from flask_cors import CORS

#Config
from config import config

#Routes
from routes import Usuarios
from routes import Notas

app = Flask(__name__)

CORS(app)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__== '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Usuarios.main, url_prefix='/usuario')
    app.register_blueprint(Notas.main, url_prefix='/nota')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()