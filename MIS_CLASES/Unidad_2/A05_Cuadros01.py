""" En este ejercicio dibujaremos cuadros de diferentes colores usando la primitiva GL_QUADS.
    Cada cuadro estara formado por cuatro vertices.
    Los cuadros se dibujaran en las cuatro esquinas de la ventana.
    Se usaran colores aleatorios para cada cuadro.
    Ademas las cordenadas de los vertices se almacenaran en listas para facilitar su manejo.
"""

import glfw
from OpenGL.GL import *
import random


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


def dibuja_cuadros():
    """ Dibuja cuadros. """     
    cuadro1 = [(0.5, 0.5), (0.8, 0.5), (0.8, 0.8), (0.5, 0.8)]
    cuadro2 = [(-0.5, 0.5), (-0.2, 0.5), (-0.2, 0.8), (-0.5, 0.8)]
    cuadro3 = [(-0.5, -0.5), (-0.2, -0.5), (-0.2, -0.8), (-0.5, -0.8)]
    cuadro4 = [(0.5, -0.5), (0.8, -0.5), (0.8, -0.8), (0.5, -0.8)]
  
    for cuadro in [cuadro1, cuadro2, cuadro3, cuadro4]:
         glBegin(GL_QUADS)
         glColor3f(random.random(), random.random(), random.random())   # Color aleatorio del cuadro
         for vertice in cuadro:
             glVertex2f(vertice[0], vertice[1])                         # Coordenada de dibujo
         glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        dibuja_cuadros()         
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
