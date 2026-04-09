from funciones import (cargar_datos,listar_informacion_heroes,
                       contar_informacion, buscar_por_nombre)

datos = cargar_datos("datos.json")
opcion = ""

while opcion != "0":
    print(
        """
===== MENU - SUPER ESCUADRON DE HEROES =====
1. Listar informacion de los heroes
2. Contar Informacion
3. Buscar Heroes por su Nombre
0.Salir
""")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        listar_informacion_heroes(datos)
    elif opcion == "2":
        contar_informacion(datos)
    elif opcion == "3":
        buscar_por_nombre(datos)
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opcion no valida. Intenta otra vez.")

    
