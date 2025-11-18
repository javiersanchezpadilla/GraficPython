""" Importante: formato de los sonidos
    Música:
        .mp3
        .ogg

    Efectos:
        .wav (recomendado)
        .ogg

    ¿Por qué WAV para efectos?
    Porque se cargan completo en memoria → muy rápidos → sin retraso.

    ¿Cómo añadir sonido a combos, golpes, colisiones?
    Muy simple:

        if combo_detectado:
            sonido_hadouken.play()

        if personaje_golpea:
            sonido_golpe.play()

        if personaje_recibe_daño:
            sonido_daño.play()

"""


import glfw
from OpenGL.GL import *
import pygame

# -------------------------
# Iniciar GLFW
# -------------------------
glfw.init()
window = glfw.create_window(800, 600, "Sonidos + GLFW", None, None)
glfw.make_context_current(window)

# -------------------------
# Iniciar sonido
# -------------------------
pygame.mixer.init()

# Música de fondo
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

# Efectos
sonido_salto = pygame.mixer.Sound("salto.wav")
sonido_paso  = pygame.mixer.Sound("paso.wav")

# -------------------------
# Bucle principal
# -------------------------
while not glfw.window_should_close(window):

    glfw.poll_events()

    # Cuando presiones espacio → salto
    if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
        sonido_salto.play()

    # Sonido de pasos (ejemplo simple)
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        sonido_paso.play()

    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)

glfw.terminate()
