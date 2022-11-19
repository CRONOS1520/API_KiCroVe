from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel ():

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT idusuario, nombre, email, clave, fechacreacion FROM public.usuario ORDER BY nombre""")
                resultset = cursor.fetchall()
                
                for row in resultset:
                    usuario = Usuario(row[0],row[1],row[2],row[3],row[4])
                    usuarios.append(usuario.to_JSON())                     
            
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_usuario(self, nombre):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT idusuario, nombre, email, clave, fechacreacion FROM public.usuario 
                WHERE nombre = %s ORDER BY nombre""",(nombre,))
                row = cursor.fetchone()
                
                usuario = None
                if row != None:
                    usuario = Usuario(row[0],row[1],row[2],row[3],row[4])
                    usuario = usuario.to_JSON()                 
            
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.usuario (nombre, email, clave) VALUES(%s,%s,%s)""",(usuario.nombre, usuario.email, usuario.clave,))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public.usuario SET nombre=%s, email=%s, clave=%s WHERE idusuario=%s""",(usuario.nombre, usuario.email, usuario.clave,usuario.id))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public.usuario WHERE idusuario = %s""",(usuario.id,))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
