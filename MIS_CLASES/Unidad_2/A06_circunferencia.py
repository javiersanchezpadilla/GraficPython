""" Ecuación Paramétrica de una Circunferencia
    La ecuación paramétrica te da las coordenadas (x, y) de cada punto en la circunferencia en 
    función de un ángulo θ (theta).

    La ecuación es:                                                  
        x = r * cos(θ)   y = r * sin(θ)   Donde:    r es el radio de la circunferencia.
                                                    (θ) theta es el ángulo que va de 0 a 360 grados 
                                                    (o de 0 a 2\pi radianes).

    En la programación, esta ecuación se usa en un bucle. Generas un valor de (θ) theta para cada 
    punto y luego calculas las coordenadas (x, y) para cada uno.

    1. generamos una serie de ángulos (θ) theta en incrementos pequeños para obtener suficientes 
       puntos y que la circunferencia se vea suave.
    2. Define los parámetros: El radio (r) y el número de puntos que quieres dibujar.
    3. Crea un bucle: Itera desde 0 hasta 2\pi (o 360 grados) con un paso pequeño (ejm, 0.01 radianes).
    4. Calcula los puntos: En cada iteración, usa la ecuación paramétrica para encontrar 'x' e 'y'

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


def dibuja_circulo():
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
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    while not glfw.window_should_close(ventana):
        dibuja_circulo()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
