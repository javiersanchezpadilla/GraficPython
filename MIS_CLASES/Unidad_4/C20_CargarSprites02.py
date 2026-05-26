""" En este ejemplo vamos a cargar una hoja de sprites y recortarlos

Aqui vamos a cargar varias imagenes (sprites).

Este es un truco muy elegante para controlar los elementos
del arreglo o lista de sprites:

    frame = (frame + 1) % len(sprites)

Por ejemplo, si tengo 8 elementos en mi lista,
mi indice va del 0 al 7.

    rutas = [
        "PajA.png",   # indice 0
        "PajB.png",   # indice 1
        "PajC.png",   # indice 2
        "PajD.png",   # indice 3
        "PajE.png",   # indice 4
        "PajF.png",   # indice 5
        "PajG.png",   # indice 6
        "PajH.png"    # indice 7
    ]

    sprites = [cargar_textura(r) for r in rutas]

La línea:

    frame = (frame + 1) % len(sprites)

permite ciclar infinitamente entre los elementos.

Ejemplo con 8 sprites:

    0 % 8 = 0
    1 % 8 = 1
    2 % 8 = 2
    3 % 8 = 3
    4 % 8 = 4
    5 % 8 = 5
    6 % 8 = 6
    7 % 8 = 7
    8 % 8 = 0

Mientras frame sea menor que la cantidad total
de sprites, el modulo devuelve el mismo numero.

Cuando frame llega a 8:

    8 % 8 = 0

Entonces el indice vuelve al inicio automaticamente,
creando un ciclo perfecto.
"""

import glfw
from OpenGL.GL import *
from PIL import Image
import time
from pathlib import Path


def cargar_textura(ruta):
    """
    Carga una imagen y la convierte en una textura OpenGL.

    Args:
        ruta (str):
            Ruta de la imagen.

    Returns:
        int:
            ID de la textura generada.
    """

    imagen = Image.open(ruta).transpose(Image.FLIP_TOP_BOTTOM)

    img_data = imagen.convert("RGBA").tobytes()

    width, height = imagen.size

    tex_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, tex_id)

    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        width,
        height,
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        img_data
    )

    glTexParameteri(
        GL_TEXTURE_2D,
        GL_TEXTURE_MIN_FILTER,
        GL_LINEAR
    )

    glTexParameteri(
        GL_TEXTURE_2D,
        GL_TEXTURE_MAG_FILTER,
        GL_LINEAR
    )

    return tex_id


def cargar_spritesheet(ruta, num_frames):
    """
    Divide un spritesheet en multiples texturas OpenGL.

    Args:
        ruta (str):
            Ruta del spritesheet.

        num_frames (int):
            Cantidad de frames contenidos
            en el spritesheet.

    Returns:
        list[int]:
            Lista con los IDs de las texturas generadas.
    """

    imagen = Image.open(ruta).convert("RGBA")

    ancho_total, alto = imagen.size

    ancho_frame = ancho_total / num_frames

    texturas = []

    for i in range(num_frames):

        # Recorta el frame actual.
        izq = i * ancho_frame
        der = izq + ancho_frame

        frame = imagen.crop((izq, 0, der, alto))

        frame = frame.transpose(Image.FLIP_TOP_BOTTOM)

        img_data = frame.tobytes()

        tex_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, tex_id)

        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            ancho_frame,
            alto,
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            img_data
        )

        glTexParameteri(
            GL_TEXTURE_2D,
            GL_TEXTURE_MIN_FILTER,
            GL_LINEAR
        )

        glTexParameteri(
            GL_TEXTURE_2D,
            GL_TEXTURE_MAG_FILTER,
            GL_LINEAR
        )

        texturas.append(tex_id)

    return texturas


def main():
    """
    Funcion principal del programa.
    """

    # Inicializar GLFW.
    if not glfw.init():
        return

    ventana = glfw.create_window(
        800,
        600,
        "Animación con Sprites",
        None,
        None
    )

    glfw.make_context_current(ventana)

    # rutas = (
    #     "C:/Users/hecto/PycharmProjects/WarLife_v1/assets/sprites/enemigos/enemigo1/Death.png"
    # )
    rutas = Path.cwd() / 'MIS_CLASES/Unidad_4/PNGs/Sprites/Death.png'

    # sprites = [cargar_textura(r) for r in rutas]
    sprites = cargar_spritesheet(rutas, 6)

    # Configuracion OpenGL.
    glEnable(GL_TEXTURE_2D)

    glEnable(GL_BLEND)

    glBlendFunc(
        GL_SRC_ALPHA,
        GL_ONE_MINUS_SRC_ALPHA
    )

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glOrtho(
        0,
        800,
        0,
        600,
        -1,
        1
    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    frame = 0

    velocidad = 0.15


    # Loop principal de renderizado.
    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT)

        # Seleccionar textura actual.
        

        # Dibujar sprites.
        aumento_x = 0

        for i in range(len(sprites)):
            glBindTexture(GL_TEXTURE_2D, sprites[i])
            glBegin(GL_QUADS) 
            glTexCoord2f(0, 0); 
            glVertex2f(aumento_x, 400) 
            glTexCoord2f(1, 0); 
            glVertex2f(aumento_x + 96 , 400) 
            glTexCoord2f(1, 1); 
            glVertex2f(aumento_x + 96 , 496) 
            glTexCoord2f(0, 1); 
            glVertex2f(aumento_x, 496) 
            glEnd()

            aumento_x += 96

        glfw.swap_buffers(ventana)

        glfw.poll_events()

    glfw.terminate()


main()
