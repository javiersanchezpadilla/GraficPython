""" RELLENO DE POLIGONOS (METODO DE INUNDACIÓN).

    ¿CÓMO FUNCIONA?

    1)  Punto de partida: Se selecciona un punto inicial dentro del polígono 
        que se desea rellenar.
    2)  Comprobación de vecinos: Se examinan los píxeles adyacentes al punto 
        inicial (arriba, abajo, izquierda, derecha).
    3)  Relleno: Si un píxel adyacente está dentro del polígono y aún no ha sido 
        coloreado, se le asigna el color de relleno y se añade a una lista de 
        píxeles a procesar.
    4)  Iteración: Se repite el paso 3 para cada píxel de la lista hasta que no 
        queden más píxeles por procesar.

    Leer pixeles.
    -------------
    Imagina que la pantalla es una rejilla gigante de colores. Tú le dices a la 
    función: ¿Qué color hay en la coordenada (x, y)?, y ella te devuelve los 
    valores Rojo, Verde y Azul de ese píxel.

            glReadPixels(x, y, ancho, alto, formato, tipo, datos)

    Ejemplo práctico: Leer el color bajo el ratón de un solo pixel.

    3 Detalles importantes:
    -----------------------
    1)  Coordenadas invertidas: En la mayoría de las librerías de ventanas 
        (como GLFW o Pygame), el punto (0,0) es la esquina superior izquierda. 
        En OpenGL, glReadPixels considera que el (0,0) es la esquina inferior 
        izquierda. Se requiere hacer una resta (alto_ventana - y_raton) para que 
        coincidan.
    2)  Rendimiento: Leer píxeles es una operación algo 'lenta' porque la 
        información tiene que viajar desde la tarjeta de video (GPU) de vuelta 
        al procesador (CPU). Se debe usar con cuidado, por ejemplo, cuando el 
        usuario hace clic.
    3)  Formato: Normalmente usamos GL_RGB o GL_RGBA y el tipo GL_UNSIGNED_BYTE 
        para obtener valores entre 0 y 255.
"""
import glfw
from OpenGL.GL import *

def obtener_color_pixel(x, y):
    # Leemos 1x1 píxel en el formato RGB
    # Nota: y suele estar invertido en OpenGL (el 0 está abajo)
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
    
    # Convertimos los bytes a una lista de números (R, G, B)
    if color:
        return list(color)
    return [0, 0, 0]

# Ejemplo de uso dentro del bucle:
r, g, b = obtener_color_pixel(400, 300) # Centro de una ventana 800x600
print(f"Rojo {r}, verde {g}, azul{b}")
