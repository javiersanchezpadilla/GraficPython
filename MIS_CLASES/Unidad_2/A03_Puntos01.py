""" Esta función inicializa una ventana OpenGL usando GLFW.
    La estemos utilizando para dibujar primitivas en OpenGL.
    
    GL_POINTS   Primitiva PUNTO. Permite dibujar puntos en la ventana.
    Este ejemplo solo dibuja un punto rojo en el centro de la ventana.
    
    Las coordenadas están normalizadas: X e Y van de -1 a 1.
    El punto rojo aparecerá en el centro de la ventana.
    
    Concepto	                Descripción

    glColor3f(r,g,b)	Establece el color de acuerdo al modelo RGB (valores entre 0 y 1)
    glBegin(...)	    Inicia el dibujo de una primitiva
    glVertex2f(x,y)	    Establece una coordenada 2D
    glEnd()	            Finaliza la primitiva

    Coordenadas	De -1 a 1 tanto en X como Y
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

# NO USARE ESTA FUNCION, AHORA TRABAJAREMOS CON COORDENADAS NORMALIZADAS (-1 a 1) PARA LOS EJES X Y Y
# Al no definir una proyeccion, OpenGL usa coordenadas normalizadas por defecto.
# def proyeccion():
#     """ Esta función configura la matriz de proyección para definir el espacio de coordenadas
#         que vamos a utilizar para dibujar en la ventana.
#         No retorna ningún valor, solo configura el estado de OpenGL.
#         La función establece un sistema de coordenadas 2D donde el origen (0,0) está en la esquina
#         inferior izquierda, el eje X va de 0 a 200 y el eje Y va de 0 a 150.
#         Esto significa que cualquier cosa que dibujemos usando estas coordenadas se ajustará a este
#         rango dentro de la ventana.
#     """
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 200.0, 0.0, 150.0, -1.0, 1.0) 
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


if __name__ == "__main__":
    ventana = iniciar_ventana()
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_POINTS)
        glColor3f(1, 0, 0)                  # Color rojo
        glVertex2f(0.0, 0.0)                # Coordenada central (0,0)
        glEnd()

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()
