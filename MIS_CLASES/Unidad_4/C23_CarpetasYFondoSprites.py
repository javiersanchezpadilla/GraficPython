"""



EN CONSTRUCCIÓN
"""

import glfw
from OpenGL.GL import *
from PIL import Image
import os
import time

# ------------------------------------------------------
# Función para cargar texturas usando Pillow (PIL)
# ------------------------------------------------------
def load_texture(path):
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
def load_sprite_folder(folder):
    textures = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            textures.append(load_texture(os.path.join(folder, file))[0])
    return textures

# ------------------------------------------------------
# Iniciar GLFW
# ------------------------------------------------------
glfw.init()
window = glfw.create_window(800, 600, "Sprite + Fondo con Scroll", None, None)
glfw.make_context_current(window)

# ------------------------------------------------------
# Cargar el fondo
# ------------------------------------------------------
background_tex, bg_w, bg_h = load_texture("background.png")

bg_scroll = 0.0        # posición del fondo
bg_speed = 0.01        # velocidad del scroll

# ------------------------------------------------------
# Cargar animaciones del sprite
# ------------------------------------------------------
sprites = {
    "down":  load_sprite_folder("sprites/down"),
    "up":    load_sprite_folder("sprites/up"),
    "left":  load_sprite_folder("sprites/left"),
    "right": load_sprite_folder("sprites/right")
}

direction = "down"
frame_index = 0
last_time = time.time()
frame_speed = 0.15

player_x, player_y = 0.0, -0.2

# ------------------------------------------------------
# Bucle principal
# ------------------------------------------------------
while not glfw.window_should_close(window):
    glfw.poll_events()

    moving = False

    # --------------------------------------------------
    # Movimiento y control de dirección
    # --------------------------------------------------
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        bg_scroll -= bg_speed
        direction = "right"
        moving = True
    elif glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        bg_scroll += bg_speed
        direction = "left"
        moving = True
    elif glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        player_y += 0.01
        direction = "up"
        moving = True
    elif glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        player_y -= 0.01
        direction = "down"
        moving = True

    # --------------------------------------------------
    # Animación del personaje
    # --------------------------------------------------
    now = time.time()
    if moving and now - last_time > frame_speed:
        frame_index = (frame_index + 1) % len(sprites[direction])
        last_time = now

    # --------------------------------------------------
    # Dibujar
    # --------------------------------------------------
    glClear(GL_COLOR_BUFFER_BIT)

    # ----------------------------
    # Fondo con scroll
    # ----------------------------
    glBindTexture(GL_TEXTURE_2D, background_tex)

    glBegin(GL_QUADS)
    
    # Mover el fondo usando coordenadas de textura
    glTexCoord2f(0 + bg_scroll, 0); glVertex2f(-1, -1)
    glTexCoord2f(2 + bg_scroll, 0); glVertex2f( 1, -1)
    glTexCoord2f(2 + bg_scroll, 1); glVertex2f( 1,  1)
    glTexCoord2f(0 + bg_scroll, 1); glVertex2f(-1,  1)
    
    glEnd()

    # ----------------------------
    # Sprite animado
    # ----------------------------
    current_texture = sprites[direction][frame_index]
    glBindTexture(GL_TEXTURE_2D, current_texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(player_x - 0.1, player_y - 0.1)
    glTexCoord2f(1, 0); glVertex2f(player_x + 0.1, player_y - 0.1)
    glTexCoord2f(1, 1); glVertex2f(player_x + 0.1, player_y + 0.1)
    glTexCoord2f(0, 1); glVertex2f(player_x - 0.1, player_y + 0.1)
    glEnd()

    glfw.swap_buffers(window)

glfw.terminate()
