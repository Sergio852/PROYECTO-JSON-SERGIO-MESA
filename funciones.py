import json


def cargar_datos(nombre_fichero):
    fichero = open(nombre_fichero, "r", encoding="utf-8")
    datos = json.load(fichero)
    fichero.close()
    return datos


def listar_informacion_heroes(datos):
    miembros = datos["miembros"]

    print("\n--- INFORMACION DE LOS HEROES ---")
    for heroe in miembros:
        nombre = heroe["nombre"]
        edad = heroe["edad"]
        identidad = heroe["identidadSecreta"]
        emails = heroe["contacto"]["emails"]
        poderes = heroe["poderes"]

        if identidad is None:
            identidad = "No tiene identidad secreta"

        print("Nombre: " + str(nombre))
        print("Edad: " + str(edad))
        print("Identidad secreta: " + str(identidad))
        print("Numero de emails: " + str(len(emails)) + " │ Poderes: " + str(len(poderes)))
        print("-" * 30)


