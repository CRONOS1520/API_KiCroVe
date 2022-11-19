from database.db import get_connection
from .entities.Notas import Nota

class NotaModel ():

    @classmethod
    def get_nota(self, nombre, fechanota):
        try:
            connection = get_connection()
            notas = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT idnota, titulo, duracion, fechanota, fechafinalizacion, fkestado FROM public.nota 
                WHERE fkusuario = (SELECT idusuario
                                    FROM public.usuario
                                    WHERE nombre = %s) AND DATE(fechanota) = DATE(%s)""",(str(nombre), str(fechanota)))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    nota = Nota(row[0],row[1],row[2],row[3],row[4],row[5])
                    notas.append(nota.to_JSON())                     
            
            connection.close()
            return notas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_nota(self, nota):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.nota (titulo, duracion, fechanota, fkestado, fkusuario) 
                VALUES(%s,%s,%s,%s,%s)""",(nota.titulo, nota.duracion, nota.fechanota, nota.fkestado, nota.fkusuario))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_nota(self, nota):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public.nota SET titulo=%s, duracion=%s, fechanota=%s, fkestado=%s, fechafinalizacion=%s 
                WHERE idnota=%s""",(nota.titulo, nota.duracion, nota.fechanota, nota.fkestado, nota.fechafinalizacion))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_nota(self, nota):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public.nota WHERE idnota = %s""",(nota.id,))
                affected_rows= cursor.rowcount
                connection.commit()                
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)