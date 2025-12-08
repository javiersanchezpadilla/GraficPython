""" Código para crear un fondo que se desplaza horizontalmente de manera infinita.
    Se declararon algunas variables de mas, por si requieren hacer modificaciones al código
    y requieren el uso de esas variables o propiedades.

"""

import glfw
from OpenGL.GL import *
from PIL import Image
import time


                                                                # Cargar textura
def cargar_textura(ruta):
    imagen = Image.open(ruta).transpose(Image.FLIP_TOP_BOTTOM)
    datos_imagen = imagen.convert("RGBA").tobytes()
    ancho_imagen, alto_imagen = imagen.size

    textura_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_id)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ancho_imagen, alto_imagen, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, datos_imagen)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return textura_id, ancho_imagen, alto_imagen                                



                                                                # Programa principal
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(800, 600, "Scroll Horizontal de pantalla de fondo", None, None)
    glfw.make_context_current(ventana)

    # Cargar fondo
    # la variable fondo_text es el ID de la textura
    # fondo_ancho y fondo_alto son el ancho y alto de la imagen, extraidos de la imagen cargada
    fondo_tex, fondo_ancho, fondo_alto = cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/FondoSprite02.jpg")
    # fondo_tex = cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/PruebaTextura.bmp")  # Probar con esta textura

    glEnable(GL_TEXTURE_2D)

    # Offset horizontal del fondo
    offset = 0.0
    velocidad = 0.002  # velocidad del scroll

    # Loop principal
    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT)

        glBindTexture(GL_TEXTURE_2D, fondo_tex)

        # Mover textura, el termino 'offset' se aplica a las coordenadas de textura
        offset += velocidad

        # Reiniciar cuando llegue al final (para hacerlo infinito)
        if offset >= 1:
            offset = 0

        # Dibujar fondo con offset aplicado
        glBegin(GL_QUADS)
        glTexCoord2f(offset, 0);         glVertex2f(-1, -1)
        glTexCoord2f(1 + offset, 0);     glVertex2f( 1, -1)
        glTexCoord2f(1 + offset, 1);     glVertex2f( 1,  1)
        glTexCoord2f(offset, 1);         glVertex2f(-1,  1)
        glEnd()

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()


main()
