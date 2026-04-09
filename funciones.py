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

def buscar_por_nombre(datos, texto):
    miembros = datos["miembros"]
    texto = texto.lower()
    encontrado = False

    print("\n--- BUSQUEDA POR NOMBRE ---")
    for heroe in miembros:
        nombre = heroe["nombre"]

        if texto in nombre.lower():
            encontrado = True
            edad = heroe["edad"]
            identidad = heroe["identidadSecreta"]
            poderes = heroe["poderes"]

            if identidad is None:
                identidad = "No tiene identidad secreta"

            print("Nombre: " + str(nombre))
            print("Edad: " + str(edad))
            print("Identidad secreta: " + str(identidad))
            print("Poderes:")
            for poder in poderes:
                print("- " + str(poder))
            print("-" * 30)

    if encontrado == False:
        print("No se ha encontrado ningun heroe con ese nombre o texto.")

def buscar_por_poder(datos, nombre_poder):
    miembros = datos["miembros"]
    nombre_poder = nombre_poder.lower()
    encontrado = False

    print("\n--- BUSQUEDA POR PODER ---")
    for heroe in miembros:
        poderes = heroe["poderes"]

        for poder in poderes:
            if poder.lower() == nombre_poder:
                encontrado = True
                nombre = heroe["nombre"]
                edad = heroe["edad"]
                identidad = heroe["identidadSecreta"]
                misiones = heroe["misiones"]

                if identidad is None:
                    identidad = "No tiene identidad secreta"

                print("Nombre: " + str(nombre))
                print("Edad: " + str(edad))
                print("Identidad secreta: " + str(identidad))
                print("Numero de misiones: " + str(len(misiones)))
                print("-" * 30)
                break

    if encontrado == False:
        print("No existe ningun heroe con ese poder.")


