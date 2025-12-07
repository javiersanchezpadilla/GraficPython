""" El objetivo de este programa es mostrar como cargar varios sprites desde una carpeta
    y mostrarlos en pantalla, permitiendo mover el sprite con las flechas del teclado.
    Estos es, pueden colocar sus sprites en una carpeta y el programa los cargara todos automaticamente, lo que 
    deben considerar (MUY IMPORTANTE!!!) es que los nombres de los archivos deben permitir ordenarlos correctamente 
    (por ejemplo: sprite_01.png, sprite_02.png, sprite_03.png, etc).


        Parte	                    Explicación
    cargar_textura	                Carga una imagen PNG y la vuelve textura OpenGL
    carga_sprites_de_carpeta	    Carga todas las imágenes de una carpeta como una lista de texturas
    sprites	                        Diccionario con 2 listas: izquierda, derecha (pde agregar arriba y abajo)
    direccion	                    Guarda hacia dónde está mirando el personaje
    indice_frame	                Dice cuál foto de la animación se está mostrando
    Animación	                    Cada 0.15 segundos cambiamos al siguiente frame
    Movimiento	                    Si presionas las flechas (izquierda, derecha) el sprite se mueve y cambia de animación
    
"""

import glfw
from OpenGL.GL import *
from PIL import Image
import os
import time


                                                # Cargar una textura expedifica con PIL 
def cargar_textura(path):
    img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture



                                                # Cargar todos los sprites de una carpeta
def carga_sprites_de_carpeta(folder):
    textures = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            textures.append(cargar_textura(os.path.join(folder, file)))
    return textures



                                                # Programa principal
def principal():
        # Inicializar GLFW
    if not glfw.init():
        return

    ventana = glfw.create_window(800, 600, "Cargar varios sprites", None, None)
    glfw.make_context_current(ventana)

    # Cargar animaciones por dirección
    sprites = {
    "left":  carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/izquierda"),
    "right": carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sprites/derecha")
    }

    # Si van a habilitar las cuatro flechas pueden usar estas líneas:

    # sprites = {
    # "down":  carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/Sprites/abajo"), 
    # "up":    carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/Sprites/arriba"),
    # "left":  carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/Sprites/izquierda"),
    # "right": carga_sprites_de_carpeta("/home/javier/Documentos/Programas/Python/Texturas/Sprites/derecha")
    # }

                                                            # Activar texturas
    glEnable(GL_TEXTURE_2D)

                                                            # Activar transparencia en PNGs
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

                                                            # Dirección actual del personaje
    direccion = "left"
    indice_frame = 0
    ultimo_valor_de_tiempo = time.time()
    velocidad_de_cada_frame = 0.15                          # segundos entre frames

    x, y = 0.0, 0.0                                         # posición del sprite

    while not glfw.window_should_close(ventana):
        glfw.poll_events()

                                                            # Movimiento y dirección de cada flecha
        if glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
            x -= 0.01
            direccion = "left"
        elif glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
            x += 0.01
            direccion = "right"

        # si habilitaron las cuatro flechas, entondes el if queda así
        # if glfw.get_key(ventana, glfw.KEY_UP) == glfw.PRESS:
        #     y += 0.01
        #     direccion = "up"
        # elif glfw.get_key(ventana, glfw.KEY_DOWN) == glfw.PRESS:
        #     y -= 0.01
        #     direccion = "down"
        # elif glfw.get_key(ventana, glfw.KEY_LEFT) == glfw.PRESS:
        #     x -= 0.01
        #     direccion= "left"
        # elif glfw.get_key(ventana, glfw.KEY_RIGHT) == glfw.PRESS:
        #     x += 0.01
        #     direccion = "right"


        # Animación (cambiar frames)
        now = time.time()
        if now - ultimo_valor_de_tiempo > velocidad_de_cada_frame:
            indice_frame = (indice_frame + 1) % len(sprites[direccion])
            ultimo_valor_de_tiempo = now

        # Dibujar
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        current_texture = sprites[direccion][indice_frame]
        glBindTexture(GL_TEXTURE_2D, current_texture)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(x - 0.1, y - 0.1)
        glTexCoord2f(1, 0); glVertex2f(x + 0.1, y - 0.1)
        glTexCoord2f(1, 1); glVertex2f(x + 0.1, y + 0.1)
        glTexCoord2f(0, 1); glVertex2f(x - 0.1, y + 0.1)
        glEnd()

        glfw.swap_buffers(ventana)

    glfw.terminate()

principal()
