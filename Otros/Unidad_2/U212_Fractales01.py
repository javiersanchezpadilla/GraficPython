""" El Triángulo de Sierpinski: 
    El Triángulo de Sierpinski se construye a partir de un triángulo grande, que llamamos el "triángulo padre". 
    Para crear la siguiente generación de la figura, hacemos lo siguiente:

    A) Dibuja un triángulo "hijo" en el centro del triángulo padre. Este triángulo hijo es una versión más pequeña 
       del padre, pero está invertido.
    B) Repite el proceso en cada uno de los tres triángulos más pequeños que quedan en las esquinas del triángulo padre.
    C) Sigue repitiendo este proceso de forma recursiva hasta que hayas alcanzado el nivel de detalle que desees.

    La clave aquí es la recursividad, que es cuando una función se llama a sí misma. Es como si le dieras a tu ordenador 
    la instrucción: "Dibuja un triángulo, y luego, para cada una de las tres esquinas, 
    ¡vuelve a ejecutar esta misma instrucción!".

    
    A diferencia de las curvas de Bézier, que se basan en una fórmula matemática directa, el Triángulo de Sierpinski se 
    genera con una regla de construcción muy sencilla que se repite una y otra vez.

    La "fórmula" de un fractal como este es un conjunto de instrucciones que definen cómo se construye. 
    
    Aquí está la regla paso a paso:

    Comenzar: Empieza con un solo triángulo grande.
    Dividir: Encuentra el punto medio de cada uno de los tres lados de ese triángulo.
    Eliminar: Conecta esos tres puntos medios. Esto formará un nuevo triángulo invertido en el centro. Este triángulo 
    central es el que "eliminamos" (o, en nuestro código, el que no dibujamos).
    Repetir: Nos quedamos con tres triángulos más pequeños en las esquinas. Repite los pasos 1, 2 y 3 para cada uno de 
    estos tres nuevos triángulos.
    Esta regla de "dividir y eliminar" se repite un número determinado de veces (lo que llamamos "nivel de detalle" en 
    nuestro código). Cuantas más veces se repite, más detallado y complejo se vuelve el fractal.
    El código implementa esta fórmula de forma recursiva. 
    La función triangulo_sierpinski() se encarga de "dividir" el triángulo y luego se llama a sí misma para cada uno de 
    los tres triángulos más pequeños, "repitiendo" así el proceso.
            """

import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# La función que dibuja el triángulo
def dibujar_triangulo(puntos):
    glBegin(GL_TRIANGLES)
    for punto in puntos:
        glVertex2f(punto[0], punto[1])
    glEnd()

# La función recursiva para crear el fractal
def triangulo_sierpinski(puntos, nivel):
    # Si el nivel es 0, simplemente dibujamos el triángulo
    if nivel == 0:                      # Este es el caso base de la recursión
        dibujar_triangulo(puntos)
        return

    # Calculamos los puntos medios de los lados del triángulo
    puntos_medios = [
        [(puntos[0][0] + puntos[1][0]) / 2, (puntos[0][1] + puntos[1][1]) / 2],
        [(puntos[1][0] + puntos[2][0]) / 2, (puntos[1][1] + puntos[2][1]) / 2],
        [(puntos[2][0] + puntos[0][0]) / 2, (puntos[2][1] + puntos[0][1]) / 2]
    ]

    # Llamamos a la función de nuevo para los 3 triángulos más pequeños
    # de los "rincones"
    triangulo_sierpinski([puntos[0], puntos_medios[0], puntos_medios[2]], nivel - 1)
    triangulo_sierpinski([puntos_medios[0], puntos[1], puntos_medios[1]], nivel - 1)
    triangulo_sierpinski([puntos_medios[2], puntos_medios[1], puntos[2]], nivel - 1)

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0) # Fondo negro

    # Puntos del triángulo inicial
    puntos_iniciales = [
        [0.0, 0.8],
        [-0.8, -0.8],
        [0.8, -0.8]
    ]

    # Número de niveles de detalle (mientras más alto, más detalle)
    nivel_de_detalle = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 0.0) # Color de los triángulos (amarillo)
        triangulo_sierpinski(puntos_iniciales, nivel_de_detalle)
        pygame.display.flip()

main()