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

def contar_informacion(datos):
    miembros = datos["miembros"]
    total_heroes = len(miembros)
    heroes_con_3_poderes = 0
    heroes_con_2_emails = 0

    for heroe in miembros:
        poderes = heroe["poderes"]
        emails = heroe["contacto"]["emails"]

        if len(poderes) >= 3:
            heroes_con_3_poderes = heroes_con_3_poderes + 1
        if len(emails) >= 2:
            heroes_con_2_emails = heroes_con_2_emails + 1

    print("\n--- CONTADORES ---")
    print("Total de heroes en la escuadra: " + str(total_heroes))
    print("Heroes con al menos 3 superpoderes: " + str(heroes_con_3_poderes))
    print("Heroes con al menos 2 emails: " + str(heroes_con_2_emails))
