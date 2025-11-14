""" ESTRUCTURA DE UN PROYECTO PARA EL DESARROLLO DE UN JUEGO.

            MiniJuego2D/
        │── main.py
        │── audio/
        │     ├── musica_fondo.mp3
        │     ├── paso.wav
        │     ├── golpe.wav
        │     └── salto.wav
        │
        │── parallax/
        │     ├── layer0.png
        │     ├── layer1.png
        │     ├── layer2.png
        │     └── layer3.png
        │
        │── sprites/
            ├── up/
            │     ├── frame0.png
            │     ├── frame1.png
            │     ├── frame2.png
            │     └── ...
            ├── down/
            ├── left/
            └── right/





"""

import glfw
from OpenGL.GL import *
from PIL import Image
import pygame
import os
import time

# ===========================================================
#                 SISTEMA DE TEXTURAS (PIL)
# ===========================================================
def load_texture(path):
    img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 img.width, img.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    return texture

def load_sprite_folder(folder):
    textures = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            textures.append(load_texture(os.path.join(folder, file)))
    return textures


# ===========================================================
#                        PARALLAX
# ===========================================================
def draw_parallax(layers, scroll, speeds):
    for i, tex in enumerate(layers):
        glBindTexture(GL_TEXTURE_2D, tex)

        glBegin(GL_QUADS)
        glTexCoord2f(0 + scroll[i], 0); glVertex2f(-1, -1)
        glTexCoord2f(2 + scroll[i], 0); glVertex2f( 1, -1)
        glTexCoord2f(2 + scroll[i], 1); glVertex2f( 1,  1)
        glTexCoord2f(0 + scroll[i], 1); glVertex2f(-1,  1)
        glEnd()


# ===========================================================
#                  PERSONAJE ANIMADO
# ===========================================================
def draw_sprite(texture, x, y):
    glBindTexture(GL_TEXTURE_2D, texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x - 0.1, y - 0.1)
    glTexCoord2f(1, 0); glVertex2f(x + 0.1, y - 0.1)
    glTexCoord2f(1, 1); glVertex2f(x + 0.1, y + 0.1)
    glTexCoord2f(0, 1); glVertex2f(x - 0.1, y + 0.1)
    glEnd()


# ===========================================================
#                        MAIN GAME
# ===========================================================
def main():
    # -----------------------------
    # INICIALIZAR GLFW
    # -----------------------------
    glfw.init()
    window = glfw.create_window(800, 600, "Mini Motor 2D", None, None)
    glfw.make_context_current(window)

    # -----------------------------
    # AUDIO
    # -----------------------------
    pygame.mixer.init()

    pygame.mixer.music.load("audio/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    sonido_paso  = pygame.mixer.Sound("audio/paso.wav")
    sonido_golpe = pygame.mixer.Sound("audio/golpe.wav")
    sonido_salto = pygame.mixer.Sound("audio/salto.wav")

    # -----------------------------
    # CARGAR PARALLAX
    # -----------------------------
    layers = [
        load_texture("parallax/layer0.png"),
        load_texture("parallax/layer1.png"),
        load_texture("parallax/layer2.png"),
        load_texture("parallax/layer3.png")
    ]

    scroll = [0.0, 0.0, 0.0, 0.0]
    speeds = [0.002, 0.004, 0.008, 0.012]

    # -----------------------------
    # CARGAR SPRITES
    # -----------------------------
    sprites = {
        "down":  load_sprite_folder("sprites/down"),
        "up":    load_sprite_folder("sprites/up"),
        "left":  load_sprite_folder("sprites/left"),
        "right": load_sprite_folder("sprites/right")
    }

    direction = "down"
    frame_index = 0
    last_frame_time = time.time()
    frame_speed = 0.15  # velocidad de animación

    player_x = 0.0
    player_y = -0.3
    last_step_sound = time.time()

    # -----------------------------
    # BUCLE PRINCIPAL
    # -----------------------------
    while not glfw.window_should_close(window):
        glfw.poll_events()

        moving = False

        # -------------------------
        # Movimiento del jugador
        # -------------------------
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            scroll = [s - speeds[i] for i, s in enumerate(scroll)]
            direction = "right"
            moving = True

        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            scroll = [s + speeds[i] for i, s in enumerate(scroll)]
            direction = "left"
            moving = True

        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            player_y += 0.01
            direction = "up"
            moving = True

        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            player_y -= 0.01
            direction = "down"
            moving = True

        # Sonido de pasos
        if moving and time.time() - last_step_sound > 0.25:
            sonido_paso.play()
            last_step_sound = time.time()

        # Animación
        now = time.time()
        if moving and now - last_frame_time > frame_speed:
            frame_index = (frame_index + 1) % len(sprites[direction])
            last_frame_time = now

        # -------------------------
        # DIBUJAR
        # -------------------------
        glClear(GL_COLOR_BUFFER_BIT)

        draw_parallax(layers, scroll, speeds)

        texture = sprites[direction][frame_index]
        draw_sprite(texture, player_x, player_y)

        glfw.swap_buffers(window)

    pygame.quit()
    glfw.terminate()


main()


