from funciones import (cargar_datos,listar_informacion_heroes)

datos = cargar_datos("datos.json")
opcion = ""

while opcion != "0":
    print(
        """
===== MENU - SUPER ESCUADRON DE HEROES =====
1. Listar informacion de los heroes
""")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        listar_informacion_heroes(datos)

    
