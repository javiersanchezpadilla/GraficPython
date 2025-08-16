""" El Árbol Fractal Binario
    Imagina que empiezas con un solo tronco. A medida que avanzas, este tronco se divide en dos ramas más pequeñas, 
    cada una con un ángulo diferente. Luego, cada una de esas dos ramas se vuelve a dividir en otras dos, y así 
    sucesivamente. Al igual que el brócoli, cada rama pequeña se parece al árbol entero, pero en miniatura.

    El código para generar este fractal es muy similar al del Triángulo de Sierpinski, pero en lugar de triángulos, 
    trabajamos con líneas. Usaremos las transformaciones de rotación y traslación que ya aprendimos.
    
    glLoadIdentity() simplemente reemplaza la matriz de transformación actual por una matriz "limpia" o "por defecto", 
    que no hace nada. De esta forma, cada fotograma empieza con una hoja en blanco, y las transformaciones que apliques 
    solo durarán hasta que se dibuje el siguiente fotograma.

    """

import pygame
from pygame.locals import *
from OpenGL.GL import *

def dibujar_linea(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# Función recursiva para dibujar el árbol
def dibujar_arbol(nivel, longitud, angulo):
    # Condición de salida (caso base)
    if nivel == 0:
        return

    # Dibuja la rama actual
    dibujar_linea(0, 0, 0, longitud)

    # Guarda la matriz actual (para que las ramas no se afecten entre sí)
    glPushMatrix()
    
    # Rotación para la rama derecha
    glRotatef(angulo, 0, 0, 1)
    # Trasladar al final de la rama actual
    glTranslatef(0, longitud, 0)
    # Dibujar la rama derecha más pequeña
    dibujar_arbol(nivel - 1, longitud * 0.7, angulo)
    
    # Restaura la matriz
    glPopMatrix()
    
    # Guarda de nuevo la matriz
    glPushMatrix()
    
    # Rotación para la rama izquierda
    glRotatef(-angulo, 0, 0, 1)
    # Trasladar al final de la rama actual
    glTranslatef(0, longitud, 0)
    # Dibujar la rama izquierda más pequeña
    dibujar_arbol(nivel - 1, longitud * 0.7, angulo)
    
    # Restaura la matriz
    glPopMatrix()


def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    nivel_detalle = 10
    longitud_inicial = 0.5
    angulo_rotacion = 30.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        
        # Reinicia las transformaciones en cada fotograma
        glLoadIdentity()
        
        # Trasladamos el árbol hacia abajo para que se vea completo
        glTranslatef(0.0, -0.7, 0.0) # He ajustado el valor para que se vea mejor
        
        # Llamamos a la función para dibujar el árbol
        dibujar_arbol(nivel_detalle, longitud_inicial, angulo_rotacion)
        
        pygame.display.flip()

main()