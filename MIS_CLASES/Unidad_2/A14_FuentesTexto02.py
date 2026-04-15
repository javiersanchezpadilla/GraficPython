""" TEXTO MEDIANTE PYGAME

    
"""
import glfw
from OpenGL.GL import *
import pygame # Usaremos Pygame solo para generar la imagen del texto

class TextoRenderer:
    def __init__(self, mensaje, tamaño=50):
        pygame.font.init()
        # 1. Crear la fuente y el texto en Pygame
        fuente = pygame.font.SysFont("Arial", tamaño)
        # Dibujamos el texto en una superficie (imagen) de Pygame
        superficie_texto = fuente.render(mensaje, True, (255, 255, 255, 255), (0, 0, 0, 0))
        
        # 2. Convertir la imagen de Pygame a datos que OpenGL entienda
        datos_texto = pygame.image.tostring(superficie_texto, "RGBA", True)
        ancho, alto = superficie_texto.get_size()

        # 3. Crear una textura de OpenGL
        self.textura_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.textura_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ancho, alto, 0, GL_RGBA, GL_UNSIGNED_BYTE, datos_texto)
        
        # Configuración para que no se vea borroso
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        """Dibuja un cuadrado con la textura del texto"""
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.textura_id)
        
        # Habilitar transparencia (importante para texto)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Dibujamos un cuadrado simple donde se pegará el texto
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(-0.5, -0.2)
        glTexCoord2f(1, 0); glVertex2f(0.5, -0.2)
        glTexCoord2f(1, 1); glVertex2f(0.5, 0.2)
        glTexCoord2f(0, 1); glVertex2f(-0.5, 0.2)
        glEnd()
        
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)

def main():
    if not glfw.init(): return

    ventana = glfw.create_window(800, 600, "Texto con Pygame + GLFW", None, None)
    glfw.make_context_current(ventana)

    # Creamos nuestro objeto de texto
    mi_texto = TextoRenderer("¡Hola desde OpenGL!", 64)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Dibujamos el texto
        mi_texto.dibujar()

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()

