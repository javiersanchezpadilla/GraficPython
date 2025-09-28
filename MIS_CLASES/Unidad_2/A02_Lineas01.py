""" Programa que dibuja una linea en OpenGL 
    Esta es la version mas simple del programa, donde todo el codigo esta en el cuerpo principal.
    En este ejemplo se dibuja una linea roja desde el punto (180,15) hasta el punto (10,145)
    usando coordenadas 2D.
"""

# Importamos las librias
# Como vamos a usar funciones de OpenGL, necesitamos importar las librerías
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


def proyeccion():
    """ Esta función configura la matriz de proyección para definir el espacio de coordenadas
        que vamos a utilizar para dibujar en la ventana.
        No retorna ningún valor, solo configura el estado de OpenGL.
        La función establece un sistema de coordenadas 2D donde el origen (0,0) está en la esquina
        inferior izquierda, el eje X va de 0 a 200 y el eje Y va de 0 a 150.
        Esto significa que cualquier cosa que dibujemos usando estas coordenadas se ajustará a este
        rango dentro de la ventana.
    """
    
    # Indicamos que vamos a trabajar en la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    # Limpiamos cualquier configuración anterior
    glLoadIdentity()
    # Establecemos el espacio de coordenadas de 0 a 200 en X y 0 a 150 en Y
    glOrtho(0.0, 200.0, 0.0, 150.0, -1.0, 1.0) 

    # Volvemos a la matriz de modelo-vista para dibujar
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# El bucle principal de trabajo
# Asignamos a la variable ventana el valor retornado por la función iniciar_ventana
ventana = iniciar_ventana()

proyeccion()
while not glfw.window_should_close(ventana):
    # Limpiamos la pantalla
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # Fija el color rojo para dibujar
    glColor3f(1.0, 0.0, 0.0)
    # Dibuja una línea desde (10,15) hasta (180,145)
    glBegin(GL_LINES)
    glVertex2i(180, 15)
    glVertex2i(10, 145)
    glEnd()

    # Refresca la pantalla
    # Intercambia las dos caras del lienzo para mostrar lo que hemos dibujado
    glfw.swap_buffers(ventana)
    glfw.poll_events()

# Terminamos el programa y cerramos todo
glfw.terminate()
