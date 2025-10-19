""" Rotación de un punto alrededor DEL ORIGEN (0, 0)
    La ecuación para rotar un punto (x, y) alrededor del origen (0, 0) en un ángulo θ (theta) es:

    x' = x * cos(θ) - y * sin(θ)
    y' = x * sin(θ) + y * cos(θ)

    Donde:
    (x, y) son las coordenadas originales del punto.
    (x', y') son las nuevas coordenadas del punto después de la rotación.
    θ (theta) es el ángulo de rotación. El valor de theta debe estar en radianes.

    Si eliminamos la linea glClear(GL_COLOR_BUFFER_BIT) veremos el rastro del punto
"""

import glfw
from OpenGL.GL import *
from math import cos, sin, pi


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


def rotar_punto(x, y, angulo_grados):
    glClearColor(0.0, 0.0, 0.0, 1.0)    # Limpia la pantalla
    glClear(GL_COLOR_BUFFER_BIT)        # Si quitamos esta linea, veremos el rastro del punto

    glBegin(GL_LINES)                   # Dibuja los ejes
    glColor3f(1.0, 1.0, 1.0)            # Ejes en color blanco
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glEnd()
    
    glColor3f(1.0, 1.0, 0.0)            # Color amarillo brillante

    theta = angulo_grados * (pi / 180)  # Convertir grados a radianes
    x_prima = x * cos(theta) - y * sin(theta)
    y_prima = x * sin(theta) + y * cos(theta)
 
    # Dibuja un punto en las coordenadas (x, y)
    glPointSize(5)  # Tamaño del punto
    glBegin(GL_POINTS)
    glVertex2f(x_prima, y_prima)
    glEnd()
    return x_prima, y_prima


if __name__ == "__main__":
    ventana = iniciar_ventana()
    x = 0.5                 # Coordenada x del punto original
    y = 0.0                 # Coordenada y del punto original
    angulo_en_grados = 1    # Ángulo de rotación en grados

    while not glfw.window_should_close(ventana):
        x, y = rotar_punto(x, y, angulo_en_grados)         
        angulo_en_grados += 0.01  # Incrementa el ángulo para la próxima rotación
        print(f"Nuevo punto rotado: ({x:.3f}, {y:.3f})")
        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()
