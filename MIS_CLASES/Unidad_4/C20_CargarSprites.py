""" Aqui vamos a cargar varias imagenes (sprites)

    Este es un truco muy elegante para controlar los elementos del arreglo o lista de sprites

                frame = (frame + 1) % len(sprites)

    Por ejemplo si tengo 8 elementos en mi lista, mi indice es del 0 al 7
                rutas = [
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajA.png",      <-- Elemento 1 indice 0
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajB.png",      <-- Elemento 2 indice 1
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajC.png",      <-- Elemento 3 indice 2
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajD.png",      <-- Elemento 4 indice 3
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajE.png",      <-- Elemento 5 indice 4
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajF.png",      <-- Elemento 6 indice 5
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajG.png",      <-- Elemento 7 indice 6
                "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajH.png"       <-- Elemento 8 indice 7
                ]

                sprites = [cargar_textura(r) for r in rutas]        <-- Carga las 8 imagenes en la lista sprites

                
    Entonces si yo quiero ciclar entre los 8 elementos que por referencia al indice debe ciclar entre el 0 y el 7

                La línea frame = (frame + 1) % len(sprites)         len(sprites) = 8
    
                frame = (frame + 1) % len(sprites) = (0+1) & 8

                cuando frame es        modulo es                cuando frame es        modulo es
                    0                   0 % 8 = 0                   5                   5 % 8 = 5
                    1                   1 % 8 = 1                   6                   6 % 8 = 6
                    2                   2 % 8 = 2                   7                   7 % 8 = 7
                    3                   3 % 8 = 3                   8                   8 % 8 = 0
                    4                   4 % 8 = 4                   0                   0 % 8 = 0

    Mientras el frame sea menor que el número total de sprites (7 en este caso), el módulo no hace nada y devuelve el mismo número.
    Justo cuando el frame intenta pasar a 8, el módulo lo detecta y lo reinicia a 0, creando el bucle perfecto.

"""

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
    # Inicializar GLFW
    if not glfw.init():
        return

    ventana = glfw.create_window(800, 600, "Animación con Sprites", None, None)
    glfw.make_context_current(ventana)

    # Cargar 5 sprites
    rutas = [
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajA.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajB.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajC.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajD.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajE.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajF.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajG.png",
        "/home/javier/Documentos/Programas/Python/Texturas/PNGs/PajH.png"
    ]

    sprites = [cargar_textura(r) for r in rutas]

    # Configurar OpenGL
    glEnable(GL_TEXTURE_2D)

    frame = 0
    velocidad = 0.15   # tiempo entre frames

                                                    # Loop de renderizado
    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT)

        # Seleccionar textura actual
        glBindTexture(GL_TEXTURE_2D, sprites[frame])

        # Dibujar un quad con la textura del sprite
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(-0.3, -0.3)
        glTexCoord2f(1, 0); glVertex2f( 0.3, -0.3)
        glTexCoord2f(1, 1); glVertex2f( 0.3,  0.3)
        glTexCoord2f(0, 1); glVertex2f(-0.3,  0.3)
        glEnd()

        # Avanzar frame
        frame = (frame + 1) % len(sprites)
        time.sleep(velocidad)

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()


main()
