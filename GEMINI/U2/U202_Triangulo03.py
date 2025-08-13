""" Dándole color a tu triángulo
    Anteriormente, usaste glClearColor() para cambiar el color de toda la ventana. 
    Para darle color a un objeto específico, como nuestro triángulo, usamos una 
    función similar, glColor3f().

    Imagina que glColor3f() es como seleccionar un color de la paleta del pintor antes 
    de empezar a dibujar. La magia es que este color se mantiene activo para todos los 
    vértices que dibujes después de que lo declares, hasta que lo cambies de nuevo.

    La función glColor3f() recibe tres valores flotantes (de 0.0 a 1.0) para los 
    componentes de color:

    El primer valor es para el Rojo
    El segundo es para el Verde
    El tercero es para el Azul

    Coloreando cada vértice
    Pero, ¿qué pasa si quieres que cada vértice de tu triángulo tenga un color diferente, 
    creando un degradado? Aquí es donde OpenGL se vuelve realmente interesante. Puedes 
    declarar un color antes de cada vértice. OpenGL se encargará de "mezclar" o interpolar 
    los colores entre los vértices, creando un efecto de degradado muy suave."""


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
    glClearColor(0.0, 0.0, 0.0, 1.0) # Limpiamos a negro para que se note nuestro triángulo

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)      # Color rojo para el siguiente vértice
    glVertex2f(-0.5, -0.5)      # Vértice inferior izquierdo

    glColor3f(0.0, 1.0, 0.0)      # Color verde para el siguiente vértice
    glVertex2f(0.5, -0.5)       # Vértice inferior derecho

    glColor3f(0.0, 0.0, 1.0)      # Color azul para el siguiente vértice
    glVertex2f(0.0, 0.5)        # Vértice superior central
    glEnd()

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()
