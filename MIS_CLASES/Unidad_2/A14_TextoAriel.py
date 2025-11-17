import glfw
from OpenGL.GL import *
from math import cos, sin
from OpenGL import GLUT
import sys
import random


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 800, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    GLUT.glutInit(sys.argv)				# Linea para inicializar GLUT y poder mandar texto a pantalla.
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
        # --- F U E N T E S   D E   M A P A   D E   B I T S ---

        # 1. PEQUEÑAS (Tamaño más común para logs y etiquetas)
        # GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_8_BY_13, ord(character))    # 8 píxeles de ancho x 13 de alto
        # GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_TIMES_ROMAN_10, ord(character)) # Times Roman de 10 puntos
        
        # 2. MEDIANAS (La que usabas antes)
        # GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_9_BY_15, ord(character))    # 9 píxeles de ancho x 15 de alto
        
        # 3. GRANDES (Más fáciles de leer)
        # GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_HELVETICA_18, ord(character)) # Helvetica de 18 puntos
        GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_TIMES_ROMAN_24, ord(character)) # Times Roman de 24 puntos
        
        # 4. OTRAS VARIACIONES
        # GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_HELVETICA_10, ord(character)) # Helvetica de 10 puntos
        # GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_HELVETICA_12, ord(character)) # Helvetica de 12 puntos


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
