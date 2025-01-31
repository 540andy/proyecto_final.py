#listas en python#

numeros = [1,3,4,5,6,7,11]
frutas = [ "sandia","pera","manzana","melón"]
datos = [0, "Juan","pera", "manzana"]
"""
print(datos[2])
print(frutas[1])"""

"""para poder imprimir el último elemento de una lista, podemos utilizar print(nombre de la lista[-1])"""

"""print(números[-1])"""


"""para añadir un elemento a la lista existente usamos nombre de la lista y 
agregamos.append(aqui va el dato a agregar) luego 
print(frutas[-1])
lo aplicamos....."""

"""
frutas.append("frambuesa")

print(frutas[-1])"""

"""para eliminar un elemento en la lista: nombre de la lista seguido de
.remove(aquí va el elemento a eliminar) seguido de  
print(aquí va el nombre de la lista en cuestiòn [-1]), lo aplicamos a la practica"""


#eliminaremos el elemento frambuesa de la lista frutas

"""frutas.remove("frambuesa")
print(frutas[-1])"""


#Utilizamos un ciclo for para imprimir el contenido de una lista: 
"""for i in numeros: 
    print(i)"""

#Tuplas ejemplo 1
"""colores = ("rojo", "azul", "verde", "rosa")
numeros = (1, 2, 4, 4, 6, 1, 1, 1)
#revisar cuantos elementos tiene la lista

print(len(colores))

print(len(números))
# para revisar cuantas veces se repite un dato dentro de una lista o tupla utilizamos; print para imprimir 
# en pantalla
#funciòn dentro del  paréntesis agregando el nombre de la lista màs .count,  màs paréntesis y dentro 
# de él, el dato 
# del cual queremos saber cuantas veces se repite dentro de la tupla o lista.

print(numeros.count(1))"""


#diccionario 
d1 = {
     "Nombre" : " Andrea" ,
     "Edad" : 28,
     "Localidad" : " Edo_de _Mèxico"
}

print(d1)
 