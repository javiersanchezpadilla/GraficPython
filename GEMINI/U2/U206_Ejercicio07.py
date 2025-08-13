""" una escena completa con casa + sol + pasto + árbol, usando solo primitivas de OpenGL 
    (GL_TRIANGLES, GL_QUADS y GL_TRIANGLE_FAN).
    Añade un sol en la esquina superior derecha usando GL_TRIANGLE_FAN.Objetivo
    Combinar varias primitivas para crear una composición visual completa.
    Practicar posicionamiento de coordenadas y combinación de colores.
    Aprender a usar GL_TRIANGLE_FAN para círculos.

    Explicación
    Fondo celeste → simula el cielo.
    Pasto → un gran GL_QUADS en la parte inferior.
    Casa → misma estructura del reto anterior.
    Árbol → tronco (GL_QUADS) + copa (GL_TRIANGLE_FAN).
    Sol → GL_TRIANGLE_FAN amarillo.

    La función dibujar_circulo() permite crear círculos de cualquier color y posición.

    Posibles mejoras para tu práctica
    Añadir nubes usando círculos blancos.
    Cambiar la posición del sol y hacerlo más grande o pequeño.
    Usar varios árboles con tamaños diferentes para simular profundidad.
    """

import glfw
from OpenGL.GL import *
import math

def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")

    ventana = glfw.create_window(800, 600, "Escena 2D con OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")

    glfw.make_context_current(ventana)
    return ventana

# Función para dibujar un círculo usando GL_TRIANGLE_FAN
def dibujar_circulo(x, y, radio, r, g, b, segmentos=50):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r, g, b)
    glVertex2f(x, y)  # Centro
    for i in range(segmentos + 1):
        angulo = 2 * math.pi * i / segmentos
        glVertex2f(x + math.cos(angulo) * radio, y + math.sin(angulo) * radio)
    glEnd()

ventana = iniciar_ventana()

while not glfw.window_should_close(ventana):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.8, 0.9, 1.0, 1)  # Fondo celeste

    # 🌿 Pasto
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.7, 0.3)
    glVertex2f(-1.0, -0.5)
    glVertex2f(1.0, -0.5)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

    # 🏠 Pared de la casa
    glBegin(GL_QUADS)
    glColor3f(0.9, 0.7, 0.5)
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.0)
    glVertex2f(-0.4, 0.0)
    glEnd()

    # 🏠 Techo
    glBegin(GL_TRIANGLES)
    glColor3f(0.7, 0.2, 0.2)
    glVertex2f(-0.45, 0.0)
    glVertex2f(0.45, 0.0)
    glVertex2f(0.0, 0.4)
    glEnd()

    # 🚪 Puerta
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.3, 0.1)
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.2)
    glVertex2f(-0.1, -0.2)
    glEnd()

    # 🪟 Ventana izquierda
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.8, 1.0)
    glVertex2f(-0.35, -0.1)
    glVertex2f(-0.15, -0.1)
    glVertex2f(-0.15, 0.1)
    glVertex2f(-0.35, 0.1)
    glEnd()

    # 🪟 Ventana derecha
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.8, 1.0)
    glVertex2f(0.15, -0.1)
    glVertex2f(0.35, -0.1)
    glVertex2f(0.35, 0.1)
    glVertex2f(0.15, 0.1)
    glEnd()

    # 🌳 Tronco del árbol
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.1)
    glVertex2f(0.65, -0.5)
    glVertex2f(0.75, -0.5)
    glVertex2f(0.75, -0.2)
    glVertex2f(0.65, -0.2)
    glEnd()

    # 🌳 Copa del árbol (círculo)
    dibujar_circulo(0.7, 0.0, 0.25, 0.0, 0.6, 0.0)

    # ☀ Sol (círculo amarillo)
    dibujar_circulo(0.75, 0.75, 0.15, 1.0, 1.0, 0.0)

    glfw.swap_buffers(ventana)
    glfw.poll_events()

glfw.terminate()

