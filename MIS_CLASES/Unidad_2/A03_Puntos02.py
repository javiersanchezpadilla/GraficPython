""" GL_POINTS   Primitiva PUNTO. 
    glPointSize(tamaño)     Permite definir el tamaño del punto (en pixeles).

    En este ejemplo dibujamos varios puntos rojos de diferentes tamaños en la ventana.
        
    Las coordenadas están normalizadas: X e Y van de -1 a 1.
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

def dibuja_punto():
      # Tamaño del punto

    glColor3f(1, 0, 0)                  # Color rojo

    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(-0.9, 0.0)              
    glEnd()

    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(-0.8, 0.0)              
    glEnd()

    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(-0.7, 0.0)              
    glEnd()

    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(-0.6, 0.0)              
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(-0.5, 0.0)              
    glEnd()

    glPointSize(6)
    glBegin(GL_POINTS)
    glVertex2f(-0.4, 0.0)              
    glEnd()

    glPointSize(7)
    glBegin(GL_POINTS)
    glVertex2f(-0.3, 0.0)
    glEnd()

    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(-0.2, 0.0) 
    glEnd()

    glPointSize(9)
    glBegin(GL_POINTS)
    glVertex2f(-0.1, 0.0) 
    glEnd()

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0) 
    glEnd()

    glPointSize(20)
    glBegin(GL_POINTS)
    glVertex2f(0.5, 0.0) 
    glEnd()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        dibuja_punto()         

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
