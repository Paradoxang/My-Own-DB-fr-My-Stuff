import logica

def solicitar_datos():
    datos = {}
    datos["_id"] = input("Ingrese el ID del documento: ")
    datos["titulo"] = input("Nombre del Contenido?: ")
    datos["año_visto"] = input("Ingrese el año en el que se vivió el contenido: ")
    datos["autor"] = input("Ingrese el autor/creador: ")
    datos["mes_leido"] = input("Ingrese el mes en el que se vivió el contenido: ")
    datos["genero"] = input("Ingrese el género (separado por comas si es más de uno) ").split(", ")
    datos["calificacion_0_10"] = input("Calificación de Cero a Diez ")
    datos["comentarios_personales"] = input("Ingrese comentarios: ")
    return datos


def main():
    while True:
        logica.mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de documento (pelicula, serie, comic, manga, manwha, anime, videojuego, libro): ")
            if tipo in logica.dbs:
                datos = solicitar_datos()
                logica.crear_documento(tipo, datos)
            else:
                print("Tipo de documento no válido.")
        elif opcion == "2":
            tipo = input("Ingrese el tipo de documento (pelicula, serie, comic, manga, manwha, anime, videojuego, libro): ")
            if tipo in logica.dbs:
                doc_id = input("Ingrese el ID del documento: ")
                doc = logica.obtener_documento(tipo, doc_id)
                if doc:
                    print(doc)
            else:
                print("Tipo de documento no válido.")
        elif opcion == "3":
            tipo = input("Ingrese el tipo de documento (pelicula, serie, comic, manga, manwha, anime, videojuego, libro): ")
            if tipo in logica.dbs:
                doc_id = input("Ingrese el ID del documento a actualizar: ")
                nuevos_datos = solicitar_datos()
                logica.actualizar_documento(tipo, doc_id, nuevos_datos)
            else:
                print("Tipo de documento no válido.")
        elif opcion == "4":
            tipo = input("Ingrese el tipo de documento (pelicula, serie, comic, manga, manwha, anime, videojuego, libro): ")
            if tipo in logica.dbs:
                doc_id = input("Ingrese el ID del documento a eliminar: ")
                logica.eliminar_documento(tipo, doc_id)
            else:
                print("Tipo de documento no válido.")
        elif opcion == "5":
            tipo = input("Ingrese el tipo de documento (pelicula, serie, comic, manga, manwha, anime, videojuego, libro): ")
            if tipo in logica.dbs:
                documentos = logica.obtener_todos_documentos(tipo)
                if documentos:
                    for doc_id in documentos:
                        print(logica.obtener_documento(tipo, doc_id))
                else:
                    print(f"No hay documentos en la base de datos '{tipo}'.")
            else:
                print("Tipo de documento no válido.")
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()