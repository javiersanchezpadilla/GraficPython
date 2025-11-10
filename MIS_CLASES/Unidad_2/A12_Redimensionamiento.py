""" El soguiente permite modificar el tamaño de la ventana y reajustar la escala automáticamente.
    Se usa la función de callback 'framebuffer_size_callback' para ajustar el viewport."""

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


# Esta es la  funcion de retorno que se llama automaticamente cuando la ventana se redimensiona.
def framebuffer_size_callback(window, width, height):
    # Esta función se llama automáticamente cuando la ventana se redimensiona.
    # ¡Llamada clave! Le dice a OpenGL que el área de dibujo debe 
    # ajustarse a las nuevas dimensiones (width, height) de la ventana.
    glViewport(0, 0, width, height)


def dibujar():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3i(-9,9, 0)
    glVertex3i(-9, 1, 0)
    glVertex3i( -1, 1, 0)
    glVertex3i( -1, 9, 0)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(4.5, 8, 0)
    glVertex3f( 1, 1, 0)
    glVertex3f( 9, 1, 0)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3i(-9, -1, 0)
    glVertex3i( -1, -1, 0)
    glVertex3i( -2, -9, 0)
    glVertex3i( -10,-9, 0)
    glEnd()
    glColor3f(1.0, 1.0, 0.0)

    glBegin(GL_POLYGON)
    glVertex3i( 5, -1, 0)
    glVertex3i( 0, -5, 0)
    glVertex3i( 5, -9, 0)
    glVertex3i( 10,-5, 0)
    glEnd()
    glColor3f(0.278, 0.545,.003);

   
def main():
    ventana_ancho = 600
    ventana_alto = 600
    ventana = iniciar_ventana()

    # Configurar la proyección para trabajar con coordenadas de píxeles
    configurar_coordenadas_ventana(-10.0, 10.0, -10.0, 10.0)
    glClearColor(0.0, 0.0, 0.2, 1.0) # Fondo azul oscuro

    # ********************************************************************************
    # ** Establecer la función de callback para el redimensionamiento de la ventana **
    # ********************************************************************************
    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
    

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        # Llama a la función de dibujo de mapa de bits
        dibujar()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
