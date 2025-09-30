""" En este ejercicio dibujaremos cuadros de diferentes colores usando la primitiva GL_QUADS.
    Cada cuadro estara formado por cuatro vertices.
    Los cuadros se dibujaran en las cuatro esquinas de la ventana.
    Se usaran colores aleatorios para cada cuadro.
    Ademas las cordenadas de los vertices se almacenaran en listas para facilitar su manejo.
    En este caso dibujaremos un cuadro cada medio segundo en una posicion y con un tamaño aleatorio.
    Haremos uso de la funcion time.sleep(segundos) para crear la pausa entre cuadros.
"""

import glfw
from OpenGL.GL import *
import numpy as np

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


def dibuja():
    glColor3f(0.8, 0.8, 0.8)        # Dibujar una cuadrícula
    for punto in np.arange(-1.0, 1.0, 0.1):
        glBegin(GL_LINES)
        glVertex2f(punto, -1)
        glVertex2f(punto, 1)
        glVertex2f(-1, punto)
        glVertex2f(1, punto)
        glEnd()

    glColor3f(1.0,0.0,0.0)          # Dibuja una lineas formando una flecha
    glBegin(GL_LINES)
    glVertex2f(-0.9, 0.7)
    glVertex2f(-0.9, 0.9)
    glVertex2f(-0.9, 0.9)
    glVertex2f(-0.7, 0.9)
    glVertex2f(-0.7, 0.9)
    glVertex2f(-0.7, 1.0)
    glVertex2f(-0.7, 1.0)
    glVertex2f(-0.6, 0.8)
    glVertex2f(-0.6, 0.8)
    glVertex2f(-0.7, 0.6)
    glVertex2f(-0.7, 0.6)
    glVertex2f(-0.7, 0.7)
    glVertex2f(-0.7, 0.7)
    glVertex2f(-0.9, 0.7)
    glEnd()

    glBegin(GL_LINE_STRIP)          # Se unen el primer punto con el ultimo
    glVertex2f(-0.9, 0.2)
    glVertex2f(-0.9, 0.4)
    glVertex2f(-0.7, 0.4)
    glVertex2f(-0.7, 0.5)
    glVertex2f(-0.6, 0.3)
    glVertex2f(-0.7, 0.1)
    glVertex2f(-0.7, 0.2)
    glVertex2f(-0.9, 0.2)
    glEnd()

                                    # Se unen automaticamente el primer punto con el ultimo
    glBegin(GL_LINE_LOOP)  
    glVertex2f(-0.9, -0.1)
    glVertex2f(-0.9, -0.3)
    glVertex2f(-0.7, -0.3)
    glVertex2f(-0.7, -0.4)
    glVertex2f(-0.6, -0.2)
    glVertex2f(-0.7, 0.0)
    glVertex2f(-0.7, -0.1)
    glEnd()


    glBegin(GL_QUADS)               # Dibuja un cuadrado
    glVertex(-0.5, 0.9)
    glVertex(-0.2, 0.9)
    glVertex(-0.2, 0.7)
    glVertex(-0.5, 0.7)
    glEnd()

    glBegin(GL_POLYGON)             # Dibuja un poligono
    glVertex(-0.4, 0.5)
    glVertex(-0.3, 0.6)
    glVertex(-0.2, 0.5)
    glVertex(-0.3, 0.4)
    glEnd()

    glBegin(GL_POLYGON)             # Dibuja un pentagono
    glVertex(0.4, -0.5)
    glVertex(0.58, -0.63)
    glVertex(0.5, -0.9)
    glVertex(0.3, -0.9)
    glVertex(0.22, -0.63)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)      # Dibuja una tira de triángulos
    glColor3f(0.0, 0.5, 0.0)        # Color verde
    glVertex2f(0.5, 0.5)
    glColor3f(0.8, 0.0, 0.0)        # Color rojo claro
    glVertex2f(0.6, 0.7)
    glColor3f(0.0, 0.0, 1.0)        # Color azul brillante
    glVertex2f(0.7, 0.5)
    glVertex2f(0.8, 0.7)
    glColor3f(0.0, 0.5, 0.0)        # Color verde
    glVertex2f(0.9, 0.5)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)        # Dibuja un abanico de triángulos
    glColor3f(1.0, 0.5, 0.0)        # Color naranja
    glVertex2f(-0.5, -0.5)  # Centro del abanico
    # The code snippet you provided is using a for loop to iterate over a range of angles from 0 to 2π
    # (a full circle) with a step of 0.1 radians. For each angle, it calculates the x and y
    # coordinates of a point on a circle centered at (-0.5, -0.5) with a radius of 0.2. These
    # coordinates are then used to draw a series of connected points forming a circle using
    # `glVertex2f(x, y)`. Finally, `glEnd()` is called to end the drawing of the triangle fan, which
    # represents a filled sector of the circle centered at (-0.5, -0.5).
    # range por si solo no admite flotantes, por lo que usamos np.arange()
    for angulo in np.arange(0, 2 * np.pi, 0.1):
        x = -0.5 + 0.2 * np.cos(angulo)
        y = -0.5 + 0.2 * np.sin(angulo)
        glVertex2f(x, y)
    glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    glClearColor(0.3, 0.3, 0.3, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    while not glfw.window_should_close(ventana):
        dibuja()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
