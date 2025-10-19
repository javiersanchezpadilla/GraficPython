""" Manejo de los puertos de visión.
    En este ejercicio se manejaran puertos de vision independientes para cada figura
"""

import glfw
from OpenGL.GL import *


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(600, 600, "Uso de los puertos de vision", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def configurar_coordenadas_ventana(menos_x, mas_x, menos_y, mas_y):
    """Configura la proyección para usar coordenadas de píxeles (ventana)."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    # Esto mapea [0, ancho] en X y [0, alto] en Y
    glOrtho(menos_x, mas_x, menos_y, mas_y, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def framebuffer_size_callback(window, width, height):
    # Esta función se llama automáticamente cuando la ventana se redimensiona.
    # ¡Llamada clave! Le dice a OpenGL que el área de dibujo debe 
    # ajustarse a las nuevas dimensiones (width, height) de la ventana.
    glViewport(0, 0, width, height)


def dibuja_fondo(rojo, verde, azul):
    glColor3f(rojo, verde, azul)
    glBegin(GL_QUADS)
    glVertex3i(-10,-10, 0)
    glVertex3i(-10, 10, 0)
    glVertex3i( 10, 10, 0)
    glVertex3i( 10,-10, 0)
    glEnd()


def dibujar():

    glViewport(0, 300, 300, 300)
    dibuja_fondo(0.35, 0.46, 0.62)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3i(-5,-5, 0)
    glVertex3i(-5, 5, 0)
    glVertex3i( 5, 5, 0)
    glVertex3i( 5,-5, 0)
    glEnd()

    glViewport(300, 300, 300, 300)
    dibuja_fondo(0.80, 0.16, 0.25)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3i(-5,-5, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5,-5, 0)
    glEnd()

    glViewport(0, 0, 300, 300)
    dibuja_fondo(0.20, 0.30, 0.50)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3i(-5, 0, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5, 0, 0)
    glVertex3i( 5,-5, 0)
    glEnd()

    glViewport(300, 0, 300, 300)
    dibuja_fondo(0.1, 0.8,0.1)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3i(-5, 0, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5, 0, 0)
    glVertex3i( 0,-5, 0)
    glEnd()
    glColor3f(0.278, 0.545,.003);

    
if __name__ == "__main__":
    ventana_ancho = 600
    ventana_alto = 600
    ventana = iniciar_ventana()

    # Configurar la proyección para trabajar con coordenadas de píxeles
    configurar_coordenadas_ventana(-10.0, 10.0, -10.0, 10.0)
    glClearColor(0.0, 0.0, 0.2, 1.0) # Fondo azul oscuro
    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    
    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        # Llama a la función de dibujo de mapa de bits
        dibujar()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()
