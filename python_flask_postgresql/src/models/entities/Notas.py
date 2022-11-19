from utils.DateFormat import DateFormat

class Nota():

    def __init__(self, id, titulo=None, duracion=None, fechanota = None, fechafinalizacion = None,fkestado = None, fkusuario = None ) -> None:
        if(type(fechanota) == str):
            self.fechanota = fechanota
        else:
            self.fechanota = DateFormat.convert_date_hour(fechanota)

        if(type(fechanota) == str):
            self.fechafinalizacion = fechafinalizacion
        else:
            self.fechafinalizacion = DateFormat.convert_date_hour(fechafinalizacion)

        self.id = id
        self.titulo = titulo
        self.duracion = str(duracion)
        self.fkestado = str(fkestado)
        self.fkusuario = str(fkusuario)

    def to_JSON(self):
        return {
            'id' : self.id,
            'titulo' : self.titulo,
            'duracion' : self.duracion,
            'fechanota' : self.fechanota,
            'fechafinalizacion' : self.fechafinalizacion,
            'fkestado' : self.fkestado,
            'fkusuario' : self.fkusuario,
        }