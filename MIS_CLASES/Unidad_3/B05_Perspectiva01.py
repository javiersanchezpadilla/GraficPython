""" USO DE GLUPERSPECTIVE Y GLULOOKAT, EXPLICACIÓN DETALLADA.
    
    Imagina que estás mirando a través de una pirámide truncada (llamada Frustum):
    Elegir gluPerspective() es como decidir: "Quiero una toma con un ángulo de 45 grados en una 
    pantalla con relación 4:3, y solo me interesan los objetos que están entre 0.1 y 50 metros de 
    distancia."

    gluPerspective(fovy, aspect, zNear, zFar)

    fovy (Field of View Y)          Es el ángulo vertical de visión.
    Angulo PEQUEÑO (ej: 30°)        Es como usar un teleobjetivo. Verás el mundo "acercado" o 
                                    con zoom. La perspectiva es más plana.
    Ángulo GRANDE (ej: 90°)         Es como usar un gran angular. Verás más del mundo, pero con 
                                    una distorsión de perspectiva más pronunciada (los objetos 
                                    cercanos se verán muy grandes).
                                    <<<Sugerencia: Un valor común es 45 o 60.>>>
    aspect (Aspect Ratio)           Es la relación de aspecto de la ventana (ANCHO / ALTO).
                                    Esto es crucial para que los objetos no se vean estirados. 
                                    Si tu ventana es 800x600, el aspect es 800 / 600 = 1.33.
    zNear y zFar                    Son los planos de corte cercano y lejano.
    zNear                           Es la distancia mínima que la cámara ve. Los objetos más cerca 
                                    de este plano se cortan. Debe ser un valor pequeño (ej: 0.1).
    zFar                            Es la distancia máxima que la cámara ve. Los objetos más allá 
                                    de este plano no se dibujan, lo que ayuda a ahorrar recursos. 
                                    Debe ser un valor grande (ej: 50.0).

                                    

    gluLookAt(): Colocar y Apuntar la Cámara (Matriz de Vista)
    gluLookAt() define dónde está la cámara, hacia dónde está mirando y cuál es su orientación vertical.
    Su Función: Mueve el mundo entero de forma que parezca que la cámara se ha movido o rotado.

    ¿Cómo funciona?
    Esta función toma 9 argumentos que se organizan en 3 grupos de coordenadas (X, Y, Z):

    gluLookAt(eyeX, eyeY, eyeZ,               1. Posición de la Cámara (Eye)
              centerX, centerY, centerZ,      2. El Punto al que Mira (Center)
              upX, upY, upZ)                  3. La Orientación Vertical (Up)

    eye (Posición de la Cámara): ¿Dónde está el fotógrafo? Si pones (0, 0, 10), la cámara está en (0, 0, 10).
    center (Punto al que Mira): ¿Hacia dónde apunta el fotógrafo? Si pones (0, 0, 0), la cámara mira 
    directamente al origen del mundo 3D.
    up (Orientación Vertical): ¿Qué es "arriba" para la cámara? Casi siempre es (0, 1, 0). Esto significa que 
    el eje Y es la dirección vertical de tu cámara (el lado superior de la pantalla).

    Analogía:
    Usar gluLookAt(0, 2, 5, 0, 0, 0, 0, 1, 0)       es como decir: "Coloca al fotógrafo 5 metros delante del 
                                                    origen y 2 metros por encima, apuntando al centro, y mantén 
                                                    la cabeza derecha (el eje Y es arriba)."

"""

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # <-- Aqui estamos importando la biblioteca GLUT FreeGLUT para las figuras precargadas.

# Inicializar ventana
if not glfw.init():
    raise Exception("No se pudo inicializar GLFW")

window = glfw.create_window(800, 600, "gluPerspective y gluLookAt - Ejemplo básico", None, None)
glfw.make_context_current(window)
glEnable(GL_DEPTH_TEST)
glutInit()                  # Inicializar GLUT para usar cubos de alambre (figuras precargadas de GLUT)


# Variables de cámara
# fov = 90  # campo de visión fov = 60 grados
# eye_z = 5  # posición de la cámara en Z


def cubo(x, y, z, color):
    """Dibuja un cubo sencillo en la posición indicada"""
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3fv(color)
    glutWireCube(1.0)
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Juega con estos cambios:
    # Cambia el campo de visión (zoom):
    # fov = 30  # zoom in (más cerca)
    # fov = 90  # gran angular (más lejos)

    # Mueve la cámara:
    # eye_z = 10  # más lejos → todo se ve más pequeño
    # eye_z = 2   # más cerca → los cubos parecen gigantes

    # Lo que aprenderás visualmente:
    #  Acción	                        Qué cambia	                Qué representa
    # ----------------------------------------------------------------------------------------
    # Modificar fov	                Ángulo del lente	        Efecto de zoom / gran angular
    # Modificar eye_z	            Posición de la cámara	    Distancia al objeto observado
    # Cambiar center en gluLookAt	Punto hacia el que mira     Dirección de visión

    fov = 90        # campo de visión fov = 60 grados
    eye_z = 5       # posición de la cámara en Z

    glMatrixMode(GL_PROJECTION)                     # --- PROYECCIÓN ---
    glLoadIdentity()
    gluPerspective(fov, 800/600, 0.1, 50)

    glMatrixMode(GL_MODELVIEW)                      # --- CÁMARA ---
    glLoadIdentity()
    gluLookAt(0, 0, eye_z, 0, 0, 0, 0, 1, 0)
                                                    # --- ESCENA ---                    
    cubo(0, 0, 0, (1, 0, 0))     # cubo rojo (centro)
    cubo(0, 0, -3, (0, 1, 0))    # cubo verde (más lejos)
    cubo(0, 0, -6, (0, 0, 1))    # cubo azul (aún más lejos)



while not glfw.window_should_close(window):
    display()
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
