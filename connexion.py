import pyodbc

class Database:

    def __init__(self):
        try:
            self.connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=NEAL\\SQLEXPRESS;'
                'DATABASE=test1;'
                'Trusted_connection=yes;'
            )

            self.cursor = self.connection.cursor()

            print("Conexion exitosa")
        except Exception as e:
            print('Error al conectar a la base de datos:', e)

    def execute(self, query, params=()):
        try: 
            self.cursor.execute(query, params)
            self.connection.commit()

            print('Query ejecutado correctamente')

        except Exception as e:
            print('Error al ejecutar query: ', e)
        
    def fetchall(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            print('Error al obtener datos: ', e)
            return []
    def close(self):
        try: 
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print('Conexion cerrada')
        except Exception as e:
            print('Error al cerrar la conexion: ', e)