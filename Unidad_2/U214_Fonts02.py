""" Mostrando una cadena de texto
    Para dibujar una palabra, como "HOLA", no tienes que escribir el mismo código una y otra vez. 
    En cambio, usaremos un bucle y una función para automatizar el proceso. La idea es simple:

    1) Recorrer cada letra de la palabra que queremos dibujar.
    2) Para cada letra, calcular sus coordenadas en el atlas de texturas (la "H", la "O", la "L", etc.).
    3) Dibujar el cuadrado con la textura correspondiente en la posición correcta de la pantalla.
    4) Moverse un poco hacia la derecha para la siguiente letra.

    Ejemplo de código que combina todos estos pasos. He creado un diccionario que guarda las coordenadas del 
    atlas para cada letra y una función que se encarga de todo el proceso."""

import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# Creamos un diccionario para guardar las coordenadas de cada letra en el atlas
# La clave es la letra, el valor es la coordenada (u, v) en el atlas 4x4
coordenadas_atlas = {
    'A': (0.0, 0.75), 'B': (0.25, 0.75), 'C': (0.5, 0.75), 'D': (0.75, 0.75),
    'E': (0.0, 0.5),  'F': (0.25, 0.5),  'G': (0.5, 0.5),  'H': (0.75, 0.5),
    'I': (0.0, 0.25), 'J': (0.25, 0.25), 'K': (0.5, 0.25), 'L': (0.75, 0.25),
    'M': (0.0, 0.0),  'N': (0.25, 0.0),  'O': (0.5, 0.0),  'P': (0.75, 0.0)
}

# La textura debe estar cargada antes de usar esta función
def dibujar_cadena(texto, x_inicio, y_inicio, tamano):
    # Usaremos esta variable para saber dónde dibujar la siguiente letra
    x_posicion = x_inicio
    
    # Recorremos cada letra de la palabra
    for letra in texto:
        # Buscamos las coordenadas de la letra en nuestro diccionario
        if letra in coordenadas_atlas:
            u, v = coordenadas_atlas[letra]

            # Definimos las coordenadas de la textura para la letra
            tex_coords = np.array([
                (u, v),
                (u + 0.25, v),
                (u + 0.25, v + 0.25),
                (u, v + 0.25)
            ], 'f')

            # Definimos los vértices del cuadrado en la pantalla
            quad_vertices = np.array([
                (x_posicion, y_inicio),
                (x_posicion + tamano, y_inicio),
                (x_posicion + tamano, y_inicio + tamano),
                (x_posicion, y_inicio + tamano)
            ], 'f')

            # Dibujamos el cuadrado con la textura
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_TEXTURE_COORD_ARRAY)
            
            glTexCoordPointer(2, GL_FLOAT, 0, tex_coords)
            glVertexPointer(2, GL_FLOAT, 0, quad_vertices)
            glDrawArrays(GL_QUADS, 0, 4)
            
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_TEXTURE_COORD_ARRAY)

            # Nos movemos a la derecha para la siguiente letra
            x_posicion += tamano

# --- Y en el bucle principal lo usaríamos así: ---
# Aquí solo llamamos a la función
# dibujar_cadena("HOLA", -0.5, 0.0, 0.2)
