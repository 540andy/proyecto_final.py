#calculadora 

"""Definimos funciones"""


def suma (a, b): 
    return a + b

def resta (a, b ): 
    return a - b
 
def multiplicacion (a, b ): 
    return a * b 
def division  (a, b ): 
    return a / b 


cerrarPrograma = False

"""Buble while, en donde el còdigo  dentro del bucle se ejecutara: 
mientras la condiciòn sea verdadera
not cerrarPrograma: 
esta parte del bucle se ejecutara mientras cerrarPprograma sea False el bucle continuara ejecutandose
  """
while not cerrarPrograma: 
          
    print("Elìge una opciòn: \n1: Suma\n2: Resta\n3: Multiplicaciòn\n4: Divisiòn\n0: Salir")  

    opcion= int(input("Opciòn:   "))

    match opcion:
        
        case 1: 
          a = float(input("Primer nùmero: "))
          b = float(input("segundo nùmero: "))
          print(f"Resultado: {suma(a, b )}")
        case 2: 
          a = float(input("Primer nùmero: "))
          b = float(input("segundo nùmero: "))
          print(f"Resultado: {resta(a, b )}")
        case 3: 
          a = float(input("Primer nùmero: "))
          b = float(input("segundo nùmero: "))
          print(f"Resultado: {multiplicacion(a, b )}")

        case 4: 
          a = float(input("Primer nùmero: "))
          b = float(input("segundo nùmero: "))
          print(f"Resultado: {division(a, b )}")

        case 0: 
          cerrarPrograma= True
        case _:
          print("Opciòn no valida")



