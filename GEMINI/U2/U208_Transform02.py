""" NO FUNCIONA ADECUADAMENTE!!!!"""

import glfw
from OpenGL.GL import *
import math

# (Código de configuración de la ventana... es el mismo que antes)
if not glfw.init():
    raise Exception("glfw can't be initialized!")
window = glfw.create_window(800, 600, "Animación 2D", None, None)
if not window:
    glfw.terminate()
    raise Exception("glfw window can't be created!")
glfw.make_context_current(window)

# Variables para la animación
translation_x = 0.0
rotation_angle = 0.0
scale = 1.0
factor = 0.005

# El bucle principal
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.2, 0.3, 0.3, 1.0)

    # --- ¡Aquí es donde aplicamos las transformaciones! ---
    glPushMatrix() # Guarda el estado actual de la matriz de transformación

    # 1. Rotación
    glRotatef(rotation_angle, 0.0, 0.0, 1.0)
    
    # 2. Escalamiento
    glScalef(scale, scale, 1.0)
    
    # 3. Traslación
    glTranslatef(translation_x, 0.0, 0.0)

    # Dibuja el triángulo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(-0.2, -0.2)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.2, -0.2)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.2)
    glEnd()

    glPopMatrix() # Restaura el estado de la matriz

    # Actualiza las variables para la próxima iteración
    rotation_angle += 1.0
    if factor > 1 or factor < -1:
        factor = -1 * factor  # Cambia la dirección de la traslación
    # translation_x += 0.005
    translation_x += factor
    if scale > 1.5 or scale < 0.5:
        factor = -factor  # Cambia la dirección del escalamiento
    # scale += 0.001
    # scale += factor
    
    print(f"Rotación: {rotation_angle:.2f}, Traslación: {translation_x:.2f}, Escala: {scale:.2f}")
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()