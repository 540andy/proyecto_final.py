#Intentare hacer un menu de compra de gomitas

#creamos varibla 

opcion = -1

#utilizamos un siclo while
while opcion != 5:
    print("1.- Deseo comprar Gomitas azucaradas")

    print("2.- Deseo comprar Gomitas acidas")

    print("3.- Deseo comprar Gomitas de colores") 

    print("4.- Deseo comprar Gomitas azucaradas")

    print("5.- terminar compra")
    opcion =int (input("introduce una opcion"))
    # una vez teniendo las opciones, se necesita un codigo que ejecute cierta accion dependiendo lo que elija el ususrio
    # para ello utilizaremos un match case
    match opcion:
        case 1:
            print("En gomitas dulces, tenemos las de frutas")
        case 2:
            print("En gomitas acidas, tenemos las de arcoiris")
        case 3:
            print("En gomitas de colores, tenemos las de panditas ")

        case 4:
            print("En gomitas azucaradas, tenemos las de formas ")
        case 5:
            print("terminar compra")
        case _:
            print("Opcion invalida")

     
     








