""" PARALLAX con el perosnaje

    Controles:
    - Flecha derecha: Mover personaje hacia la izquierda (el fondo simula moverse a la derecha)
    - Flecha izquierda: Mover personaje hacia la derecha (el fondo simula moverse a la izquierda)

"""

import glfw
from OpenGL.GL import *
from PIL import Image
import time
import os

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


                                                            # Cargar carpeta de sprites
def carga_sprites_de_carpeta(folder):
    texturas = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            texturas.append(cargar_textura(os.path.join(folder, file))) 
    return texturas



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

                                                            # **********  CARGAR LAS LISTAS DE LOS SPRITES PARA CADA DIRECCION
    sprites = {
    "left":  carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/izquierda"),
    "right": carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/derecha")
    }

    direccion = "right"
    indice_del_frame = 0
    pos_jugador_x, pos_jugador_y = 0.0, -0.6

                                                            # Bucle principaa
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
                                                            # Si presionas tecla derecha el scroll es positivo
        if glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
            for i in range(len(posicion_scroll_en_x)):
                posicion_scroll_en_x[i] += velodiad_del_scroll[i]
            direccion = "right"
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])

                                                            # Si presionas tecla izquierda el scroll positivo
        if glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
            for i in range(len(posicion_scroll_en_x)):
                posicion_scroll_en_x[i] -= velodiad_del_scroll[i]
            direccion = "left"
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])


        glClear(GL_COLOR_BUFFER_BIT)                        # DIBUJAMOS TODA LA ESCENA *****************                                                            
        for i, tex in enumerate(capas):
            glBindTexture(GL_TEXTURE_2D, tex)

            glBegin(GL_QUADS)
            glTexCoord2f(0 + posicion_scroll_en_x[i], 0); glVertex2f(-1, -1)
            glTexCoord2f(1 + posicion_scroll_en_x[i], 0); glVertex2f( 1, -1)
            glTexCoord2f(1 + posicion_scroll_en_x[i], 1); glVertex2f( 1,  1)
            glTexCoord2f(0 + posicion_scroll_en_x[i], 1); glVertex2f(-1,  1)
            glEnd()

        # En este caso el sprite se dibuja en la posición (pos_jugador_x, pos_jugador_y)
        # voy a considerar los cuatro sentidos de movimiento, por lo que la posición Y también puede cambiar
        # en caso de solo usar izquierda y derecha, solo la posición X cambiará
        # pero queda preparado para que puedan agregar arriba y abajo si lo desean
        textura_actual_personaje = sprites[direccion][indice_del_frame]          # Sprite animado
        glBindTexture(GL_TEXTURE_2D, textura_actual_personaje)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(pos_jugador_x - 0.1, pos_jugador_y - 0.1)
        glTexCoord2f(1, 0); glVertex2f(pos_jugador_x + 0.1, pos_jugador_y - 0.1)
        glTexCoord2f(1, 1); glVertex2f(pos_jugador_x + 0.1, pos_jugador_y + 0.1)
        glTexCoord2f(0, 1); glVertex2f(pos_jugador_x - 0.1, pos_jugador_y + 0.1)
        glEnd()

        glfw.swap_buffers(ventana)
    glfw.terminate()


programa_principal()
