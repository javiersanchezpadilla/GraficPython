"""

"""

import glfw
from OpenGL.GL import *
from PIL import Image
import os
import time
import pygame               # <<< Esto es solo para el audio.

# ------------------------------------------------------
# INICIALIZAR AUDIO (pygame.mixer)
# ------------------------------------------------------
pygame.mixer.init()

# Música de fondo
pygame.mixer.music.load("audio/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.5)   # volumen 50%
pygame.mixer.music.play(-1)          # repetir infinito

# Efectos de sonido
sonido_paso  = pygame.mixer.Sound("audio/paso.wav")
sonido_golpe = pygame.mixer.Sound("audio/golpe.wav")
sonido_salto = pygame.mixer.Sound("audio/salto.wav")

# ------------------------------------------------------
# Funciones para cargar texturas (igual que antes)
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


def load_sprite_folder(folder):
    textures = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            textures.append(load_texture(os.path.join(folder, file))[0])
    return textures

# ------------------------------------------------------
# Ventana GLFW
# ------------------------------------------------------
glfw.init()
window = glfw.create_window(800, 600, "Juego con Música y Sonidos", None, None)
glfw.make_context_current(window)

# ------------------------------------------------------
# Cargar fondo + sprites
# ------------------------------------------------------
background_tex, bg_w, bg_h = load_texture("background.png")

bg_scroll = 0.0
bg_speed = 0.01

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
step_cooldown = time.time()

# ------------------------------------------------------
# BUCLE PRINCIPAL
# ------------------------------------------------------
while not glfw.window_should_close(window):
    glfw.poll_events()

    moving = False

    # --------------------------------------------
    # MOVIMIENTO + SONIDOS
    # --------------------------------------------
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

    # Reproducir sonido de paso (cada 0.25 segundos)
    if moving:
        if time.time() - step_cooldown > 0.25:
            sonido_paso.play()
            step_cooldown = time.time()

    # --------------------------------------------
    # Animación del sprite
    # --------------------------------------------
    now = time.time()
    if moving and now - last_time > frame_speed:
        frame_index = (frame_index + 1) % len(sprites[direction])
        last_time = now

    # --------------------------------------------
    # Dibujar fondo con scroll
    # --------------------------------------------
    glClear(GL_COLOR_BUFFER_BIT)
    glBindTexture(GL_TEXTURE_2D, background_tex)

    glBegin(GL_QUADS)
    glTexCoord2f(0 + bg_scroll, 0); glVertex2f(-1, -1)
    glTexCoord2f(2 + bg_scroll, 0); glVertex2f( 1, -1)
    glTexCoord2f(2 + bg_scroll, 1); glVertex2f( 1,  1)
    glTexCoord2f(0 + bg_scroll, 1); glVertex2f(-1,  1)
    glEnd()

    # --------------------------------------------
    # Dibujar sprite animado
    # --------------------------------------------
    current_texture = sprites[direction][frame_index]
    glBindTexture(GL_TEXTURE_2D, current_texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(player_x - 0.1, player_y - 0.1)
    glTexCoord2f(1, 0); glVertex2f(player_x + 0.1, player_y - 0.1)
    glTexCoord2f(1, 1); glVertex2f(player_x + 0.1, player_y + 0.1)
    glTexCoord2f(0, 1); glVertex2f(player_x - 0.1, player_y + 0.1)
    glEnd()

    glfw.swap_buffers(window)

# ------------------------------------------------------
# Al cerrar, apagar audio
# ------------------------------------------------------
pygame.mixer.music.stop()
pygame.quit()
glfw.terminate()
