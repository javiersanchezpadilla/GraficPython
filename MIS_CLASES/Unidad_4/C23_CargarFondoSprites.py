""" En este codigo se muestra como cargar un fondo de pantalla (background) que se desplaza horizontalmente
    mientras se muestra un sprite animado encima del fondo.
    al haber movimiento del fondo, se da la sensación de que el sprite se mueve.

    ELEMENTOS IMPORTANTES A CONSIDERAR:
        1) Carga de texturas usando Pillow (PIL)
        2) Carga de carpeta de sprites
        3) Animación de sprites
        4) Movimiento del fondo (scroll)
        5) Movimiento del sprite
        6) Combinación de sprite animado + fondo con scroll
        7) Manejo de transparencia
        8) Manejo de teclado para mover el sprite y el fondo

"""

import glfw
from OpenGL.GL import *
from PIL import Image
import os
import time


def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Movimiento del fondo con movimiento del sprite", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana



                                                            # Función para cargar texturas usando Pillow (PIL)
def cargar_textura(path):
    img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture, img.width, img.height



                                                            # Cargar carpeta de sprites
def carga_sprites_de_carpeta(folder):
    textures = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            textures.append(cargar_textura(os.path.join(folder, file))[0])
    return textures



                                                            # funcion principal
def funcion_principal():
    ventana = iniciar_ventana()
                                                            # Activar texturas
    glEnable(GL_TEXTURE_2D)
                                                            # Activar transparencia en PNGs
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glfw.make_context_current(ventana)
                                                            # *********   CARGAR EL FONDO

    background_tex, bg_w, bg_h = cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/FondoSprite02.bmp")

    posicion_del_fondo = 0.0                                # posición del fondo
    velocidad_del_fondo = 0.01                              # velocidad del scroll

                                                            # **********  CARGAR LAS LISTAS DE LOS SPRITES PARA CADA DIRECCION
    sprites = {
    "left":  carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/izquierda"),
    "right": carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/derecha")
    }

    direccion = "right"
    indice_del_frame = 0
    ultimo_tiempo = time.time()
    velocidad_del_frame = 0.15
    pos_jugador_x, pos_jugador_y = 0.0, -0.6

                                                            # Bucle principal
    while not glfw.window_should_close(ventana):
        glfw.poll_events()

        se_esta_moviendo = False

                                                            # Movimiento y control de dirección
        if glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
            posicion_del_fondo += velocidad_del_fondo
            direccion = "right"
            se_esta_moviendo = True
        elif glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
            posicion_del_fondo -= velocidad_del_fondo
            direccion = "left"
            se_esta_moviendo = True


        # En caso de usar las cuatro direcciones, pueden agregar estas líneas para limitar el movimiento del jugador
        # if glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
        #     posicion_del_fondo += velocidad_del_fondo
        #     direccion = "right"
        #     se_esta_moviendo = True
        # elif glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
        #     posicion_del_fondo -= velocidad_del_fondo
        #     direccion = "left"
        #     se_esta_moviendo = True
        # elif glfw.get_key(ventana, glfw.KEY_UP) == glfw.PRESS:
        #     pos_jugador_y += 0.01
        #     direccion = "up"
        #     se_esta_moviendo = True
        # elif glfw.get_key(ventana, glfw.KEY_DOWN) == glfw.PRESS:
        #     pos_jugador_y -= 0.01
        #     direccion = "down"
        #     se_esta_moviendo = True


                                                            # Animación del personaje
        now = time.time()
        if se_esta_moviendo and now - ultimo_tiempo > velocidad_del_frame:
            indice_del_frame = (indice_del_frame + 1) % len(sprites[direccion])
            ultimo_tiempo = now

                                                            
        glClear(GL_COLOR_BUFFER_BIT)                        # Dibujar la escena
                                                            
        glBindTexture(GL_TEXTURE_2D, background_tex)        # Fondo con scroll

        # observen como cargo dos veces la misma textura sobre el poligono, en caso de que no
        # les guste solo cambien el '2' por un '1' en las coordenadas de textura
        glBegin(GL_QUADS)
        glTexCoord2f(0 + posicion_del_fondo, 0); glVertex2f(-1, -1)     # mover el fondo usando
        glTexCoord2f(2 + posicion_del_fondo, 0); glVertex2f( 1, -1)     # las coordenadas de textura
        glTexCoord2f(2 + posicion_del_fondo, 1); glVertex2f( 1,  1)
        glTexCoord2f(0 + posicion_del_fondo, 1); glVertex2f(-1,  1)
        glEnd()


        textura_actual_personaje = sprites[direccion][indice_del_frame]          # Sprite animado
        glBindTexture(GL_TEXTURE_2D, textura_actual_personaje)

        # En este caso el sprite se dibuja en la posición (pos_jugador_x, pos_jugador_y)
        # voy a considerar los cuatro sentidos de movimiento, por lo que la posición Y también puede cambiar
        # en caso de solo usar izquierda y derecha, solo la posición X cambiará
        # pero queda preparado para que puedan agregar arriba y abajo si lo desean
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(pos_jugador_x - 0.1, pos_jugador_y - 0.1)
        glTexCoord2f(1, 0); glVertex2f(pos_jugador_x + 0.1, pos_jugador_y - 0.1)
        glTexCoord2f(1, 1); glVertex2f(pos_jugador_x + 0.1, pos_jugador_y + 0.1)
        glTexCoord2f(0, 1); glVertex2f(pos_jugador_x - 0.1, pos_jugador_y + 0.1)
        glEnd()

        glfw.swap_buffers(ventana)
    glfw.terminate()


funcion_principal()
