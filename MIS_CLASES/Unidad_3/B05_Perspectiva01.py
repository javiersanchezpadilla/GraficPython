""" ¿si puedo hacer uso de freeglut en python?
    Es importante entender cómo se relacionan estas librerías.
    La respuesta corta es: Sí, técnicamente puedes usar FreeGLUT en Python, pero no es necesario 
    ni la mejor práctica para tu configuración actual (GLFW + PyOpenGL).

    Aquí tienes la explicación detallada y por qué es mejor seguir con el código que ya tenemos:

    1. ¿Cómo se usaría FreeGLUT en Python?
    FreeGLUT es una reimplementación moderna de la vieja librería C, GLUT. Para usarla en Python, 
    no instalas FreeGLUT por separado como un módulo de Python, sino que utilizas el enlace que ya 
    viene en la librería PyOpenGL.

    Cuando importas:

    from OpenGL.GLU import *
    from OpenGL.GLUT import * # Aquí es donde se accede a las funciones de GLUT/FreeGLUT

    Si tu sistema Linux tiene instaladas las librerías binarias de FreeGLUT, PyOpenGL puede encontrarlas 
    y permitirte usar funciones como glutWireCube().

    2. ¿Por qué es mejor evitarlo? (El Contexto Moderno)
    Te recomiendo encarecidamente que no lo hagas si quieres estabilidad, especialmente en Linux:

    Librería	        Propósito Original	                   Problema al Mezclar
    ---------------------------------------------------------------------------------
    GLFW	        Maneja la ventana, el bucle principal, 	    Es la solución moderna y limpia 
                    y la entrada de usuario.                    para la ventana.
                    
    GLUT/FreeGLUT	Solía hacer TODO (ventana, bucle, 	        Duplicidad: Usar glut para geometría 
                    entrada, utilidades).                       mientras glfw maneja la ventana puede 
                                                                causar conflictos e inestabilidad 
                                                                en el contexto de OpenGL.

    Cuando ya estás usando GLFW para la ventana, la filosofía es usar PyOpenGL para las llamadas de dibujo y 
    tú mismo definir la geometría.

    Conclusión y Solución Estándar
    
    Método glutWireCube() (Inestable):

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
glutInit()


# Variables de cámara
fov = 90  # campo de visión fov = 60 grados
eye_z = 5  # posición de la cámara en Z

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



    # --- PROYECCIÓN ---
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, 800/600, 0.1, 50)

    # --- CÁMARA ---
    glMatrixMode(GL_MODELVIEW)
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
