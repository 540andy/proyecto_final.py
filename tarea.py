#situaciòn: si tu nombre es Andrea, te dire ¡Que gusto verte!, de lo contrario te dire buenas tardes, nombre, Còmo estas?#
#variables#
Nombre1 = "Andrea"
#pedir datos al usurio#
nombre_usuario = input("Ingrese su nombre: ")

if nombre_usuario == Nombre1:
    print(f"Hola, {nombre_usuario}! ¡Qué gusto verte!")
else:
    print(f"Buenas tardes, {nombre_usuario}. ¿Cómo estás?")
