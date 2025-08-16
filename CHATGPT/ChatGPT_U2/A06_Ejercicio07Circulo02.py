""" Ejemplo que permite generar una circunferencia con OpenGL.
    Utiliza GL_TRIANGLE_FAN para dibujar un círculo.
    Permite especificar el radio y el color del círculo.

    Conceptos clave:
    - glBegin(GL_TRIANGLE_FAN): Inicia el dibujo de un círculo.
    - glVertex2f(x, y): Define los vértices del círculo.
    - glColor3f(r, g, b): Establece el color del círculo.

    Requisitos:
    - Tener instalado GLFW y PyOpenGL.
"""

import glfw
from OpenGL.GL import *
import math 

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Círculo con OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana  


def dibujar_circulo(radio, r, g, b):
    """
    The function `dibujar_circulo` draws a circle with a specified radius and color using OpenGL in
    Python.
    
    :param radio: The parameter "radio" in the function "dibujar_circulo" represents the radius of the
    circle that you want to draw. It determines the size of the circle that will be drawn on the screen
    :param r: The parameter `r` in the `dibujar_circulo` function represents the red component of the
    color used to draw the circle. It is a value between 0.0 and 1.0 that determines the intensity of
    the red color in the circle
    :param g: The 'g' parameter in the function `dibujar_circulo` is used to specify the green component
    of the color of the circle to be drawn. It is a value between 0.0 and 1.0, representing the
    intensity of the green color in the RGB color
    :param b: The parameter `b` in the `dibujar_circulo` function represents the blue component of the
    color used to draw the circle. In the `glColor3f` function, `r`, `g`, and `b` represent the red,
    green, and blue components of
    """
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Centro del círculo
    for ang in range(0, 361, 10):  # Dibujar el círculo en segmentos de 10 grados
        ang_rad = math.radians(ang)
        print(f"Ángulo: {ang}° → Valor radianes: {ang_rad:.2f}")  # Mostrar el ángulo en grados y su valor en radianes
        # Calcular las coordenadas del vértice del círculo
        glVertex2f(math.cos(ang_rad) * radio, math.sin(ang_rad) * radio)
    glEnd() 



# Aquí pondremos el código para dibujar primitivas
ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    tiempo = glfw.get_time()

    # Dibujar un círculo en el centro de la ventana
    glPushMatrix()
    glTranslatef(0, 0, 0)  # Mover al centro
    dibujar_circulo(0.5, 1.0, 0.0, 0.0)  # Círculo rojo
    glPopMatrix()

    glfw.swap_buffers(ventana)

glfw.terminate()
