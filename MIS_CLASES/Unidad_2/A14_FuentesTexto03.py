""" IMPRESION DE TEXTO EN PANTALLA.

    FONTS DISPONIBLES:
    ------------------
    glutBitmapCharacter( Font, ASCII)

    GLUT_BITMAP_8_BY_13
    GLUT_BITMAP_9_BY_15
    GLUT_BITMAP_TIMES_ROMAN_10
    GLUT_BITMAP_TIMES_ROMAN_24
    GLUT_BITMAP_HELVETICA_10
    GLUT_BITMAP_HELVETICA_12
    GLUT_BITMAP_HELVETICA_18

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
from OpenGL.GLU import *
from OpenGL.GLUT import *



def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "Mi primera ventana como funcion en OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    GLUT.glutInit()                  # Inicializa glut para el manejo de los textos.
    return ventana


def dibujar_texto(pos_x, pos_y, numero_font, texto):
    # Función sencilla para dibujar texto en coordenadas 2D

    fonts = ["GLUT_BITMAP_8_BY_13", "GLUT_BITMAP_9_BY_15", "GLUT_BITMAP_TIMES_ROMAN_10",
             "GLUT_BITMAP_TIMES_ROMAN_24", "GLUT_BITMAP_HELVETICA_10", "GLUT_BITMAP_HELVETICA_12",
             "GLUT_BITMAP_HELVETICA_18"]

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
    glRasterPos2f(pos_x, pos_y)
    
    # Dibujar cada carácter
    for caracter in texto:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, ord(caracter))
    
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
        gluPerspective(45, 800/600, 0.1, 50.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    
        
        # ¡DIBUJAR TEXTO EN PANTALLA!
        dibujar_texto(10, 580, 0, "Hola OpenGL!")
        dibujar_texto(10, 550, 1, "Rotacion: ")
        dibujar_texto(10, 520, 2, "Contador:")
        dibujar_texto(10, 490, 3, "Presiona ESC para salir")
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    principal()