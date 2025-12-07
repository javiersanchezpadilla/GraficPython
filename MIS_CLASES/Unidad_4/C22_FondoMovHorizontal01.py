""" Código para mostrar como se puede cargar un fondo variando su punto en "x" de inicio 
    la carga de la textura la realizaremos esta vez no desde su posicion de inicio (0,0) sino desde un punto "x" que aumentaremos
    creando un efecto de desplazamiento horizontal, se realiza en el eje "x" pero se puede hacer en "y" de igual manera.
    Al llegar al final de la imagen, el punto "x" se reinicia a 0, creando un efecto de desplazamiento infinito.
    Se utilizan 4 cuadrantes para cubrir toda la pantalla, y apreciar las distintas formas en que se carga la imagen en los poligonos.

    En el último cuadrante se muestra como repetir la textura varias veces en el mismo polígono, modificando .
    las coordenadas de textura, observen el valor 3 (indica que se cargara 3 veces la misma imagen en el poligono).
    El código del último cuadrante está comentado, pueden descomentar para probarlo.

            glBegin(GL_QUADS)
            glTexCoord2f(0 + offset, 0); glVertex2f(0.0, -1.0)
            glTexCoord2f(3 + offset, 0); glVertex2f(1.0, -1.0)
            glTexCoord2f(3 + offset, 1); glVertex2f(1.0, 0.0)
            glTexCoord2f(0 + offset, 1); glVertex2f(0.0, 0.0)
            glEnd()
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

    return textura_id   


def carga_textura_en_poligonos():
        """ El truco esta no en el dibujo del poligono, sino en como se cargan las coordenadas de textura
            en cada cuadrante, variando el punto de inicio en "x" de las coordenadas de textura.
            Lo interesanto es que a medida que el offset aumenta, las coordenadas de textura se van desplazando
            y el resto de la imagen se carga al final de lo que consideramos la misma imagen.
            Poner atencion en la varible <<offset>> y como se aplica en las coordenadas de textura en cada cuadrante.
            Elegi el nombre offset porque en terminos de texturas, es el desplazamiento que se aplica a las coordenadas de textura,
            sin embargo el nombre puede ser el que ustedes quieran.
            """

        offset = 0.0        
                                    # Dibujar el los poligonos con la textura de la imagen
                                    # Cuadrante superior izquierdo
        glBegin(GL_QUADS)
        glTexCoord2f(0 + offset, 0); glVertex2f(-1.0, 0.0)
        glTexCoord2f(1 + offset, 0); glVertex2f(0.0, 0.0)
        glTexCoord2f(1 + offset, 1); glVertex2f(0.0, 1.0)
        glTexCoord2f(0 + offset, 1); glVertex2f(-1.0, 1.0)
        glEnd()
                                    # Cuadrante superior derecha
                                    # afectamos las coordenadas de textura para crear el efecto de desplazamiento
                                    # en este caso solo en el eje X de glTexCoord2f
        offset += 0.3
        glBegin(GL_QUADS)
        glTexCoord2f(0 + offset, 0); glVertex2f(0.0, 0.0)
        glTexCoord2f(1 + offset, 0); glVertex2f(1.0, 0.0)
        glTexCoord2f(1 + offset, 1); glVertex2f(1.0, 1.0)
        glTexCoord2f(0 + offset, 1); glVertex2f(0.0, 1.0)
        glEnd()
                                    # Cuadrante inferior izquierdo
        offset += 0.3
        glBegin(GL_QUADS)
        glTexCoord2f(0 + offset, 0); glVertex2f(-1.0, -1.0)
        glTexCoord2f(1 + offset, 0); glVertex2f(0.0, -1.0)
        glTexCoord2f(1 + offset, 1); glVertex2f(0.0, 0.0)
        glTexCoord2f(0 + offset, 1); glVertex2f(-1.0, 0.0)
        glEnd()
                                    # Cuadrante inferior derecho
                                    # como una prueba podemos indicar cuantas veces se repite la textura en este cuadrante
                                    # en este caso 3 veces en el eje X
        offset += 0.3
        glBegin(GL_QUADS)
        glTexCoord2f(0 + offset, 0); glVertex2f(0.0, -1.0)
        glTexCoord2f(1 + offset, 0); glVertex2f(1.0, -1.0)
        glTexCoord2f(1 + offset, 1); glVertex2f(1.0, 0.0)
        glTexCoord2f(0 + offset, 1); glVertex2f(0.0, 0.0)
        glEnd()

                                    # como una prueba podemos indicar cuantas veces se repite la textura en este cuadrante
                                    # en este caso 3 veces en el eje X, con su respectivo offset (desplazamiento)
        # glBegin(GL_QUADS)
        # glTexCoord2f(0 + offset, 0); glVertex2f(0.0, -1.0)
        # glTexCoord2f(3 + offset, 0); glVertex2f(1.0, -1.0)        # <-- aqui se indica el numero de veces a repetir la imagen
        # glTexCoord2f(3 + offset, 1); glVertex2f(1.0, 0.0)         # <-- aqui se indica el numero de veces a repetir la imagen
        # glTexCoord2f(0 + offset, 1); glVertex2f(0.0, 0.0)
        # glEnd()


                                    # Programa principal
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(800, 600, "Cargar textura desde posicion variable", None, None)
    glfw.make_context_current(ventana)
                                                                # Cargar fondo
    fondo_tex = cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/PruebaTextura.bmp")
    glEnable(GL_TEXTURE_2D)
                                                                # Programa principal
    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT)
        glBindTexture(GL_TEXTURE_2D, fondo_tex)

        carga_textura_en_poligonos()

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


main()
