""" Manejo de los puertos de visión
    los puertos de visión o viewports son fundamentales para controlar dónde se dibujan tus gráficos dentro de 
    la ventana de la aplicación.
    Un Puerto de Visión es la región rectangular de la ventana de tu aplicación a la que OpenGL mapea el espacio 
    de coordenadas normalizadas (el cubo de visión con coordenadas de -1.0 a 1.0).
    En términos sencillos:Es el área en la pantalla donde realmente se produce el dibujo. Es la etapa final en el 
    proceso de transformación de vértices.La Función Clave: glViewport()El puerto de visión se define usando la 
    función de OpenGL:
            glViewport(x, y, ancho, alto);
    Donde:
        'x' y 'y': La posición (coordenadas de píxel) de la esquina inferior izquierda del viewport dentro de la ventana.
        ancho y alto: El ancho y el alto del viewport en píxeles.

    PROPOSITO Y FUNCIONAMIENTO. 
    --------------------------
    1) Mapeo de Coordenadas. El principal trabajo del viewport es la transformación de coordenadas.
          1. Tu geometría se define en el espacio de clip (coordenadas normalizadas, de -1.0 a 1.0).
          2. El viewport toma este cubo de -1.0 a 1.0 y lo escala y desplaza para ajustarlo al rectángulo de píxeles que 
             tú definiste con glViewport().
           
          Si tu ventana es de 800 x 600 píxeles, y llamas a glViewport(0, 0, 800, 600), un punto en OpenGL en (1.0, 1.0) 
          se mapea a la esquina superior derecha de la ventana (800, 600), y el origen (0.0, 0.0) se mapea al centro (400, 300).
        
    2) Redimensionamiento de Ventanas. Cuando el usuario cambia el tamaño de la ventana de tu aplicación, el viewport no 
       se ajusta automáticamente. Es tu responsabilidad llamar a glViewport() dentro de un "callback de redimensionamiento"
       de GLFW para asegurarte de que tus gráficos siempre llenen toda la ventana correctamente.
       
    3) Múltiples VistasPuedes usar puertos de visión para crear múltiples paneles de visualización dentro de una sola 
       ventana.Por ejemplo, podrías dividir una ventana por la mitad para mostrar dos vistas diferentes de la misma escena 
       (como una vista de primera persona y un mapa superior) o para renderizar dos cámaras diferentes. Simplemente llamas 
       a glViewport() para definir el primer rectángulo, dibujas, y luego llamas a glViewport() para definir el segundo 
       rectángulo y vuelves a dibujar.

    IMPLEMENTACION:
    ---------------
    def framebuffer_size_callback(window, width, height):
    # Esta función se llama automáticamente cuando la ventana se redimensiona.
    
    # ¡Llamada clave! Le dice a OpenGL que el área de dibujo debe 
    # ajustarse a las nuevas dimensiones (width, height) de la ventana.
    glViewport(0, 0, width, height)

# En tu función main() después de crear la ventana:
    glfw.set_framebuffer_size_callback(ventana, framebuffer_size_callback)
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
    glColor3f(1.0, 0.0, 0.0)
    glViewport(0, 300, 300, 300)
    glBegin(GL_QUADS)
    glVertex3i(-5,-5, 0)
    glVertex3i(-5, 5, 0)
    glVertex3i( 5, 5, 0)
    glVertex3i( 5,-5, 0)
    glEnd()
    glColor3f(0.0, 1.0, 0.0)
    glViewport(300, 300, 300, 300)
    glBegin(GL_TRIANGLES)
    glVertex3i(-5,-5, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5,-5, 0)
    glEnd()
    glColor3f(0.0, 0.0, 1.0)
    glViewport(0, 0, 300, 300)
    glBegin(GL_POLYGON)
    glVertex3i(-5, 0, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5, 0, 0)
    glVertex3i( 5,-5, 0)
    glEnd()
    glColor3f(1.0, 1.0, 0.0)
    glViewport(300, 0, 300, 300)
    glBegin(GL_POLYGON)
    glVertex3i(-5, 0, 0)
    glVertex3i( 0, 5, 0)
    glVertex3i( 5, 0, 0)
    glVertex3i( 0,-5, 0)
    glEnd()
    glColor3f(0.278, 0.545,.003);

    

def main():
    ventana_ancho = 600
    ventana_alto = 600
    ventana = iniciar_ventana()

    # Configurar la proyección para trabajar con coordenadas de píxeles
    configurar_coordenadas_ventana(ventana_ancho, ventana_alto)
    glClearColor(0.0, 0.0, 0.2, 1.0) # Fondo azul oscuro
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

