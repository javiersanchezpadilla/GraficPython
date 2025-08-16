""" Dibujando curvas: Curvas de Bézier
    Imagina que quieres dibujar una curva suave, como un camino sinuoso en un mapa. Si usaras solo 
    puntos, tendrías que poner muchísimos, y no quedaría muy bien. Las curvas de Bézier nos dan 
    una forma mucho más inteligente de hacerlo.

    n lugar de definir todos los puntos de la curva, solo le dices a OpenGL unos pocos puntos clave, 
    llamados puntos de control.

    Puntos de inicio y fin: Son los dos extremos de la curva.

    Puntos de control: Estos puntos no están en la curva, pero actúan como "imanes" que la atraen y le 
    dan su forma.

    Piensa en los puntos de control como si fueran cuerdas atadas a la línea. Al mover las cuerdas, la línea 
    se dobla y cambia de forma. Con solo dos o tres puntos de control, podemos crear una curva muy suave y precisa.

    En OpenGL, dibujar una curva de Bézier implica varios pasos:

    1) Definir los puntos de control: Usamos una función especial para decirle a OpenGL dónde están estos puntos.
    2) Generar la curva: OpenGL "calcula" la forma de la curva a partir de esos puntos de control.
    3) Dibujar la curva: Finalmente, le decimos a OpenGL que dibuje la línea que ha calculado.
    
    Dibujando la curva de Bézier manualmente
    La fórmula para un punto en una curva de Bézier de 4 puntos de control (P0, P1, P2, P3) es una combinación de 
    esos puntos. No te preocupes por la fórmula matemática compleja, es más fácil de entender con código. 
    La idea es que, a medida que un valor t (que va de 0 a 1) avanza, el punto se mueve suavemente entre los 
    puntos de control.

    EN ESTA VERSION SE USA NUMPY PARA DEFINIR LOS PUNTOS DE CONTROL, PERO NO ES NECESARIO
    """

import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

def dibujar_curva_bezier_manual():
    # Definimos los 4 puntos de control (x, y)
    # puntos_de_control = [
    #     [-0.75, -0.75],
    #     [-0.25,  0.75],
    #     [ 0.25,  0.75],
    #     [ 0.75, -0.75]
    # ]

    puntos_de_control = [
        [-0.75, -0.75],
        [-0.25,  0.75],
        [ 0.25,  -0.75],
        [ 0.75, 0.75]
    ]


    # Convertimos la lista de puntos a un array de NumPy.
    puntos_np = np.array(puntos_de_control, 'f')

    glColor3f(1.0, 1.0, 1.0) # Color de la curva
    glBegin(GL_LINE_STRIP) # Dibujamos una serie de líneas conectadas

    # El bucle va de 0 a 100, para generar 101 puntos en la curva
    for i in range(101):
        t = float(i) / 100.0 # 't' va de 0.0 a 1.0
        
        # Fórmula de la curva de Bézier (lo más importante)
        # La fórmula combina los 4 puntos de control usando 't'
        punto_x = (1-t)**3 * puntos_np[0][0] + 3*(1-t)**2*t * puntos_np[1][0] + 3*(1-t)*t**2 * puntos_np[2][0] + t**3 * puntos_np[3][0]
        punto_y = (1-t)**3 * puntos_np[0][1] + 3*(1-t)**2*t * puntos_np[1][1] + 3*(1-t)*t**2 * puntos_np[2][1] + t**3 * puntos_np[3][1]
        
        glVertex2f(punto_x, punto_y)

    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        dibujar_curva_bezier_manual()
        pygame.display.flip()

main()