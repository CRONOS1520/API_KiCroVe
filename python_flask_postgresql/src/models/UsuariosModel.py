from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel ():

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT idusuario, nombre, email, clave, fkusuario,
                    fechacreacion FROM public.usuario ORDER BY nombre""")
                resultset = cursor.fetchall()
                
                for row in resultset:
                    usuario = Usuario(row[0],row[1],row[2],row[3],row[4],row[5])
                    usuarios.append(usuario.to_JSON())                     
            
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_usuario(self, id):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT idusuario, nombre, email, clave, fkusuario, 
                    fechacreacion FROM public.usuario WHERE idusuario = %s ORDER BY nombre""",(id,))
                row = cursor.fetchone()
                
                usuario = None
                if row != None:
                    usuario = Usuario(row[0],row[1],row[2],row[3],row[4],row[5])
                    usuario = usuario.to_JSON()                 
            
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.usuario (nombre, email, clave, fkusuario, fechacreacion) VALUE(%s,%s,%s,1 ,now())""",(usuario.nombre, usuario.email, usuario.clave,))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
