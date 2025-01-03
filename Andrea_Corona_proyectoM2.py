"""
Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta debe tener entre cuatro y ocho letras.
Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique que la palabra es correcta.
Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de la palabra).
Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: “Sobran letras. Tiene N letras” (siendo N el número de letras de la palabra).

"""


#1 Definimos variables que son : (palabra y longitud)
#2 Pedimos al ususrio ingresar una palabra
#Imprimimos un saludo o damos la bienvenida al usuario
print("Bienvenido")
palabra = input("Ingrese una palabra: ")
#la funciòn len() devuelve la longitud de una cadena de texto
longitud=len(palabra)

#  Para realizar las comparaciones y mostrar los mensajes correspondientes usaremos if, elif y else (Operadores lògicos)

if 4 <= longitud <= 8: 
    print(f"La palabra ingresada es correcta y tiene {longitud} letras")
elif longitud <4: 
    print(f"Ups!! a tu palabra le hacen falta letras. solo tiene {longitud} letras.")
else: 
    print(f"Sobran letras. Tiene {longitud} letras.")




print("\n¡Gracias por usar el programa!\n")



"""Crear un programa que en base a 2 números de entrada, coordenadas, 
identifique en cuál de los 4 cuadrantes se encuentra el punto.
 El programa debe verificar que ninguna coordenada sea 0. """

#Definimos valores, este dato es un valor que sera ingresado por el usurio.


x = int ( input ("Ingrese la cordenada en x: "));
y = int ( input ("Ingrese la cordenada en y: "));

 #Se otorgan los valores a x y y, mismos que ingresa el usuario
 #con este siclo de condicionales se podrá mostrar un mensaje indicando en que cuadrante se ubican las coordenadas ingresadas.  



if ((x > 0) and (y > 0 )):
    print("Punto ubicado en el primer cuadrante")
elif    ((x > 0) and (y > 0 )):
    print("Punto ubicado en el sugundo cuadrante")

elif ((x < 0) and (y < 0 )):
    print("Punto ubicado en el tercer cuadrante")

elif ((x < 0) and (y >0 )):
    
    print("Punto ubicado en el cuanto cudrante")

else:
    print("Punto en el origen")

print("vuelva pronto")
