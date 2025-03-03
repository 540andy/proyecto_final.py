import requests  # Permite hacer peticiones HTTP (obtener datos de la web)
import matplotlib.pyplot as plt  # Permite crear gráficos y mostrar imágenes
from PIL import Image  # Permite trabajar con imágenes

from io import BytesIO  # Permite trabajar con bytes en memoria
import json  # Permite trabajar con archivos JSON
import os  # Permite trabajar con el sistema operativo (crear carpetas)

print("bienvenido al programa")

pokemon = input("Introduce un pokémon: ")  # Pide al usuario el nombre del Pokémon

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()  # Crea la URL para obtener los datos del Pokémon
resultado = requests.get(url)  # Obtiene los datos del Pokémon desde la API

if resultado.status_code != 200:  # Verifica si el Pokémon existe (código 200 significa éxito)
    print("pokèmon no encontrado")  # Muestra un mensaje de error si el Pokémon no existe

    exit()  # Termina el programa

datos = resultado.json()  # Convierte los datos obtenidos a formato JSON (diccionario de Python)

try:
    url_imagen = datos['sprites']['front_default']  # Obtiene la URL de la imagen del Pokémon

    respuesta_imagen = requests.get(url_imagen)  # Obtiene la imagen del Pokémon

    respuesta_imagen.raise_for_status()  # Verifica si la imagen se obtuvo correctamente

    imagen = Image.open(BytesIO(respuesta_imagen.content))  # Abre la imagen desde los bytes obtenidos

    plt.title(datos['name'].capitalize())  # Establece el título de la imagen (nombre del Pokémon)

    plt.imshow(imagen)  # Muestra la imagen del Pokémon

    plt.show()  # Muestra la ventana con la imagen

    print("\nEstadísticas:")  # Imprime un encabezado para las estadísticas

    print(f"  Peso: {datos['weight']}")  # Imprime el peso del Pokémon

    print(f"  Tamaño: {datos['height']}")  # Imprime el tamaño del Pokémon

    print("\n  Movimientos:")  # Imprime un encabezado para los movimientos

    for movimiento in datos['moves']:  # Itera sobre los movimientos del Pokémon

        print(f"    - {movimiento['move']['name'].capitalize()}")  # Imprime el nombre de cada movimiento

    print("\n  Habilidades:")  # Imprime un encabezado para las habilidades
    for habilidad in datos['abilities']:  # Itera sobre las habilidades del Pokémon
        print(f"    - {habilidad['ability']['name'].capitalize()}")  # Imprime el nombre de cada habilidad

    print("\n  Tipos:")  # Imprime un encabezado para los tipos
    for tipo in datos['types']:  # Itera sobre los tipos del Pokémon
        print(f"    - {tipo['type']['name'].capitalize()}")  # Imprime el nombre de cada tipo

    if not os.path.exists("pokedex"):  # Verifica si la carpeta "pokedex" existe
        os.makedirs("pokedex")  # Crea la carpeta "pokedex" si no existe

    datos['front_image_url'] = url_imagen # Agrega la url de la imagen al json.
    del datos['sprites'] # Elimina la informacion de sprites.

    nombre_archivo = f"pokedex/{datos['name'].lower()}.json"  # Crea el nombre del archivo JSON

    with open(nombre_archivo, "w") as archivo_json:  # Abre el archivo JSON en modo escritura
        
        json.dump(datos, archivo_json, indent=4)  # Guarda los datos del Pokémon en el archivo JSON

    print(f"Información de {datos['name'].capitalize()} guardada en {nombre_archivo}")  # Muestra un mensaje de confirmación

except requests.exceptions.RequestException as e:  # Captura errores al obtener la imagen
    print(f"Error al obtener la imagen: {e}")  # Muestra un mensaje de error
    exit()  # Termina el programa

except KeyError:  # Captura el error si no existe la URL de la imagen
    print("No tiene imagen!!")  # Muestra un mensaje de error
    exit()  # Termina el programa

except Exception as e:  # Captura cualquier otro error
    print(f"Ocurrió un error inesperado: {e}")  # Muestra un mensaje de error

    exit()  # Termina el programa



"""Este proyecto es el que más me ha causado conflicto realizar. Me pasé varios días analizando cómo debía hacerle ..
Incluso sentí que mi capacidad de resolver problemas era de un cero... pero volviendo a ver los recursos del curso capté varias ideas.
También pedí ayuda a la inteligencia artificial para entender cómo funciona el código.
De lo que yo quería realizar, a pesar de no haber hecho 100% este trabajo, me siento contenta de haber avanzado mucho estos 4 meses, ya que en la universidad no lo estaba haciendo.
""" 
