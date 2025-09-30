""" En este ejercicio se desarrollara el tema de rotación de un objeto alrededor de un punto.
    LA ecuación matemática para la rotación de un punto (x, y) alrededor del origen (0, 0) por un ángulo θ es:
        x' = x * cos(θ) - y * sin(θ)
        y' = x * sin(θ) + y * cos(θ)
    Donde (x', y') son las nuevas coordenadas del punto después de la rotación.
    Si queremos rotar alrededor de un punto (h, k) que no es el origen, primero trasladamos el punto al origen,
    aplicamos la rotación y luego trasladamos de vuelta:
        1. Trasladar el punto al origen: (x - h, y - k)
        2. Aplicar la rotación:
            x' = (x - h) * cos(θ) - (y - k) * sin(θ)
            y' = (x - h) * sin(θ) + (y - k) * cos(θ)
        3. Trasladar de vuelta: (x' + h, y' + k)
    Finalmente, combinando estos pasos, obtenemos las fórmulas finales para rotar alrededor del punto (h, k):
        x' = (x - h) * cos(θ) - (y - k) * sin(θ) + h
        y' = (x - h) * sin(θ) + (y - k) * cos(θ) + k    
    
     x_prima=x_r+(x-x_r)*cos(pi*ang_rotac/180)-(y-y_r)*sin(pi*ang_rotac/180)
     y_prima=y_r+(y-y_r)*cos(pi*ang_rotac/180)+(x-x_r)*sin(pi*ang_rotac/180)

    Donde:
        (x, y) son las coordenadas originales del punto.
        (x', y') son las coordenadas del punto después de la rotación.
        (h, k) es el punto alrededor del cual se rota.
        θ es el ángulo de rotación en radianes.

        
        ESTOY DESARROLLANDO ESTE EJERCICIO, ESTO QUIERE DECIR QUE ESTA IMCOMPLETO.
"""

import glfw
from OpenGL.GL import *
from math import cos, sin


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


def rotar_punto():
    PI = 3.141592653589793
    radio = 0.6
    puntos_a_dibujar = 1000
    glColor3f(1.0, 1.0, 0.0)     # Color amarillo brillante

    for i in range(puntos_a_dibujar + 1):
        angulo = (i / puntos_a_dibujar) * 2 * PI
        # Ecuación paramétrica
        x = radio * cos(angulo)
        y = radio * sin(angulo)

        # Dibuja un punto en las coordenadas (x, y)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        rotar_punto()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
