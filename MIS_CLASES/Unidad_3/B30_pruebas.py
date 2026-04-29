import glfw
from OpenGL.GL import *
import pygame

def crear_textura_texto(mensaje, fuente_sistema, tamaño, color_rgb=(255, 255, 255)):
    """
    Usa Pygame para convertir texto en una textura que OpenGL pueda entender.
    """
    # 1. Configurar la fuente en Pygame
    pygame.font.init()
    fuente = pygame.font.SysFont(fuente_sistema, tamaño)
    
    # 2. Renderizar el texto a una superficie (imagen)
    # El color es personalizable y el fondo es transparente
    superficie = fuente.render(mensaje, True, color_rgb)
    
    # 3. Convertir la superficie de Pygame a datos de bytes
    ancho, alto = superficie.get_size()
    datos_imagen = pygame.image.tobytes(superficie, "RGBA", True)

    # 4. Crear la textura en OpenGL
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ancho, alto, 0, GL_RGBA, GL_UNSIGNED_BYTE, datos_imagen)
    
    # Filtros para que el texto se vea nítido
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2f, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    return tex_id, ancho, alto

def dibujar_cuadrado_texto(x, y, ancho, alto, tex_id):
    """Dibuja un rectángulo en la pantalla con la textura del texto."""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    
    # Habilitar transparencia (Blending) para evitar cuadros negros
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glBegin(GL_QUADS)
    # Coordenadas de textura (UV) y coordenadas de vértices (XY)
    glTexCoord2f(0, 0); glVertex2f(x, y)
    glTexCoord2f(1, 0); glVertex2f(x + ancho, y)
    glTexCoord2f(1, 1); glVertex2f(x + ancho, y + alto)
    glTexCoord2f(0, 1); glVertex2f(x, y + alto)
    glEnd()

    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)

def main():
    if not glfw.init():
        return

    ancho_ventana, alto_ventana = 800, 600
    ventana = glfw.create_window(ancho_ventana, alto_ventana, "Texto con GLFW y Pygame", None, None)
    
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    
    # --- PREPARACIÓN DEL TEXTO ---
    # Creamos la textura una vez (Color amarillo: 255, 255, 0)
    id_texto, w, h = crear_textura_texto("¡Texto renderizado con Pygame!", "Arial", 48, (255, 255, 0))
    
    # Ajuste de escala proporcional para coordenadas de OpenGL (-1 a 1)
    # Dividimos por el tamaño de la ventana para normalizar
    escala_w = (w / ancho_ventana) * 2
    escala_h = (h / alto_ventana) * 2

    while not glfw.window_should_close(ventana):
        # Color de fondo gris oscuro
        glClearColor(0.15, 0.15, 0.15, 1.0) 
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar el texto centrado horizontalmente
        # (x = -escala_w/2 para centrar el bloque de texto)
        dibujar_cuadrado_texto(-escala_w / 2, 0, escala_w, escala_h, id_texto)

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    # Limpieza de recursos
    glDeleteTextures(1, [id_texto])
    glfw.terminate()

if __name__ == "__main__":
    main()
    