"""
        Parte	                    Explicación
    load_texture	        Carga una imagen PNG y la vuelve textura OpenGL
    load_sprite_folder	    Carga todas las imágenes de una carpeta como una lista de texturas
    sprites	                Diccionario con 4 listas: arriba, abajo, izquierda, derecha
    direction	            Guarda hacia dónde está mirando el personaje
    frame_index	            Dice cuál foto de la animación se está mostrando
    Animación	            Cada 0.15 segundos cambiamos al siguiente frame
    Movimiento	            Si presionas ↑ ↓ ← → el sprite se mueve y cambia de animación

    
    C+ODIGO NO TERMINADO AÚN 

"""

import glfw
from OpenGL.GL import *
from PIL import Image
import os
import time

# -------------------------
# Cargar una textura con PIL
# -------------------------
def load_texture(path):
    img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture

# -------------------------
# Cargar una carpeta de sprites
# -------------------------
def load_sprite_folder(folder):
    textures = []
    for file in sorted(os.listdir(folder)):
        if file.endswith(".png"):
            textures.append(load_texture(os.path.join(folder, file)))
    return textures

# =========================
# Programa principal
# =========================

glfw.init()
window = glfw.create_window(800, 600, "Sprite con animación por dirección", None, None)
glfw.make_context_current(window)

# Cargar animaciones por dirección
sprites = {
    "down":  load_sprite_folder("sprites/down"),
    "up":    load_sprite_folder("sprites/up"),
    "left":  load_sprite_folder("sprites/left"),
    "right": load_sprite_folder("sprites/right")
}

# Dirección actual del personaje
direction = "down"
frame_index = 0
last_time = time.time()
frame_speed = 0.15  # segundos entre frames

x, y = 0.0, 0.0     # posición del sprite

# =========================
# Bucle principal
# =========================
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Movimiento y dirección
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        y += 0.01
        direction = "up"
    elif glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        y -= 0.01
        direction = "down"
    elif glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        x -= 0.01
        direction = "left"
    elif glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        x += 0.01
        direction = "right"

    # Animación (cambiar frames)
    now = time.time()
    if now - last_time > frame_speed:
        frame_index = (frame_index + 1) % len(sprites[direction])
        last_time = now

    # Dibujar
    glClear(GL_COLOR_BUFFER_BIT)

    current_texture = sprites[direction][frame_index]
    glBindTexture(GL_TEXTURE_2D, current_texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x - 0.1, y - 0.1)
    glTexCoord2f(1, 0); glVertex2f(x + 0.1, y - 0.1)
    glTexCoord2f(1, 1); glVertex2f(x + 0.1, y + 0.1)
    glTexCoord2f(0, 1); glVertex2f(x - 0.1, y + 0.1)
    glEnd()

    glfw.swap_buffers(window)

glfw.terminate()
