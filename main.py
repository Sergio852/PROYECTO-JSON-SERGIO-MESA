from funciones import (cargar_datos,listar_informacion_heroes,
                       contar_informacion, buscar_por_nombre,
                       buscar_por_poder, buscar_por_tipo_equipo,)

datos = cargar_datos("datos.json")
opcion = ""

while opcion != "0":
    print(
        """
===== MENU - SUPER ESCUADRON DE HEROES =====
1. Listar informacion de los heroes
2. Contar Informacion
3. Buscar Heroes por su Nombre
4. Buscar Heroes por su poder
5. Buscar Heroes por su tipo de equipo
0.Salir
""")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        listar_informacion_heroes(datos)

    elif opcion == "2":
        contar_informacion(datos)

    elif opcion == "3":
        texto = input("Introduce una parte del nombre del heroe: ")

        if texto == "":
            print("No has escrito nada.")
        else:
            buscar_por_nombre(datos, texto)

    elif opcion == "4":
        poder = input("Introduce el nombre del poder: ")

        if poder == "":
            print("No has escrito ningun poder.")
        else:
            buscar_por_poder(datos, poder)

    elif opcion == "5":
        tipo_equipo = input("Introduce el tipo de equipo (ej.: melee, movilidad, sigilo, vision): ")

        if tipo_equipo == "":
            print("No has escrito ningun tipo de equipo.")
        else:
            buscar_por_tipo_equipo(datos, tipo_equipo)

    elif opcion == "0":
        print("Saliendo del programa...")

    else:
        print("Opcion no valida. Intenta otra vez.")
