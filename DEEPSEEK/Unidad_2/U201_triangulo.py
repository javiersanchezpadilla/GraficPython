""" 
    Se requiere instalar las librerías OpenGL y GLUT para ejecutar este código.
    Puedes instalarlas usando pip:
    pip3 install PyOpenGL PyOpenGL_accelerate
   
    Explicación:

    glutInit()              Inicializa GLUT (OpenGL Utility Toolkit).
    glClearColor()          Define el color de fondo (negro en este caso).
    gluOrtho2D()            Establece un sistema de coordenadas 2D.
    glBegin(GL_TRIANGLES)   Indica que vamos a dibujar un triángulo.
    glColor3f()             Definen el color
    glVertex2f()            Define la posición de cada vértice.
    glutMainLoop()          Mantiene la ventana abierta."""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Sistema de coordenadas

def draw():
    glClear(GL_COLOR_BUFFER_BIT)  # Limpia la pantalla
    
    # Dibuja un triángulo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex2f(0.0, 1.0)      # Vértice superior
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex2f(-1.0, -1.0)    # Vértice inferior izquierdo
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex2f(1.0, -1.0)     # Vértice inferior derecho
    glEnd()
    
    glFlush()  # Renderiza

def main():
    glutInit()  # Inicializa GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Modo de visualización
    glutInitWindowSize(500, 500)  # Tamaño de la ventana
    glutCreateWindow("Triángulo OpenGL en Python")  # Título
    glutDisplayFunc(draw)  # Función de renderizado
    init()  # Configuración inicial
    glutMainLoop()  # Bucle principal

if __name__ == "__main__":
    main()