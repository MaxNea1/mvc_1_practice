from connexion import *

class Clients:
    def mostrarClientes():
        try:
            db = Database()
            result = db.fetchall("SELECT * FROM tbl_users;")
            db.close()
            return result 
        except Exception as e:
            print("Error al mostrar clientes: ", e)
            return []
        
    def ingresarClientes(name, last_name, gender, age):
        try:
            db = Database()
            result = db.execute("INSERT INTO tbl_users (name, last_name, gender, age) VALUES (?, ?, ?, ?)" \
                                  , (name, last_name, gender, age))
            db.close()
            return result
        except Exception as e:
            print("Error al ingresar cliente: ", e)
            return []
        
    def update(id, name, last_name, gender, age):
        try:
            db = Database()
            result = db.execute("UPDATE tbl_users SET name=?, last_name=?, gender=?, age=? WHERE id=?" \
                                  , (name, last_name, gender, age, id))
            db.close()
            return result
        except Exception as e:
            print("Error al actualizar cliente: ", e)
            return []
        
    def delete(id):
        try:
            db = Database()
            result = db.execute("DELETE FROM tbl_users WHERE id=?" \
                                  , (id))
            db.close()
            return result
        except Exception as e:
            print("Error al eliminar cliente: ", e)
            return []
        
    