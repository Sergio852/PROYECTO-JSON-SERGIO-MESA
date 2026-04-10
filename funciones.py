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


def buscar_por_tipo_equipo(datos, tipo):
    miembros = datos["miembros"]
    tipo = tipo.lower()
    total_equipos_tipo = 0
    total_equipos = 0
    heroes_con_tipo = []
    resumen_tipos = {}

    print("\n--- BUSQUEDA POR TIPO DE EQUIPO ---")

    for heroe in miembros:
        nombre_heroe = heroe["nombre"]
        equipos = heroe.get("equipo", [])

        if len(equipos) == 0:
            print(nombre_heroe + ": sin equipo asignado")
        else:
            for equipo in equipos:
                total_equipos = total_equipos + 1
                tipo_equipo = equipo["tipo"]

                if tipo_equipo in resumen_tipos:
                    resumen_tipos[tipo_equipo] = resumen_tipos[tipo_equipo] + 1
                else:
                    resumen_tipos[tipo_equipo] = 1

                if tipo_equipo.lower() == tipo:
                    total_equipos_tipo = total_equipos_tipo + 1

                    if nombre_heroe not in heroes_con_tipo:
                        heroes_con_tipo.append(nombre_heroe)

                    print("Heroe: " + str(nombre_heroe))
                    print("Equipo: " + str(equipo["nombre"]))
                    print("Tipo: " + str(tipo_equipo))

                    if "multiplicadoresDano" in equipo:
                        print("Multiplicadores de daño: " + str(equipo["multiplicadoresDano"]))
                    if "velocidadMaxKmH" in equipo:
                        print("Velocidad maxima: " + str(equipo["velocidadMaxKmH"]) + " km/h")
                    if "energiaUsadaPorHora" in equipo:
                        print("Consumo de energia por hora: " + str(equipo["energiaUsadaPorHora"]))
                    if "rangoMaxMetros" in equipo:
                        print("Rango maximo: " + str(equipo["rangoMaxMetros"]) + " metros")
                    if "modoTermico" in equipo:
                        print("Modo termico: " + str(equipo["modoTermico"]))
                    if "nivelBateria" in equipo:
                        print("Nivel de bateria: " + str(equipo["nivelBateria"]))
                    
                    print("-" * 30)

    if total_equipos_tipo == 0:
        print("No existe ningun equipo de ese tipo de equipo.")

    print("\n--- ESTADISTICAS FINALES ---")
    print("Equipos del tipo '" + str(tipo) + "': " + str(total_equipos_tipo))
    print("Heroes distintos con ese tipo de equipo: " + str(len(heroes_con_tipo)))
    print("Numero total de equipos en la escuadra: " + str(total_equipos))
    print("Resumen por tipo de equipo:")

    for tipo_equipo in resumen_tipos:
        print("- " + str(tipo_equipo) + ": " + str(resumen_tipos[tipo_equipo]))
