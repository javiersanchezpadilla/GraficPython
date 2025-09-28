""" Programa que dibuja una linea en OpenGL version 2 
    Esta es la version mas estructurada del programa, donde todo el codigo esta en funciones.
    En este ejemplo se dibuja cuatro lineas amarillas que cruzan la ventana.
"""

import glfw
from OpenGL.GL import *


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana


def proyeccion():
    """ Esta función configura la matriz de proyección para definir el espacio de coordenadas
        que vamos a utilizar para dibujar en la ventana.
        No retorna ningún valor, solo configura el estado de OpenGL.
        La función establece un sistema de coordenadas 2D donde el origen (0,0) está en la esquina
        inferior izquierda, el eje X va de 0 a 200 y el eje Y va de 0 a 150.
        Esto significa que cualquier cosa que dibujemos usando estas coordenadas se ajustará a este
        rango dentro de la ventana.
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 200.0, 0.0, 150.0, -1.0, 1.0) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    proyeccion()

    while not glfw.window_should_close(ventana):
        # Limpiamos la pantalla con fondo negro
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Fija el color amarillo para dibujar
        glColor3f(1.0, 1.0, 0.0)
        # Dibuja una lineas
        glBegin(GL_LINES)
        # Linea 1
        glVertex2i (0, 0)
        glVertex2i (200, 150)
        # Linea 2
        glVertex2i (200, 0)
        glVertex2i (0, 150)
        # Linea 3
        glVertex2i (0, 75)
        glVertex2i (200, 75)
        # Linea 4
        glVertex2i (100, 0)
        glVertex2i (100, 150)
        glEnd()

        # Refresca la pantalla
        # Intercambia las dos caras del lienzo para mostrar lo que hemos dibujado
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    # Terminamos el programa y cerramos todo
    glfw.terminate()
