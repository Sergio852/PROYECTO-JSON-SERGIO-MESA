# PROYECTO-JSON-SERGIO-MESA
En este repositorio se encuentra el contenido de mi Proyecto JSON
Ejercicio 1 – Listar información
Enunciado:
Escribe un programa que liste la información básica de cada miembro del
equipo:
• Nombre del héroe
• Edad
• Identidad secreta
• Número de contactos de email que tiene
• Número de superpoderes que posee
Objetivo:
Que el programa recorra el array miembros y muestre, para cada héroe, esa
información en formato claro, por ejemplo, una línea o bloque por héroe.
Ejercicio 2 – Contar información
Enunciado:
Escribe un programa que cuente y muestre:
• Cuántos héroes hay en total en la escuadra
• Cuántos héroes tienen al menos 3 superpoderes
• Cuántos héroes tienen al menos 2 emails de contacto
Objetivo:
Contar apariciones de ciertas condiciones, como el número de poderes o el
número de emails, y mostrar los totales.
Ejercicio 3 – Buscar o filtrar información
Enunciado:
Escribe un programa al que el usuario le pase:
• Una subcadena, por ejemplo "Hombre", "Shadow" o "Eternal"
El programa debe:
• Mostrar solo los héroes cuyo nombre contenga esa subcadena
• Para cada héroe encontrado, mostrar nombre, edad, identidad secreta
y la lista de superpoderes
Objetivo:
Filtrar los héroes usando texto introducido por teclado y mostrar solo los
que coincidan.
Ejercicio 4 – Buscar información relacionada
Enunciado:
Escribe un programa que pida al usuario:
• El nombre de un poder, por
ejemplo "Inmortalidad", "Teletransportación" o "Invisibilidad"
El programa debe:
• Buscar qué héroes tienen ese poder en su array poderes
• Para cada héroe que lo tenga, mostrar nombre del héroe, edad,
identidad secreta y número de misiones realizadas
Objetivo:
Partir de un dato, un superpoder, y mostrar la información relacionada, es
decir, los héroes que lo usan y sus datos.
Ejercicio 5 – Ejercicio libre
Enunciado:
Escribe un programa que pida al usuario:
• Un tipo de equipo del héroe, por
ejemplo "sigilo", "melee", "vision" o "movilidad"
El programa debe:
• Recorrer todos los héroes y todos sus equipos en equipo, sin limitarse
solo a algunos miembros
• Mostrar qué héroes poseen al menos un equipo de ese tipo, y para
cada coincidencia indicar:
• Nombre del héroe
• Nombre del equipo
• Tipo de equipo
• Datos adicionales del equipo, si existen, como:
• Multiplicadores de daño, si tiene multiplicadoresDano
• Velocidad máxima, si tiene velocidadMaxKmH
• Consumo de energía por hora, si tiene energiaUsadaPorHora
• Alcance máximo, si tiene rangoMaxMetros
• Si tiene modo térmico, modoTermico, etc.
También debe:
• Listar a todos los héroes que no tienen ningún equipo, indicando solo
su nombre y un mensaje tipo "sin equipo asignado", para obligar a
recorrer todo el array de héroes aunque no tengan equipo
Además, al final debe mostrar estadísticas globales:
• Cuántos equipos de ese tipo hay en total en todo el JSON
• Cuántos héroes distintos tienen al menos un equipo de ese tipo
• El número total de equipos, de cualquier tipo, que hay en la escuadra
• Un pequeño resumen por tipo de equipo, indicando para cada tipo
cuántos equipos hay, por ejemplo: melee: 1, movilidad: 1, sigilo:
1, vision: 1
Objetivo:
Combinar filtro por teclado, recorrido completo de arrays anidados, héroes
→ equipos, tratamiento de héroes sin equipo y cálculo de estadísticas
finales, tanto por tipo como globales.
