""" El siguiente código permite entender el concepto de profundidad en una escena 3D.
    Usando OpenGL y GLFW, se dibujan dos cuadros (quads) a distintas distancias en el eje Z.
    El cuadro más cercano se dibuja en verde y el más lejano en amarillo.
    
    Para este ejemplo, dadas las coordenadas y trabajando nuestros programas como lo hemos 
    hecho hasta el momento se esperaría que el cuadro amarillo estuviera atrás del cuadro verde, 
    por posicion en Z. Sin embargo, al no activar el buffer de profundidad, OpenGL dibuja los cuadros 
    en el orden en que son enviados a la tarjeta gráfica, sin considerar la profundidad.
    Por lo tanto, el cuadro amarillo (dibujado en segundo lugar) aparece encima del cuadro verde, 
    independientemente de sus posiciones en Z.
    Al activar el buffer de profundidad (con glEnable(GL_DEPTH_TEST)), OpenGL utiliza la información 
    de profundidad para determinar qué partes de los objetos son visibles y cuáles están ocultas 
    detrás de otros objetos. Esto permite que el cuadro verde (más cercano) se dibuje correctamente 
    delante del cuadro amarillo (más lejano), respetando sus posiciones en el espacio 3D. """


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(600, 600, "Uso de los puertos de vision", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def configurar_coordenadas_ventana(menos_x, mas_x, menos_y, mas_y, menos_z=-1.0, mas_z=1.0):
    # Configura la proyección para usar coordenadas de píxeles (ventana).
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    # Esto mapea [0, ancho] en X y [0, alto] en Y
    glOrtho(menos_x, mas_x, menos_y, mas_y, menos_z, mas_z)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# Función para dibujar un cuadro
def dibujar_cuadros(z1, z2):

    glColor3f(1.0, 1.0, 1.0)        # Ejes coordenados
    glBegin(GL_LINES)
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)
    glVertex3f(0.0, -15.0, 0.0)
    glVertex3f(0.0,  15.0, 0.0)
    glEnd()

    glColor3f(0.3, 0.6, 0.1)        # Cuadro verde
    glBegin(GL_QUADS)
    glVertex3f(-5.0, 12.0, z1)
    glVertex3f(5.0, 12.0, z1)
    glVertex3f(5.0, -12.0, z1)
    glVertex3f(-5.0, -12.0, z1)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)        # Cuadro amarillo
    glBegin(GL_QUADS)
    glVertex3f(-4.0, 11.0, z2)
    glVertex3f(7.0, 11.0, z2)
    glVertex3f(7.0, -7.0, z2)
    glVertex3f(-4.0, -7.0, z2)
    glEnd()



def programa_principal():
    ventana = iniciar_ventana() 
    configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
       
        # Distancias iniciales de los cuadros
        z_cuadro1 = -3   # más cercano
        z_cuadro2 = -7   # más lejano

        dibujar_cuadros(z_cuadro1, z_cuadro2) 

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
