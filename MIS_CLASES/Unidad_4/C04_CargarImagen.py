""" CARGAR UNA IMAGEN USANDO LA LIBRERIA PILLOW
    -------------------------------------------

    Este programa lee una imagen, muestra sus propiedades y la reescribe al 50% de su tamaño original

    Verificamos que tengamos las librerias instaladas
    
    pip install PyOpenGL PyOpenGL-accelerate
    pip install glfw
    pip install Pillow          <-- Esta la que vamos a estar ocupando

    
    La clave de Pillow es que convierte cualquier archivo de imagen (JPEG, PNG, etc.) en un objeto de 
    Python con el cual podemos trabajar fácilmente, olvidandonos de los detalles del formato del archivo.

    Creación del objeto del tipo imagen, para esto leemos la imagen y la asignamos a una variable (del tipo objeto)

        imagen = Image.open(nombre_archivo) 

        
    imagen.format       Nos dice el formato de la imagen, si es un PNG, JPG, etc.
    imagen.size         Nos proporciona las dimensiones de la imagen (ancho, alto).
    imagen.mode         Nos indica el formato de color que se usa en la imagen  (RGB, RGBA, etc.).

    Manipular. El objeto imagen (el que creamos al momento de cargar imagen = Image.open(nombre_archivo)) 
    tiene muchos métodos útiles, como:
    
    resize()            para cambiar el tamaño
    rotate()            para girar
    crop()              para recortar

    imagen.save()       Nos permite guardar la imagen  
    
        imagen_pequena.save(nombre_guardado)

    El método `save()` toma el objeto `Image` modificado y lo escribe de nuevo en el disco, utilizando el formato 
    de origen dado por la extensión del nombre del archivo original (en este caso, JPG).

"""


from PIL import Image       # Esta libreria da acceso a las librerias de pillow
import os
import sys

# --- CONFIGURACIÓN Y PREPARACIÓN ---

# Nombre del archivo de imagen que intentaremos cargar
NOMBRE_ARCHIVO = "/home/javier/Documentos/Programas/Python/Texturas/PNGs/FondoPaisaje02.jpg"

def crear_archivo_de_prueba():
    """
    Función auxiliar para crear una imagen simple si no existe,
    para que el script funcione inmediatamente.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"-> Creando imagen de prueba '{NOMBRE_ARCHIVO}'...")
        try:
            # Creamos una imagen simple de 100x100 píxeles de color azul
            img_prueba = Image.new('RGB', (100, 100), color = 'skyblue')
            img_prueba.save(NOMBRE_ARCHIVO)
            print("-> Imagen de prueba creada con éxito.")
        except Exception as e:
            print(f"Error al crear la imagen de prueba: {e}")
            sys.exit(1)
    else:
        print(f"-> Archivo '{NOMBRE_ARCHIVO}' encontrado. Usando este archivo.")


def cargar_y_mostrar_informacion(nombre_archivo):
    """
    Función principal que demuestra la carga de la imagen.
    nombre_archivo contiene la ruta y el nombre del archivo a cargar
    """
    print("\n PASO 1: Intentando Cargar la Imagen (por aquello de los errores) ")
    try:
                                                        # Usamos Image.open() para cargar el archivo.
                                                        # Esto crea un objeto 'Image' de Pillow.

                                                        # Este es el paso más sencillo. Le pasamos la ruta de la imagen 
                                                        # y Pillow hace todo el trabajo pesado para leer los datos. 
                                                        # La variable `imagen` ahora contiene el objeto que representa la imagen.
                                                        # Acceder a la información: Una vez cargada, puedes usar las propiedades 
                                                        # del objeto imagen para saber todo sobre ella:                                                        
        imagen = Image.open(nombre_archivo) 
        
        print(f"¡Todo correcto! Imagen cargada como un objeto de Python.")
        print("\nPASO 2: Acceder a la Información (Metadata) ")

                                                        # 1. Mostrar el formato original del archivo
        print(f"-> Formato del archivo original: {imagen.format}")

                                                        # 2. Mostrar las dimensiones (ancho y alto)
        print(f"-> Tamaño (Ancho, Alto): {imagen.size}")

                                                        # 3. Mostrar el modo de color (e.g., RGB, RGBA, etc. etc.)
        print(f"-> Modo de color: {imagen.mode}")
        
                                                        # 4. Mostrar una previsualización de la imagen
        print("\nPASO 3: Mostrar la Imagen (requiere entorno gráfico)")
        print("-> Si estás en un entorno de escritorio, la imagen se abrirá en el visor predeterminado.")

                                                        # Mostrar la imagen: Llama al visor de imágenes predeterminado del sistema
                                                        # si estamos ejecutando el codigo desde consola no se cargara el entorno 
                                                        # grafico, pero si lo esta haciendo desde visual studio o antigravity si lo 
                                                        # puede ver, <<<para ver el resultado decomentar la siguiente linea>>>
        # imagen.show()                                 # <<----- PAra ver el resultado descomentar esta linea y ejecutar el programa


        print("\nPASO 4: Un ejemplo de manipulación (Redimensionar)")
        
                                                        # Redimensionar la imagen a la mitad de su tamaño original
        nuevo_ancho = imagen.size[0] // 2
        nuevo_alto = imagen.size[1] // 2
        
                                                        # Usamos el método resize() del objeto 'Image'
        imagen_pequena = imagen.resize((nuevo_ancho, nuevo_alto))
        
        print(f"-> Tamaño original: {imagen.size}")
        print(f"-> Nuevo tamaño después de redimensionar: {imagen_pequena.size}")
        
                                                        # Guardar la nueva imagen redimensionada
        nombre_guardado = "/home/javier/Documentos/Programas/Python/Texturas/PNGs/ejm_redim.jpg"
        imagen_pequena.save(nombre_guardado)
        print(f"-> Imagen redimensionada guardada como: '{nombre_guardado}'")

    except FileNotFoundError:
        print(f"ERROR: No se pudo encontrar el archivo '{nombre_archivo}'.")
        print("Asegúrate de que la imagen esté en el mismo directorio que el script.")
    except Exception as e:
        print(f"Ocurrió un error al cargar o procesar la imagen: {e}")


                                                        # Ejecutamos el programa principal
if __name__ == "__main__":
    crear_archivo_de_prueba()                           # Aseguramos que haya un archivo para probar
    cargar_y_mostrar_informacion(NOMBRE_ARCHIVO)        # Ejecutamos la carga