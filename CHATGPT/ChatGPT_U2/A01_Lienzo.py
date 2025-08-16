""" Este ejemplo muestra cómo crear una ventana OpenGL básica usando GLFW.
    Se utiliza la biblioteca GLFW para manejar la ventana y eventos.
    Se limpia el buffer de color y se establece un color de fondo.
    Asegúrate de tener instaladas las bibliotecas GLFW y PyOpenGL.

    $ pip3 install PyOpenGL PyOpenGL_accelerate
    $ pip3 install glfw


    ¿Qué hace este código?

    Abre una ventana de 640x480 píxeles
    Pinta un fondo azul grisáceo
    Se mantiene abierta hasta que el usuario la cierra

    Como ejercicio, intenta cambiar el color de fondo a rojo oscuro
"""

import glfw
from OpenGL.GL import *

# Inicializa GLFW
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

# Crear una ventana
ventana = glfw.create_window(640, 480, "Mi primera ventana OpenGL", None, None)
if not ventana:
    glfw.terminate()
    raise Exception("No se pudo crear la ventana")

# Establece el contexto de OpenGL
glfw.make_context_current(ventana)

# Loop principal
while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)    # Limpia el buffer de color
    glClearColor(0.2, 0.3, 0.4, 1)  # Color de fondo (azul grisáceo)

    # glClearColor(0.5, 0.1, 0.1, 1)  # RGB: rojo oscuro
    
    # Aquí iría el dibujo de primitivas
    
    glfw.swap_buffers(ventana)  # Intercambia los buffers
    glfw.poll_events()          # Procesa eventos

# Finaliza GLFW
glfw.terminate()
