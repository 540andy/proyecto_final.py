# Definimos las variables para almacenar los años
año_actual = int(input("Introduce el año actual: "))
año_calcular = int(input("Introduce otro año para calcular el tiempo que ha pasado: "))

# Comparamos los años para determinar si son iguales
if año_actual == año_calcular:
    print("Los años son iguales. No hay diferencia.")  # Si los años son iguales, no hay cálculo que hacer
else:
    # Calculamos la diferencia entre los años, asegurando un valor positivo con abs()
    diferencia = abs(año_calcular - año_actual)
    if año_actual > año_calcular:
        print(f"Han transcurrido {diferencia} años.")  # Calculamos el tiempo transcurrido
    else:
        print(f"Faltan {diferencia} años para llegar al {año_calcular}.")  # Calculamos el tiempo restante 