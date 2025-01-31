#Repaso de funciones, mòdulos y paquetes. 

#def saludos_2(nombre):
 #  #Definimos la funciòn, es importante mencionar que se estàn usando parametros
  #  print(f"Hola amiga! {nombre}")   

#saludos_2("Angela")    


#funciòn de saludo sin parametros 

#def saludo():
 #   """se define una variable """
  #  nombre = "Andy"
   # print(f"Hola! {nombre} ")

#saludo()

#FUNCIÒN DE SUMA 

#def suma(): 
   
    #"""Definimos variabales"""

   # numero1=int(input("Ingrese el primer nùmero de la suma"))

   # numero2=int(input("Ingrese el segundo nùmero de la suma"))

  #  resultado = numero1 + numero2
 #   print(resultado)

#suma()



# funciòn para obtener el factorial de un nùmero

#def factorial(n):
 #   if n ==0:
  #      return 1
   # else:
    #    return n*factorial(n-1)
    
    
    #numero = int(input("ingrese un numero: "))
    #resultado = factorial(numero)
    #print(resultado)

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("ingrese un numero: "))
try:
    resultado = factorial(numero)
    print(resultado)
except ValueError as e:
    print(e)