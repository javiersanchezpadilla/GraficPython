""" 
    La función ord() convierte un carácter en su código ASCII:

    ord('A')  # → 65
    ord('a')  # → 97  
    ord('1')  # → 49
    ord('!')  # → 33

    glutBitmapCharacter() necesita el código numérico del carácter, no el carácter mismo
    (por eso es que requerimos obtener su código ASCII).


"""


import glfw
from OpenGL.GL import *
# from OpenGL.GLUT import *
import numpy as np
from OpenGL import GLUT



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
    GLUT.glutInit()                  # Inicializa glut para el manejo de los textos.
    return ventana


def dibujar_texto(x, y, texto):
    # Función sencilla para dibujar texto en coordenadas 2D
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    # Configurar proyección ortográfica para texto
    ancho, alto = glfw.get_window_size(glfw.get_current_context())
    glOrtho(0, ancho, 0, alto, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Posicionar texto
    glRasterPos2f(x, y)
    
    # glutBitmapCharacter(GLUT_BITMAP_8_BY_13, s[i])
    # glutBitmapCharacter(GLUT_BITMAP_9_BY_15, s[i])
    # glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, s[i])
    # glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, s[i])
    # glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, s[i])
    # glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, s[i])
    # glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, s[i])

    # Dibujar cada carácter
    for caracter in texto:
        GLUT.glutBitmapCharacter(GLUT.GLUT_BITMAP_8_BY_13, ord(caracter))
    
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)



def principal():
    ventana = iniciar_ventana()
    # Variables para el ejemplo
    rotacion = 0.0
    contador = 0
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
 
        # Configurar vista 3D
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        GLUT.gluPerspective(45, 800/600, 0.1, 50.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        GLUT.gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    
        # Dibujar cubo giratorio
        rotacion += 1.0
        glRotatef(rotacion, 1, 1, 0)
        
        glBegin(GL_QUADS)
        # Cara frontal (roja)
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1); glVertex3f(-1, 1, 1)
        # Cara trasera (verde)
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1); glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1); glVertex3f(1, -1, -1)
        glEnd()
        
        # ¡DIBUJAR TEXTO EN PANTALLA!
        dibujar_texto(10, 580, "Hola OpenGL!")
        dibujar_texto(10, 550, f"Rotacion: {rotacion:.1f}°")
        dibujar_texto(10, 520, f"Contador: {contador}")
        dibujar_texto(10, 490, "Presiona ESC para salir")
        
        contador += 1

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    principal()