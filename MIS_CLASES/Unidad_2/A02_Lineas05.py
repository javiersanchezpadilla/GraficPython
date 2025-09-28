""" Programa que dibuja una linea en OpenGL version 5
    Esta es la version mas estructurada del programa, donde todo el codigo esta en funciones.
    En este ejemplo se dibuja cuatro lineas de distintos colores que cruzan la ventana y los ejes X y Y en color blanco.
    Lo importante en este ejemplo es que se muestra que podemos usar varias veces la función glBegin() y glEnd()
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


def dibuja():
    """ Esta función dibuja varias líneas en la ventana utilizando OpenGL.
        No retorna ningún valor, solo ejecuta comandos de dibujo.
        La función dibuja cuatro líneas:
        1. Una línea diagonal desde la esquina inferior izquierda (0,0) hasta la esquina superior derecha (200,150).
        2. Una línea diagonal desde la esquina inferior derecha (200,0) hasta la esquina superior izquierda (0,150).
        3. Una línea horizontal en el medio de la ventana desde (0,75) hasta (200,75).
        4. Una línea vertical en el medio de la ventana desde (100,0) hasta (100,150).
    """

    glColor3f(1.0, 1.0, 1.0)    # Establece el color blanco para los ejes
    glBegin(GL_LINES)
    glVertex2i (0, 75);         # Eje X
    glVertex2i (200, 75)
    glVertex2i (100,0)          # Eje Y
    glVertex2i (100, 150)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2i (0, 0)
    glVertex2i (200, 150)
    glVertex2i (0, 150)
    glVertex2i (200, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2i (0, 0)
    glVertex2i (200,150)
    glEnd()



if __name__ == "__main__":
    ventana = iniciar_ventana()
    proyeccion()

    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        dibuja()
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
