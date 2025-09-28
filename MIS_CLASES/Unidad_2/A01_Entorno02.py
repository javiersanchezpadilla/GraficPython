""" Esta función inicializa una ventana OpenGL usando GLFW.
    El objetivo es organizar la inicializacion de la ventana 
    a travez de una funcion que se encargará solo de eso (inicializar)
    """

# Importamos las librerias
import glfw
from OpenGL.GL import *

def iniciar_ventana():
    """
    La funcion `iniciar_ventana` inicializa una ventana GLFW con dimensiones especificas y titulo 
    :return: La funcion `iniciar_ventana` retorna la ventana GLFW como un objeto del tipo 'ventana'.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana


# ********************************************************
# **  Aquí pondremos el código para dibujar primitivas  **
# ********************************************************

# Asignamos a la variable ventana el valor retornado por la función iniciar_ventana
ventana = iniciar_ventana()

# El bucle principal
while not glfw.window_should_close(ventana):
    glClearColor(1.0, 1.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Aqui ponemos todo loque se desee
    # estamos dentro del ciclo principal
    # por lo que se repite continuamente
    

    glfw.swap_buffers(ventana)
    glfw.poll_events()

# Terminamos el programa y cerramos todo
glfw.terminate()
