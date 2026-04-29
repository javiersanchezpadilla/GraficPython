""" GENRERAR TEXTOS (DEFINITIVO FINAL FINAL)

    Podemos generar textos en OpenGL usando glfw como gestor de ventanas
    y pygame para el manejo del texto

    usaremos Pygame como una 'fábrica de imágenes'. Pygame tomará tu texto y 
    lo convertirá en una imagen (Surface), la cual luego 'pegaremos' en un 
    cuadrado dentro de la ventana de GLFW usando texturas de OpenGL.

    Puntos clave del proceso
    ------------------------
    ¿Por qué pygame.image.tobytes?: OpenGL no sabe qué es un objeto de Pygame. 
    Necesita que le pasemos la información como una lista gigante de números 
    (bytes) que representan los colores de cada píxel.

    Mezcla (Blending): Al dibujar texto, es vital usar glEnable(GL_BLEND). 
    Sin esto, las letras se verían dentro de una caja negra sólida en lugar de 
    tener un fondo transparente.

    Rendimiento: Nota que la función crear_textura_texto se llama antes del 
    bucle while. Crear texturas es un proceso lento para la computadora; si 
    lo haces dentro del bucle 60 veces por segundo, tu programa irá muy lento.

    Variedad de opciones
    --------------------
    Para que el texto no sea siempre igual, puedes jugar con estos valores:
    Fuentes: Puedes usar 'Times New Roman', 'Courier' o incluso cargar un 
    archivo .ttf específico usando 
        pygame.font.Font('ruta/archivo.ttf', tamaño).

    Colores: En la línea fuente.render(mensaje, True, (255, 255, 255)), puedes 
    cambiar los números RGB para obtener letras rojas (255, 0, 0), verdes, etc.

"""

import glfw
from OpenGL.GL import *
import pygame

def crear_textura_texto(mensaje, fuente_sistema, tamaño):
    """
    Usa Pygame para convertir texto en una textura que OpenGL pueda entender.
    """
    # 1. Configurar la fuente en Pygame
    pygame.font.init()
    fuente = pygame.font.SysFont(fuente_sistema, tamaño)
    
    # 2. Renderizar el texto a una superficie (imagen)
    # El color es Blanco (255, 255, 255) y fondo transparente
    superficie = fuente.render(mensaje, True, (255, 255, 255))
    
    # 3. Convertir la superficie de Pygame a datos de bytes
    ancho, alto = superficie.get_size()
    datos_imagen = pygame.image.tobytes(superficie, "RGBA", True)

    # 4. Crear la textura en OpenGL
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ancho, alto, 0, GL_RGBA, GL_UNSIGNED_BYTE, datos_imagen)
    
    # Filtros para que el texto no se vea borroso
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    return tex_id, ancho, alto



def dibujar_cuadrado_texto(x, y, ancho, alto, tex_id):
    """Dibuja un rectángulo en la pantalla con la textura del texto."""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    
    # Habilitar transparencia para que el fondo del texto no tape lo de atrás
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glBegin(GL_QUADS)
    # Mapeamos la textura al cuadrado (coordenadas 0 a 1)
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

    ventana = glfw.create_window(800, 600, "Texto con GLFW y Pygame", None, None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    
    # --- PREPARACIÓN DEL TEXTO ---
    # Creamos la textura una sola vez fuera del bucle para no saturar la memoria
    id_texto, w, h = crear_textura_texto("¡Hola, esto es OpenGL!", "Arial", 50)
    
    # Escalar el tamaño para que se vea bien en coordenadas de OpenGL (-1 a 1)
    escala_w = w / 400 
    escala_h = h / 400

    while not glfw.window_should_close(ventana):
        glClearColor(0.1, 0.1, 0.1, 1.0) # Fondo gris oscuro
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar el texto en el centro (aproximadamente)
        dibujar_cuadrado_texto(-0.5, 0, escala_w, escala_h, id_texto)

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
