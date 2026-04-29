""" RELLENO DE POLIGONOS.

    El relleno de polígonos es el proceso por el cual OpenGL decide qué color 
    ponerle a los píxeles que están 'dentro' de las figuras que dibujamos 
    (como triángulos o cuadrados).

    Para que OpenGL sepa que debe rellenar la figura y no solo dibujar las 
    líneas, usamos 
    
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    aunque por defecto ya viene configurado así.

    1. Relleno con Color Homogéneo (Flat Shading)
    ---------------------------------------------
    El color homogéneo es cuando toda la figura tiene exactamente el mismo 
    tono. Es como si pintaras una pared con un solo bote de pintura.
    ¿Cómo funciona?: Solo necesitas definir el color una vez antes de poner 
    los puntos (vértices). OpenGL aplicará ese color a todo lo que venga 
    después.

    Concepto clave: Se usa la función 
    
            glColor3f(R, G, B).

    Ejemplo 1: Un cuadrado de un solo color
"""

import glfw
from OpenGL.GL import *

def dibujar():
    # Definimos el color una sola vez (Verde Esmeralda)
    glColor3f(0.0, 0.8, 0.4) 
    
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

def main():
    if not glfw.init(): return
    ventana = glfw.create_window(600, 600, "Color Homogeneo", None, None)
    glfw.make_context_current(ventana)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        dibujar()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()

main()
