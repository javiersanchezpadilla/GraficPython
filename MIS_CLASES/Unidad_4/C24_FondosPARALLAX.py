""" Carga de varias capas de fondo para crear un efecto parallax al moverlas a diferentes velocidades.

    CÓDIGO EN DESARROLLO

"""

import glfw
from OpenGL.GL import *
from PIL import Image
import time

# ------------------------
# Cargar una textura PIL
# ------------------------
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

# ------------------------
# Iniciar GLFW
# ------------------------
glfw.init()
window = glfw.create_window(800, 600, "Parallax Demo", None, None)
glfw.make_context_current(window)

# ------------------------
# Cargar capas de parallax
# ------------------------
layers = [
    load_texture("parallax/layer0.png"),
    load_texture("parallax/layer1.png"),
    load_texture("parallax/layer2.png"),
    load_texture("parallax/layer3.png")
]

# Velocidades de movimiento (más bajas = más lejos)
scroll_speed = [0.002, 0.004, 0.008, 0.012]

# Posición inicial del scroll
scroll_x = [0.0, 0.0, 0.0, 0.0]

# ------------------------
# Bucle principal
# ------------------------
while not glfw.window_should_close(window):
    glfw.poll_events()

    # Si presionas derecha → scroll negativo
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        for i in range(len(scroll_x)):
            scroll_x[i] -= scroll_speed[i]

    # Si presionas izquierda → scroll positivo
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        for i in range(len(scroll_x)):
            scroll_x[i] += scroll_speed[i]

    glClear(GL_COLOR_BUFFER_BIT)

    # -------- DIBUJAR TODAS LAS CAPAS -----------------
    for i, tex in enumerate(layers):
        glBindTexture(GL_TEXTURE_2D, tex)

        glBegin(GL_QUADS)

        # Nota: usamos scroll_x[i] para mover cada capa
        glTexCoord2f(0 + scroll_x[i], 0); glVertex2f(-1, -1 + i * 0.00)
        glTexCoord2f(2 + scroll_x[i], 0); glVertex2f( 1, -1 + i * 0.00)
        glTexCoord2f(2 + scroll_x[i], 1); glVertex2f( 1,  1 + i * 0.00)
        glTexCoord2f(0 + scroll_x[i], 1); glVertex2f(-1,  1 + i * 0.00)

        glEnd()

    glfw.swap_buffers(window)

glfw.terminate()
