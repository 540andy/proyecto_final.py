# BUCLE FOR

#print("Hola andy")

#nombres = ["Andrea", "Juan", "Ana"]

#for elemento in nombres:

#    print(elemento)

#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#  en una lista y la muestre por pantalla. 

#Nombramos la lista y almacenamos los datos 


#materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#print(materias)
#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
# donde <asignatura> es cada una de las asignaturas de la lista.


#Creamos una lista, que almacene los datos

#materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#for materias in materias:
#    print("yo estudio " + materias )

#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.


"""creamos la lista con los datos """

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

""" ahora una lista vacia para almacenar los datos del usuario"""
notas = []


for materias in materias: 

    notas = float(input("¿Què nota has sacado en" + materias + " ?"))

    notas.append(notas)

"""Con un siclo for i in range(()), se imprimiran los datos ingresados por el usuario, asì como tambien la materia """

for i in range(len(materia)):

    print(" En "+ materia [i] + "has sacado" + notas [i])
 

