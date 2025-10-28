""" En este ejercicio se dibujaran dos cuadros que se moveran horizontalmente en direcciones opuestas.
    Cuando los cuadros colisionen entre si, rebotaran y cambiaran de direccion.
    Cada cuadro estara formado por cuatro vertices y tendra un color diferente.
    La diferencia en este código es que se implementa el concepto de Programación Orientada a Objetos (OOP).
    Se define una clase `Cuadro` que encapsula los atributos y métodos relacionados con cada cuadro.
    Esto hace que el código sea más modular, reutilizable y fácil de entender.
"""

import glfw
from OpenGL.GL import *

class Cuadro:
    def __init__(self, pos_x, velocidad, tamanio, color):
        self.pos_x = pos_x
        self.velocidad = velocidad
        self.tamanio = tamanio
        self.color = color  # Definimos la tupla para el color RGB (r, g, b)

    def dibujar(self):
        glBegin(GL_QUADS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        
        x = self.pos_x
        tam = self.tamanio
        
        glVertex2f(x, tam)
        glVertex2f(x + tam, tam)
        glVertex2f(x + tam, -tam)
        glVertex2f(x, -tam)
        glEnd()

    def actualizar(self):
        self.pos_x += self.velocidad
        
        # Rebotar en los bordes de la pantalla
        if self.pos_x + self.tamanio >= 1.0 or self.pos_x <= -1.0:
            self.velocidad *= -1

    def detectar_colision(self, otro_cuadro):
        # La colisión ocurre si los rectángulos se superponen
        x1_a = self.pos_x
        x1_b = self.pos_x + self.tamanio
        x2_a = otro_cuadro.pos_x
        x2_b = otro_cuadro.pos_x + otro_cuadro.tamanio
        
        # Condición de superposición en el eje X
        return (x1_a < x2_b and x1_b > x2_a)


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600, "OOP: Dos cuadros rebotando", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


def programa_principal():
    ventana = iniciar_ventana()
    
    # Creamos las instancias de la clase Cuadro
    cuadro1 = Cuadro(pos_x=-0.9, velocidad=0.007, tamanio=0.2, color=(1.0, 0.0, 0.0))
    cuadro2 = Cuadro(pos_x=0.7, velocidad=-0.005, tamanio=0.2, color=(0.0, 0.0, 1.0))
    
    while not glfw.window_should_close(ventana):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Actualizar y dibujar cada cuadro
        cuadro1.actualizar()
        cuadro2.actualizar()
        
        # Detección de colisión y rebote
        if cuadro1.detectar_colision(cuadro2):
            cuadro1.velocidad *= -1
            cuadro2.velocidad *= -1

        cuadro1.dibujar()
        cuadro2.dibujar()
        
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    programa_principal()
