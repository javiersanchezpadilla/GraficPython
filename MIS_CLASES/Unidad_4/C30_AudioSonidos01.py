""" Este codigo muestra cómo añadir sonidos a un programa con OpenGL y GLFW usando Pygame.
    mediante el uso de la libreria Pygame para la gestión de audio.(solamente)

    Importante: formato de los sonidos
    ----------------------------------
    Música:     .mp3,                   .ogg
    Efectos:    .wav (recomendado)      .ogg

    ¿Por qué WAV para efectos? Porque se cargan completos en memoria (son muy rápidos y sin retraso)

    al ejecutar el programa puede oprimir las teclas del 1 al 7 para reproducir diferentes sonidos.
"""


import glfw
from OpenGL.GL import *
import pygame


glfw.init()                                         # Inicializa GLFW
window = glfw.create_window(800, 600, "Sonidos + GLFW", None, None)
glfw.make_context_current(window)

pygame.mixer.init()                                 # Iniciar sonido
                                                    # Música de fondo
pygame.mixer.music.load("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/musicafondo.mp3")              
pygame.mixer.music.play(-1)
 
sonido_explosion = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/explosion.mp3")      
sonido_game_over = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/GameOver.mp3")
sonido_laser = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/laser.mp3")
sonido_moneda = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/moneda.mp3")
sonido_ouch = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/ouch.mp3")
sonido_01 = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/sonido01.mp3")
sonido_02 = pygame.mixer.Sound("/home/javier/Documentos/Programas/Python/Texturas/PNGs/Sonidos/sonido02.mp3")


                                                    # Bucle principal
while not glfw.window_should_close(window):

    glfw.poll_events()

    if glfw.get_key(window, glfw.KEY_1) == glfw.PRESS:
        sonido_explosion.play()

    if glfw.get_key(window, glfw.KEY_2) == glfw.PRESS:
        sonido_game_over.play()

    if glfw.get_key(window, glfw.KEY_3) == glfw.PRESS:
        sonido_laser.play()

    if glfw.get_key(window, glfw.KEY_4) == glfw.PRESS:
        sonido_moneda.play()

    if glfw.get_key(window, glfw.KEY_5) == glfw.PRESS:
        sonido_ouch.play()

    if glfw.get_key(window, glfw.KEY_6) == glfw.PRESS:
        sonido_01.play()

    if glfw.get_key(window, glfw.KEY_7) == glfw.PRESS:
        sonido_02.play()

    glClear(GL_COLOR_BUFFER_BIT)

    angulo = glfw.get_time()
    glLoadIdentity()
    glRotatef(angulo * 50, 0, 0, 1)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.5)
    glEnd()

    glfw.swap_buffers(window)

glfw.terminate()
