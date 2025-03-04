import requests  # Importa la librería requests para hacer peticiones HTTP
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot para mostrar imágenes
from PIL import Image  # Importa PIL (Pillow) para trabajar con imágenes
from io import BytesIO  # Importa BytesIO para manejar datos de imagen en memoria
import json  # Importa json para trabajar con archivos JSON
import os  # Importa os para interactuar con el sistema operativo (crear carpetas)

print("bienvenido al programa")  # Imprime un mensaje de bienvenida

pokemon = input("Introduce un pokémon: ")  # Pide al usuario el nombre del Pokémon

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()  # Construye la URL de la API de Pokémon
resultado = requests.get(url)  # Hace la petición a la API

if resultado.status_code != 200:  # Verifica si la petición fue exitosa (código 200)
    print("pokèmon no encontrado")  # Imprime un mensaje de error si el Pokémon no existe
    exit()  # Termina el programa

datos = resultado.json()  # Convierte la respuesta de la API a formato JSON
print(datos) #Imprime datos para verificar la informacion obtenida de la API

try:  # Inicia un bloque try para manejar posibles errores
    url_imagen = datos['sprites']['front_default']  # Obtiene la URL de la imagen del Pokémon
    respuesta_imagen = requests.get(url_imagen)  # Obtiene la imagen del Pokémon
    respuesta_imagen.raise_for_status()  # Verifica si la imagen se obtuvo correctamente
    imagen = Image.open(BytesIO(respuesta_imagen.content))  # Abre la imagen desde los bytes obtenidos
    plt.title(datos['name'].capitalize())  # Establece el título de la imagen
    plt.imshow(imagen)  # Muestra la imagen
    plt.show()  # Muestra la ventana con la imagen

    try: #Segundo bloque try except, para manejar errores al mostrar la descripcion.
        print("\nEstadísticas:")  # Imprime un encabezado para las estadísticas
        print(f"  Peso: {datos['weight']}")  # Imprime el peso del Pokémon
        print(f"  Tamaño: {datos['height']}")  # Imprime el tamaño del Pokémon
        print("\n  Movimientos:")  # Imprime un encabezado para los movimientos
        for movimiento in datos['moves']:  # Itera sobre los movimientos
            print(f"    - {movimiento['move']['name'].capitalize()}")  # Imprime el nombre del movimiento
        print("\n  Habilidades:")  # Imprime un encabezado para las habilidades
        for habilidad in datos['abilities']:  # Itera sobre las habilidades
            print(f"    - {habilidad['ability']['name'].capitalize()}")  # Imprime el nombre de la habilidad
        print("\n  Tipos:")  # Imprime un encabezado para los tipos
        for tipo in datos['types']:  # Itera sobre los tipos
            print(f"    - {tipo['type']['name'].capitalize()}")  # Imprime el nombre del tipo

    except KeyError as e: # Captura errores de clave si faltan datos en la descripcion.
        print (f"Error al obtener datos de la descripcion: {e}")
    except Exception as e: # Captura cualquier otro error al mostrar la descripcion.
        print (f"Error inesperado al mostrar la descripcion: {e}")

except requests.exceptions.RequestException as e:  # Captura errores al obtener la imagen
    print(f"Error al obtener la imagen: {e}")  # Imprime el mensaje de error

except KeyError:  # Captura el error si no existe la URL de la imagen
    print("No tiene imagen!!")  # Imprime un mensaje de error

except Exception as e:  # Captura cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}")  # Imprime el mensaje de error

if not os.path.exists("pokedex"):  # Verifica si la carpeta "pokedex" no existe
    os.makedirs("pokedex")  # Crea la carpeta "pokedex"

datos['front_image_url'] = url_imagen  # Agrega la URL de la imagen al diccionario de datos
del datos['sprites']  # Elimina la clave 'sprites' para limpiar el JSON

nombre_archivo = os.path.join(os.getcwd(), "pokedex", f"{datos['name'].lower()}.json") #Crea la ruta absoluta del archivo json.

print(f"Ruta del archivo: {nombre_archivo}")
with open(nombre_archivo, "w", encoding="utf-8") as archivo_json:  # Abre el archivo JSON en modo escritura
    json.dump(datos, archivo_json, indent=4)  # Guarda los datos en el archivo JSON

print(f"Información de {datos['name'].capitalize()} guardada en {nombre_archivo}")  # Imprime un mensaje de confirmación
    




"""Este proyecto es el que más me ha causado conflicto realizar. Me pasé varios días analizando cómo debía hacerle ..
Incluso sentí que mi capacidad de resolver problemas era de un cero... pero volviendo a ver los recursos del curso capté varias ideas.
También pedí ayuda a la inteligencia artificial para entender cómo funciona el código.
De lo que yo quería realizar, a pesar de no haber hecho 100% este trabajo, me siento contenta de haber avanzado mucho estos 4 meses, ya que en la universidad no lo estaba haciendo.
""" 
