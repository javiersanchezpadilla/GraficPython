""" Dibujano de un triángulo en 2D 
    En este ejemplo no se define la inicialización de la ventana en una función reutilizable,
    sino que se hace directamente en el código principal.
    La ventana se crea con GLFW y se utiliza OpenGL para dibujar un triángulo.
"""

import glfw
from OpenGL.GL import *

# (Código de configuración de la ventana... es el mismo que antes)
if not glfw.init():
    raise Exception("glfw can't be initialized!")
window = glfw.create_window(800, 600, "Mi primer triángulo", None, None)
if not window:
    glfw.terminate()
    raise Exception("glfw window can't be created!")
glfw.make_context_current(window)

# El bucle principal
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 0.0, 0.0, 1.0) # Establece el color de limpieza a rojo

    # --- ¡Aquí es donde ocurre la magia! ---
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glVertex2f(0.0, 0.5)    # Vértice superior central
    glEnd()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
