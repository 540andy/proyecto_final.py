import random  # Importa el módulo random para generar números aleatorios.
import matplotlib.pyplot as plt  # Importa el módulo matplotlib.pyplot para crear gráficos.

def simular_maquina_galton(numero_de_canicas, numero_de_niveles):
    """Simula la Máquina de Galton y devuelve los resultados.

    Args:
        numero_de_canicas: El número de canicas a simular.
        numero_de_niveles: El número de niveles de obstáculos.

    Returns:
        Una lista con la posición final de cada canica.
    """
    resultados = []  # Crea una lista vacía para almacenar los resultados de cada canica.
    for _ in range(numero_de_canicas):  # Itera sobre el número de canicas a simular.
        posicion = 0  # Inicializa la posición de la canica en el centro (posición 0).
        for _ in range(numero_de_niveles):  # Itera sobre el número de niveles de obstáculos.
            desviacion = random.choices([-1, 1])[0]  # Elige aleatoriamente -1 (izquierda) o 1 (derecha).
            posicion += desviacion  # Actualiza la posición de la canica según la desviación.
        resultados.append(posicion)  # Agrega la posición final de la canica a la lista de resultados.
    return resultados  # Devuelve la lista con los resultados de todas las canicas.

def graficar_histograma(resultados, numero_de_niveles):
    """Grafica el histograma de los resultados.

    Args:
        resultados: Una lista con la posición final de cada canica.
        numero_de_niveles: El número de niveles de obstáculos.
    """
    plt.hist(resultados, bins=numero_de_niveles + 1, rwidth=0.8, color='skyblue', edgecolor='black')  # Crea el histograma.
    # bins=numero_de_niveles + 1 asegura que haya una barra para cada contenedor.
    # rwidth=0.8 ajusta el ancho de las barras para que no se superpongan.
    # color y edgecolor personalizan la apariencia de las barras.
    plt.xlabel("Posición final")  # Etiqueta el eje x como "Posición final".
    plt.ylabel("Cantidad de canicas")  # Etiqueta el eje y como "Cantidad de canicas".
    plt.title("Simulación de la Máquina de Galton (3000 canicas, 12 niveles)")  # Agrega un título al gráfico.
    plt.show()  # Muestra el histograma.

# Parámetros
numero_de_canicas = 3000  # Define el número de canicas a simular.
numero_de_niveles = 12  # Define el número de niveles de obstáculos.

# Simulación y graficación
resultados = simular_maquina_galton(numero_de_canicas, numero_de_niveles)  # Simula la máquina de Galton.
graficar_histograma(resultados, numero_de_niveles)  # Grafica el histograma con los resultados.