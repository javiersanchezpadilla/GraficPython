""" Manejo de los puertos de visión.
    En este ejercicio se manejaran puertos de vision independientes para cada figura

    glViewport(x, y, Ancho, Alto)

    Parametros
    x, y            Especifica la esquina inferior izquierda del rectangulo del viewport. 
                    (El valor inicial es (0, 0))
    Ancho, Alto     Especifica el ancho y el alto del puerto de vision. Cuando un contexto GL 
                    se adjunta por primera vez a una ventana, el ancho y el alto se establecen 
                    según las dimensiones de esa ventana (pero en PIXELES).

    Las ubicaciones en la ventana y los tamaños de cada ventana son en PIXELES (ignora la escala),
    la escala la considera para manejo interno de las representaciones graficas dentro de la misma
    ventana.

    Para una ventana definida de 600x600 para dividirla en cuatro ventanas teniendo una escala 
    de -10 a 10 para cada uno de los ejes (x,y,z)

                                                 (300, 600)             
                    (0, 600)   +----------------+----------------+ (600, 600)
                               |                |                |
                               |                |                |
                               |                |                |             *** glViewport(300,300,300,300)
                               |                |  ***           |
    glViewport(0,300,300,300)  |                | (300,300)      | 
                      (0, 300) +----------------+----------------+ (600, 300)
				               |                |                |
                               |                |                |
				               |                |                |
				               |                |                |
    glViewport(0,0,300,300)	   |                |                | 
			            (0, 0) +----------------+----------------+ (600, 0)
                                                (300, 0)          
                                                glViewport(300,0,300,300)     

    En el ejemplo mostrado arriba cada puerto de visión fue creado de 300x300 pixeles.

    Ejemplo de uso de los puertos de visión en OpenGL con Python y GLFW: 

    El primer puerto de visión se crea en la esquina inferior izquierda: glViewport(0,0,300,300)
    el segundo puerto de visión en la esquina inferior derecha:          glViewport(300,0,300,300)
    el tercer puerto de visión en la esquina superior izquierda:         glViewport(0,300,300,300)
    el cuarto puerto de visión en la esquina superior derecha.           glViewport(300,300,300,300)

    Ejemplo de como se interpreta la definición de uno de los puertos de visión:

        glViewport(300,0,300,300)       (posición_x, posición_y, ancho_en_pixeles, alto_en_pixeles)
    
    Significa que el puerto de visión empieza en la posición (300,0) de la ventana principal
    y tendrá un tamaño de 300 pixeles de ancho por 300 pixeles de alto

    Podmeos cambiar el orden de creación de los puertos de visión para ver como afecta al resultado final.
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


def dibujar():

    glViewport(0, 0, 300, 300)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3i(-5,-5, 0)
    glVertex3i(-5, 5, 0)
    glVertex3i( 5, 5, 0)
    glVertex3i( 5,-5, 0)
    glEnd()
    
    glViewport(300, 0, 300, 300)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3i(-5,-5, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5,-5, 0)
    glEnd()
    
    glViewport(0, 300, 300, 300)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3i(-5, 0, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5, 0, 0)
    glVertex3i( 5,-5, 0)
    glEnd()
    
    glViewport(300, 300, 300, 300)
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
        # Llama a la función de dibujo para los poligonos
        dibujar()
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()
