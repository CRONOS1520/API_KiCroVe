from flask import Flask

#Config
from config import config

#Routes
#from routes import Notas
from routes import Usuarios

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__== '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    #app.register_blueprint(Notas.main, url_prefix='/api/notas')
    app.register_blueprint(Usuarios.main, url_prefix='/api/usuarios')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()