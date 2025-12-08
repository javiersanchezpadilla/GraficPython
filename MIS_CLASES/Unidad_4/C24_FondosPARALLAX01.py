""" PARALLAX Carga de varias capas de fondo para crear un efecto parallax al moverlas a diferentes velocidades.

    Este efecto es común en videojuegos para simular profundidad en escenas 2D, es como cuando vamos en un coche 
    y los objetos cercanos parecen moverse más rápido que los lejanos, por ejemplo los árboles cercanos pasan rápido,
    mientras que las montañas en el horizonte parecen moverse lentamente y las nubes casi no se mueven (pero se mueven).
    Aquí cargamos varias capas de fondo (cielo, nubes, montañas, castillo, estrellas) y las movemos a diferentes velocidades
    para simular ese efecto de profundidad.

    Controles:
    - Flecha derecha: Mover fondo hacia la izquierda (simula moverse a la derecha)
    - Flecha izquierda: Mover fondo hacia la derecha (simula moverse a la izquierda)

    Podemos cargar las imagenes como se hizo en codigos anteriores, pero para simplificar el ejemplo.
"""

import glfw
from OpenGL.GL import *
from PIL import Image
import time

                                                        # Inicializar ventana GLFW
def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Movimiento del fondo tipo PARALLAX", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


                                                        # Cargar una textura PIL
def cargar_textura(path):
    img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()

    textura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 img.width, img.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return textura



def programa_principal():
    ventana = iniciar_ventana()                             # Inicializar ventana
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)                                      # Activar transparencia en PNGs
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                                                            # Cargar capas transparentes para efecto parallax
    capas = [
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa01_cielofondo.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa02_nubes.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa03_nubes.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa04_nubes.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa05_niebla.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa06_castillo.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa07_estrellas.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa08_estrellas.png"),
        cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Parallax/Capas/Capa09_estrellas.png")
            ]
                                                            # Velocidaaes de movimiento (más bajas = más lejos)
    velodiad_del_scroll = [0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018]   
                                                            # Posiciones iniciales de scroll
    posicion_scroll_en_x = [0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0]

                                                            # Bucle principaa
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
                                                            # Si presionas tecla derecha el scroll es positivo
        if glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
            for i in range(len(posicion_scroll_en_x)):
                posicion_scroll_en_x[i] += velodiad_del_scroll[i]

                                                            # Si presionas tecla izquierda el scroll positivo
        if glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
            for i in range(len(posicion_scroll_en_x)):
                posicion_scroll_en_x[i] -= velodiad_del_scroll[i]

        glClear(GL_COLOR_BUFFER_BIT)

                                                            # DIBUJAMOS TODA LA ESCENA *****************
        for i, tex in enumerate(capas):
            glBindTexture(GL_TEXTURE_2D, tex)

            glBegin(GL_QUADS)
            glTexCoord2f(0 + posicion_scroll_en_x[i], 0); glVertex2f(-1, -1)
            glTexCoord2f(1 + posicion_scroll_en_x[i], 0); glVertex2f( 1, -1)
            glTexCoord2f(1 + posicion_scroll_en_x[i], 1); glVertex2f( 1,  1)
            glTexCoord2f(0 + posicion_scroll_en_x[i], 1); glVertex2f(-1,  1)
            glEnd()

        glfw.swap_buffers(ventana)
    glfw.terminate()


programa_principal()
