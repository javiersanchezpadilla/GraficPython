""" IMPRESION DE TEXTO EN PANTALLA.

    FONTS DISPONIBLES:
    ------------------
    glutBitmapCharacter( Font, ASCII)

    GLUT_BITMAP_8_BY_13             <-- 8 pixeles de ancho por 13 de alto
    GLUT_BITMAP_9_BY_15             <-- 9 pixeles de ancho por 15 de alto
    GLUT_BITMAP_TIMES_ROMAN_10      <-- Times New Roman de tamaño 10
    GLUT_BITMAP_TIMES_ROMAN_24      <-- Times New Roman de tamaño 24
    GLUT_BITMAP_HELVETICA_10        <-- Helvetica de tamaño 10
    GLUT_BITMAP_HELVETICA_12        <-- Helvetica de tamaño 12
    GLUT_BITMAP_HELVETICA_18        <-- Helvetica de tamaño 18

    La función ord() convierte un carácter en su código ASCII:

    ord('A')  # → 65
    ord('a')  # → 97  
    ord('1')  # → 49
    ord('!')  # → 33

    glutBitmapCharacter() necesita el código numérico del carácter, no el carácter mismo
    (por eso es que requerimos obtener su código ASCII).
"""

import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 800, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    # GLUT.glutInit(sys.argv)				# Linea para inicializar GLUT y poder mandar texto a pantalla.
    glutInit()
    return ventana


def proyeccion():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000.0, 1000.0, -500.0, 500.0, -1.0, 1.0) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def dibujar_texto(text, x, y):
    # Dibuja texto usando una fuente bitmap de GLUT.

    # 1. Posicionamiento (Translación) y asignacion de color de la fuente.
    glRasterPos2f(x, y)
    
    # 2. Bucle de Dibujo
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character)) # Times Roman de 24 puntos
        

if __name__ == "__main__":
    ventana = iniciar_ventana()
    proyeccion()

    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(1.0, 1.0, 1.0, 1.0)
        dibujar_texto("Es el pinguino de Linux  ^_^", -300, 100)

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
