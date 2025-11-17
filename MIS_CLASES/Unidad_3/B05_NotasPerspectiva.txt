""" ESTE PROGRAMA NO HACE NADA, SOLAMENTE ES PARA EXPLICAR CONCEPTOS

    PARA EL USO DE LOS CUBOS DE ALAMBRE GLUT:
    -----------------------------------------
    
    Técnicamente podemos usar FreeGLUT en Python, pero no es necesario 
    ni la mejor práctica para la configuración actual (GLFW + PyOpenGL).

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
    Te recomiendo encarecidamente que no usarlas si quieres estabilidad, especialmente en Linux (en windows si):

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

    Conclusión y Solución Estándar, Método glutWireCube() (Inestable):
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
glutInit()                      # <-- Inicializar GLUT para usar cubos de alambre (figuras precargadas de GLUT o FreeGlut)

# Resto del código...