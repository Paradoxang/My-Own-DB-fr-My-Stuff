from conexionDb import ConexionDB

# Crear una instancia de la conexión a la base de datos
conexion = ConexionDB(user='Paradoxa', password='FanMiranda10')

# Crear bases de datos para cada tipo de contenido
dbs = ['pelicula', 'serie', 'comic', 'manga', 'anime', 'videojuego', 'libro','manwha']
for db_name in dbs:
    conexion.crear_db(db_name)

def crear_documento(db_name, data):
    conexion.crear_documento(db_name, data)

def obtener_documento(db_name, doc_id):
    return conexion.obtener_documento(db_name, doc_id)

def actualizar_documento(db_name, doc_id, data):
    conexion.actualizar_documento(db_name, doc_id, data)

def eliminar_documento(db_name, doc_id):
    conexion.eliminar_documento(db_name, doc_id)

def obtener_todos_documentos(db_name):
    db = conexion.obtener_db(db_name)
    if db:
        return [doc for doc in db]
    else:
        return []

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Crear documento")
    print("2. Obtener documento")
    print("3. Actualizar documento")
    print("4. Eliminar documento")
    print("5. Mostrar todos los documentos")
    print("6. Salir")
#3