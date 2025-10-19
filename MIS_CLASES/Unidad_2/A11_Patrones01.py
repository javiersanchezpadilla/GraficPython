""" Función de mapa de bits de OpenGL.
    En este ejercicio vamos a crear una mapa de bits (una letra X).

    Lo primero que tenemos que entender es la manera de definir una matriz para mapas de bits
    Tomemos como ejemplo el dibujo de la letra “X” en una matriz de mapa de bits de 16 x 16 bits, 
    donde por medio de ceros y unos dibujaremos la letra.

         8 bits    |    8 bits          Los mapas de bits son almacenados en grupos de 8 bits 
    +-------------+-+-------------+
    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1     10000000  00000001  Linea 1
    0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0     01000000  00000010  Linea 2
    0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0     00100000  00000100  Linea 3
    0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0     00010000  00001000  Linea 4
    0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0     00001000  00010000  Linea 5
    0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0     00000100  00100000  Linea 6
    0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0     00000010  01000000  Linea 7
    0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0     00000001  10000000  Linea 8
    0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0     00000001  10000000  Linea 9
    0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0     00000010  01000000  Linea 10
    0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0     00000100  00100000  Linea 11
    0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0     00001000  00010000  Linea 12
    0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0     00010000  00001000  Linea 13
    0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0     00100000  00000100  Linea 14
    0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0     01000000  00000010  Linea 15
    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1     10000000  00000001  Linea 16

    La matriz actual es de 16x16 y siempre debe tomarse de la ultima linea (Linea16) hacia arriba (Linea 1).

    Analicemos la linea 16
    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1  son dos grupos de ocho bits el primero es 1000 0000 y el segundo es 0000 0001, 
    para representar esto es hexadecimal consideramos el primer grupo 1000 0000 binario, que equivale en hexadecimal 
    al número 80, para representarlo usamos 0x80, ahora para el segundo grupo de ocho bits de la misma línea 16 que 
    es 0000 0001 su equivalente convertidor de binario a hexadecimal es 01, esto es 0x01, y así sucesivamente.

    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1     1000 0000  0000 0001  0x80  0x01

    Desarrollo de toda la matriz binaria

    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1     10000000  00000001  Linea 1     0x80, 0x01
    0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0     01000000  00000010  Linea 2     0x40, 0x02
    0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0     00100000  00000100  Linea 3     0x20, 0x04
    0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0     00010000  00001000  Linea 4     0x10, 0x08
    0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0     00001000  00010000  Linea 5     0x08, 0x10
    0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0     00000100  00100000  Linea 6     0x04, 0x20
    0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0     00000010  01000000  Linea 7     0x02, 0x40
    0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0     00000001  10000000  Linea 8     0x01, 0x80
    0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0     00000001  10000000  Linea 9     0x01, 0x80
    0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0     00000010  01000000  Linea 10    0x02, 0x40
    0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0     00000100  00100000  Linea 11    0x04, 0x20
    0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0     00001000  00010000  Linea 12    0x08, 0x10
    0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0     00010000  00001000  Linea 13    0x10, 0x08
    0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0     00100000  00000100  Linea 14    0x20, 0x04
    0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0     01000000  00000010  Linea 15    0x40, 0x02
    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1     10000000  00000001  Linea 16    0x80, 0x01

    Ahora solo debemos colocar los valores hexadecimales de cada una de las lineas iniciando desde la ultima linea hasta
    la primer linea (no queda en orden inverso, se toma cada linea respetando el orden de lo valores)
    El resultado queda de la siguiente forma:

    0x80, 0x01,  # 0x80=1000 0000 y 0x01=0000 0001 de la línea 16
    0x40, 0x02,  # 0x40=0100 0000 y 0x02=0000 0010 de la línea 15
	0x20, 0x04,  # 0x20=0010 0000 y 0x04=0000 0100 de la línea 14
	0x10, 0x08,  # 0x10=0001 0000 y 0x08=0000 1000 de la linea 13
	0x08, 0x10,  # 0x08=0000 1000 y 0x10=0001 0000 de la línea 12
	0x04, 0x20,  # 0x04=0000 0100 y 0x20=0010 0000 de la línea 11
    0x02, 0x40,  # 0x02=0000 0010 y 0x40=0100 0000 de la línea 10
	0x01, 0x80,  # 0x01=0000 0001 y 0x80=1000 0000 de la línea 09
	0x01, 0x80,  # 0x01=0000 0001 y 0x80=1000 0000 de la línea 08
	0x02, 0x40,  # 0x02=0000 0010 y 0x40=0100 0000 de la línea 07
	0x04, 0x20,  # 0x04=0000 0100 y 0x20=0010 0000 de la línea 06
	0x08, 0x10,  # 0x08=0000 1000 y 0x10=0001 0000 de la línea 05
	0x10, 0x08,  # 0x10=0001 0000 y 0x08=0000 1000 de la linea 04
	0x20, 0x04,  # 0x20=0010 0000 y 0x04=0000 0100 de la línea 03
	0x40, 0x02,  # 0x40=0100 0000 y 0x02=0000 0010 de la línea 02
	0x80, 0x01,  # 0x80=1000 0000 y 0x01=0000 0001 de la línea 01 

    PUNTOS CLAVE:

    Arreglo de Datos (Bitmap): Es conveniente usar un arreglo de NumPy con el tipo np.ubyte (unsigned byte). 
    Cada byte define 8 píxeles del mapa de bits.

    Configuración de Proyección: Para que glRasterPos2i(100, 100) funcione como esperas (en píxeles), es crucial configurar la 
    matriz de proyección con glOrtho(0, ancho, 0, alto, ...) para que las coordenadas de OpenGL coincidan con las coordenadas 
    de píxeles de la ventana.

    Por lo tanto nuestro arreglo de mapa de bits queda de la siguiente forma:

    letra_x = np.array([0x80, 0x01,  # línea 16
                        0x40, 0x02,  # línea 15
	                    0x20, 0x04,  # línea 14
	                    0x10, 0x08,  # linea 13
	                    0x08, 0x10,  # línea 12
	                    0x04, 0x20,  # línea 11
                        0x02, 0x40,  # línea 10
	                    0x01, 0x80,  # línea 09
	                    0x01, 0x80,  # línea 08
	                    0x02, 0x40,  # línea 07
	                    0x04, 0x20,  # línea 06
	                    0x08, 0x10,  # línea 05
	                    0x10, 0x08,  # linea 04
	                    0x20, 0x04,  # línea 03
	                    0x40, 0x02,  # línea 02
	                    0x80, 0x01,  # línea 01 ], dtype=np.ubyte)

    Es importante no olvidar que debemos importar la libreria numpy desde la concola de texto mediante el comando

    pip install numpy 
"""

