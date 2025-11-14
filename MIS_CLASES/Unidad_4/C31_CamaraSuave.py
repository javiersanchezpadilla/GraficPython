""" Manejo de la camara suave



    ¿Qué parte es la “cámara suave”?

    Exactamente esta:

    camera_x += (player_x - camera_x) * smoothness
    camera_y += (player_y - camera_y) * smoothness

"""


import glfw
from OpenGL.GL import *
from math import fabs

# -----------------------------------
# Inicializar GLFW y ventana
# -----------------------------------
glfw.init()
window = glfw.create_window(800, 600, "Camara Suave Ejemplo", None, None)
glfw.make_context_current(window)

# -----------------------------------
# Posición del jugador y la cámara
# -----------------------------------
player_x = 0.0
player_y = 0.0

camera_x = 0.0
camera_y = 0.0

# Factor de suavidad (0.05 es suave)
smoothness = 0.05

# -----------------------------------
# Función para dibujar un cuadrito
# -----------------------------------
def draw_square(x, y, size=0.1):
    glBegin(GL_QUADS)
    glVertex2f(x - size, y - size)
    glVertex2f(x + size, y - size)
    glVertex2f(x + size, y + size)
    glVertex2f(x - size, y + size)
    glEnd()

# -----------------------------------
# Bucle principal
# -----------------------------------
while not glfw.window_should_close(window):
    glfw.poll_events()

    # -----------------------------------
    # Movimiento del jugador
    # -----------------------------------
    speed = 0.02
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        player_x += speed
    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        player_x -= speed
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        player_y += speed
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        player_y -= speed

    # -----------------------------------
    # Cámara suave (Lerp)
    # -----------------------------------
    camera_x += (player_x - camera_x) * smoothness
    camera_y += (player_y - camera_y) * smoothness

    # -----------------------------------
    # Limpiar pantalla
    # -----------------------------------
    glClear(GL_COLOR_BUFFER_BIT)

    # -----------------------------------
    # Aplicar la cámara (transformación)
    # -----------------------------------
    glLoadIdentity()
    glTranslatef(-camera_x, -camera_y, 0)

    # -----------------------------------
    # Dibujar jugador
    # -----------------------------------
    glColor3f(1, 1, 0)   # Amarillo
    draw_square(player_x, player_y)

    # Dibujar "suelo" para notar el movimiento
    glColor3f(0.5, 0.5, 1)
    for i in range(-10, 11):
        draw_square(i * 0.5, -1.0, 0.05)

    glfw.swap_buffers(window)

glfw.terminate()
