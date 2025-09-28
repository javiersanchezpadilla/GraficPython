""" Programa que dibuja una linea en OpenGL version 8
    Esta es la version mas estructurada del programa, donde todo el codigo esta en clases.
    En este ejemplo se dibuja las lineas mediante el uso de clases, creando una cuadrícula de lineas grises cada 10 unidades
    y los ejes X y Y en color blanco.
    Lo importante en este ejemplo es que se muestra como organizar el código en clases.
"""

import glfw
from OpenGL.GL import *


class Ventana:
    def __init__(self, ancho, alto, titulo):
        if not glfw.init():
            raise Exception("No se pudo iniciar GLFW")
        self.ventana = glfw.create_window(ancho, alto, titulo, None, None)
        if not self.ventana:
            glfw.terminate()
            raise Exception("No se pudo crear la ventana")
        glfw.make_context_current(self.ventana)

    def should_close(self):
        return glfw.window_should_close(self.ventana)

    def swap_buffers(self):
        glfw.swap_buffers(self.ventana)

    def poll_events(self):
        glfw.poll_events()

    def terminate(self):
        glfw.terminate()


class Proyeccion:
    @staticmethod
    def configurar():
        """ Esta función configura la matriz de proyección para definir el espacio de coordenadas
            que vamos a utilizar para dibujar en la ventana.
            No retorna ningún valor, solo configura el estado de OpenGL.
            La función establece un sistema de coordenadas 2D donde el origen (0,0) está en la esquina
            inferior izquierda, el eje X va de 0 a 200 y el eje Y va de 0 a 150.
            Esto significa que cualquier cosa que dibujemos usando estas coordenadas se ajustará a este
            rango dentro de la ventana.
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, 200.0, 0.0, 150.0, -1.0, 1.0) 
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


class Linea:
    def __init__(self, x1, y1, x2, y2, rojo, verde, azul):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.rojo = rojo
        self.verde = verde
        self.azul = azul

    def dibujar(self):
        glColor3f(self.rojo, self.verde, self.azul)  # Fija el color para dibujar
        glBegin(GL_LINES)
        glVertex2i(self.x1, self.y1)
        glVertex2i(self.x2, self.y2)
        glEnd()

    def DibujaCuadricula(self):
        for x in range(0, 201, 10):
            linea_vertical = Linea(x, 0, x, 150, 0.3, 0.3, 0.3)
            linea_vertical.dibujar()

        for y in range(0, 151, 10):
            linea_horizontal = Linea(0, y, 200, y, 0.3, 0.3, 0.3)
            linea_horizontal.dibujar()

    def dibujar_ejes(self):
        eje_x = Linea(0, 75, 200, 75, 1.0, 1.0, 1.0)
        eje_y = Linea(100, 0, 100, 150, 1.0, 1.0, 1.0)
        eje_x.dibujar()
        eje_y.dibujar()


if __name__ == "__main__":
    mi_ventana = Ventana(800, 600, "Mi primera ventana como clase en OpenGL")
    Proyeccion.configurar()
    while not mi_ventana.should_close():
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        linea = Linea(0, 0, 200, 150, 1.0, 1.0, 0.0)  # Fija color amarillo
        linea.DibujaCuadricula()
        linea.dibujar_ejes()
        mi_ventana.swap_buffers()
        mi_ventana.poll_events()
    mi_ventana.terminate()