import glfw
from OpenGL.GL import *
import numpy as np # Necesitamos NumPy para manejar la matriz de bytes de forma eficiente

# --- 1. Definición del Mapa de Bits ---
# Creamos un patrón binario de 32x32 que representa un "cuadrado" o patrón simple.
# Cada byte (GLubyte) representa 8 píxeles. Usamos '0xff' para 8 píxeles encendidos.
# Los datos deben estar en formato C-style (generalmente de abajo hacia arriba).
# Este arreglo representa un cuadrado simple o un patrón en la esquina.
BITMAP_WIDTH = 16
BITMAP_HEIGHT = 16

# Definición del patrón binario (16x16 píxeles) una letra "X"
letra_x = np.array([0x80, 0x01,  # línea 16
                    0x40, 0x02,  # línea 15
	                0x20, 0x04,  # línea 14
	                0x10, 0x08,  # linea 13
	                0x08, 0x10,  # línea 12
	                0x04, 0x20,  # línea 11
                    0x02, 0x40,  # línea 10
	                0x01, 0x80,  # línea 09
	                0x01, 0x80,  # línea 08
	                0x02, 0x40,  # línea 07
	                0x04, 0x20,  # línea 06
	                0x08, 0x10,  # línea 05
	                0x10, 0x08,  # linea 04
	                0x20, 0x04,  # línea 03
	                0x40, 0x02,  # línea 02
	                0x80, 0x01   # línea 01 
                    ], dtype=np.ubyte)

# Definición del patrón binario (16x16 píxeles) una carita feliz
carita_feliz = np.array([0x1f, 0xf8, 0x3e, 0x7c, 0x3c, 0x3c, 0x20, 0x04, 0x60, 0x06, 0x4f, 0xf2, 0x5f, 0xfa, 0xfc, 0x3f,
                         0x7e, 0x7f, 0xff, 0xff, 0x39, 0xce, 0x61, 0x86, 0x21, 0x84, 0x21, 0x84, 0x33, 0xcc, 0x1f, 0xf8 
                        ], dtype=np.ubyte)


letra_m = np.array([0xFC, 0x0F, 0x78, 0x0E, 0x78, 0x0E, 0x78, 0x0E, 0x78, 0x8E, 0x79, 0x8E, 0x79, 0x8E, 0x7B, 0xCE,
                    0x7F, 0xEE, 0x7F, 0xFE, 0x7F, 0xFE, 0x7E, 0x7E, 0x7C, 0x3E, 0x78, 0x1E, 0xF0, 0x0E, 0xF0, 0x07
                    ], dtype=np.ubyte)


