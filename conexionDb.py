import os
import couchdb

import couchdb


class ConexionDB:
    def __init__(self, url='http://127.0.0.1:5984/', user='Paradoxa', password='FanMiranda10'):
        self.url = url
        if user and password:
            self.url = f"http://{user}:{password}@{url.split('://')[1]}"
        self.server = couchdb.Server(self.url)

    def crear_db(self, db_name):
        if db_name in self.server:
            print(f"La base de datos '{db_name}' ya existe.")
        else:
            self.server.create(db_name)
            print(f"Base de datos '{db_name}' creada.")

    def obtener_db(self, db_name):
        if db_name in self.server:
            return self.server[db_name]
        else:
            print(f"La base de datos '{db_name}' no existe.")
            return None

    def crear_documento(self, db_name, data):
        db = self.obtener_db(db_name)
        if db:
            doc_id, doc_rev = db.save(data)
            print(f"Documento creado con ID: {doc_id} y revisión: {doc_rev}")

    def obtener_documento(self, db_name, doc_id):
        db = self.obtener_db(db_name)
        if db and doc_id in db:
            return db[doc_id]
        else:
            print(f"Documento con ID '{doc_id}' no encontrado en la base de datos '{db_name}'.")
            return None

    def actualizar_documento(self, db_name, doc_id, data):
        db = self.obtener_db(db_name)
        if db and doc_id in db:
            doc = db[doc_id]
            for key, value in data.items():
                doc[key] = value
            db.save(doc)
            print(f"Documento con ID '{doc_id}' actualizado.")
        else:
            print(f"Documento con ID '{doc_id}' no encontrado en la base de datos '{db_name}'.")

    def eliminar_documento(self, db_name, doc_id):
        db = self.obtener_db(db_name)
        if db and doc_id in db:
            db.delete(db[doc_id])
            print(f"Documento con ID '{doc_id}' eliminado de la base de datos '{db_name}'.")
        else:
            print(f"Documento con ID '{doc_id}' no encontrado en la base de datos '{db_name}'.")

#2