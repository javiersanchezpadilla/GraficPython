""" Dibujano de un triángulo en 2D 
    En este ejemplo no se define la inicialización de la ventana en una función reutilizable,
    sino que se hace directamente en el código principal.
    La ventana se crea con GLFW y se utiliza OpenGL para dibujar un triángulo.
"""

import glfw
from OpenGL.GL import *

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Primitivas en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana



# El bucle principal
ventana = iniciar_ventana()
while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 0.0, 0.0, 1.0) # Establece el color de limpieza a rojo

    # --- ¡Aquí es donde ocurre la magia! ---
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glVertex2f(0.0, 0.5)    # Vértice superior central
    glEnd()

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