def dibujar_mapa_bits():
    """Función que usa glRasterPos2i() y glBitmap() para dibujar el patrón."""
    
    # 1. Establecer el color para los píxeles encendidos (donde el bit es 1)
    glColor3f(1.0, 1.0, 0.0)  # Amarillo

    # 2. Establecer la posición de trama (Raster Position) en coordenadas de ventana
    # En este caso, usaremos coordenadas de ventana (píxeles), no las coordenadas -1 a 1 de OpenGL.
    glRasterPos2i(100, 100) # El mapa de bits empezará a dibujarse en el pixel (100, 100)
    
    # 3. Dibujar el mapa de bits
    # Parámetros: width, height, xorig, yorig, xmove, ymove, bitmap_data
    glBitmap(
        BITMAP_WIDTH,         # Ancho del mapa de bits (en píxeles)
        BITMAP_HEIGHT,        # Alto del mapa de bits (en píxeles)
        0.0, 0.0,             # Origen (usaremos el borde inferior izquierdo como origen)
        0.0, 0.0,             # No mover la posición de trama después de dibujar
        letra_x               # El arreglo de bytes que contiene el patrón
    )

    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2i(100, 100) # El mapa de bits empezará a dibujarse en el pixel (100, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT, 0.0, 0.0, 0.0, 0.0, letra_x)

    # Corregimos los defectos del mapa recortando la altura en cada prueba
    glColor3f(1.0, 1.0, 0.0)
    glRasterPos2i(200, 100) # El mapa de bits empezará a dibujarse en el pixel (200, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 1, 0.0, 0.0, 0.0, 0.0, letra_x)

    glColor3f(0.0, 0.0, 1.0)
    glRasterPos2i(300, 100) # El mapa de bits empezará a dibujarse en el pixel (300, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 2, 0.0, 0.0, 0.0, 0.0, letra_x)

    glColor3f(0.4, 0.3, 0.8)
    glRasterPos2i(400, 100) # El mapa de bits empezará a dibujarse en el pixel (400, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 3, 0.0, 0.0, 0.0, 0.0, letra_x)

    glColor3f(0.0, 1.0, 1.0)
    glRasterPos2i(500, 100) # El mapa de bits empezará a dibujarse en el pixel (500, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 4, 0.0, 0.0, 0.0, 0.0, letra_x)

    glColor3f(1.0, 0.0, 1.0)
    glRasterPos2i(600, 100) # El mapa de bits empezará a dibujarse en el pixel (600, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 5, 0.0, 0.0, 0.0, 0.0, letra_x)

    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2i(700, 100) # El mapa de bits empezará a dibujarse en el pixel (700, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 6, 0.0, 0.0, 0.0, 0.0, letra_x)


    # Ahora dibujamos una carita feliz
    glColor3f(0.2, 0.7, 0.1)
    glRasterPos2i(100, 200) # El mapa de bits empezará a dibujarse en el pixel (100, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT, 0.0, 0.0, 0.0, 0.0, carita_feliz)

    # Corregimos los defectos del mapa recortando la altura en cada prueba
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2i(200, 200) # El mapa de bits empezará a dibujarse en el pixel (200, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 6, 0.0, 0.0, 0.0, 0.0, carita_feliz)

    # Ahora dibujamos una letra M
    glColor3f(0.2, 0.7, 0.1)
    glRasterPos2i(100, 300) # El mapa de bits empezará a dibujarse en el pixel (100, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT, 0.0, 0.0, 0.0, 0.0, letra_m)

    # Corregimos los defectos del mapa recortando la altura en cada prueba
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2i(200, 300) # El mapa de bits empezará a dibujarse en el pixel (200, 100)
    glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT - 6, 0.0, 0.0, 0.0, 0.0, letra_m)


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "glBitmap y glRasterPos2i", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana

def configurar_coordenadas_ventana(ancho, alto):
    """Configura la proyección para usar coordenadas de píxeles (ventana)."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    # Esto mapea [0, ancho] en X y [0, alto] en Y
    glOrtho(0.0, ancho, 0.0, alto, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Nota: glRasterPos2i() funciona en coordenadas de ventana, 
    # por lo que es esencial configurar la proyección a coordenadas de ventana.


def main():
    ventana_ancho = 800
    ventana_alto = 600
    ventana = iniciar_ventana()

    # Configurar la proyección para trabajar con coordenadas de píxeles
    configurar_coordenadas_ventana(ventana_ancho, ventana_alto)
    
    glClearColor(0.0, 0.0, 0.2, 1.0) # Fondo azul oscuro
    
    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        # Llama a la función de dibujo de mapa de bits
        dibujar_mapa_bits()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()


if __name__ == "__main__":
    main()
