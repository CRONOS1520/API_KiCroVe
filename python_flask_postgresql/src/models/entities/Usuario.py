from utils.DateFormat import DateFormat

class Usuario():

    def __init__(self, id, nombre=None, email=None, clave = None, fechaCreacion = None) -> None:
        self.id = id
        self.nombre = nombre
        self.email = email
        self.clave = clave
        self.fechaCreacion = DateFormat.convert_date(fechaCreacion)

    def to_JSON(self):
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'email' : self.email,
            'clave' : self.clave,
            'fechaCreacion' : self.fechaCreacion
        }