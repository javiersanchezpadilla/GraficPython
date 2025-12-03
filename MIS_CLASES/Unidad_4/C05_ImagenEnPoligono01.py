""" En este ejemplo cargarmos una imagen como textura en un poligono"""


import glfw
from OpenGL.GL import *
from PIL import Image
import time


                                                # Función para cargar textura
def cargar_textura(ruta):
    imagen = Image.open(ruta).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = imagen.convert("RGBA").tobytes()
    width, height = imagen.size

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return tex_id


                                                # Programa principal GLFW
def main():
    
    if not glfw.init():                         # Inicializar GLFW
        return

    ventana = glfw.create_window(800, 600, "Cargar una imagen en un poligono", None, None)
    glfw.make_context_current(ventana)

    ruta = "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PruebaTextura.bmp"
    imagen_de_textura = cargar_textura(ruta)

    # Configurar OpenGL
    glEnable(GL_TEXTURE_2D)

                                                # Ciclo de glfw
    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT)

          # Dibujar un rectangulo vacio
        glBegin(GL_QUADS)
        glVertex2f(-0.7, -0.3)
        glVertex2f(-0.1, -0.3)
        glVertex2f(-0.1,  0.3)
        glVertex2f(-0.7,  0.3)
        glEnd()

        # Seleccionar textura actual
        glBindTexture(GL_TEXTURE_2D, imagen_de_textura)

        # Dibujar el poligono con la textura de la imagen
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f( 0.1, -0.3)
        glTexCoord2f(1, 0); glVertex2f( 0.7, -0.3)
        glTexCoord2f(1, 1); glVertex2f( 0.7,  0.3)
        glTexCoord2f(0, 1); glVertex2f( 0.1,  0.3)
        glEnd()


        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()


main()
