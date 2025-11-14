import glfw
from OpenGL.GL import *
from PIL import Image
import time

# --------------------------
# Cargar textura
# --------------------------
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

    return tex_id, width, height

# Dibujar quad
def dibujar_quad(x, y, w, h):
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x - w, y - h)
    glTexCoord2f(1, 0); glVertex2f(x + w, y - h)
    glTexCoord2f(1, 1); glVertex2f(x + w, y + h)
    glTexCoord2f(0, 1); glVertex2f(x - w, y + h)
    glEnd()

# ----------------------------
# Programa principal
# ----------------------------
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(800, 600, "Scroll Horizontal", None, None)
    glfw.make_context_current(ventana)

    # Cargar fondo
    fondo_tex, fondo_w, fondo_h = cargar_textura("/home/javier/Documentos/Programas/Python/Texturas/PNGs/FondoSprite02.bmp")

    glEnable(GL_TEXTURE_2D)

    # Offset horizontal del fondo
    offset = 0.0
    velocidad = 0.002  # velocidad del scroll

    # Loop principal
    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT)

        glBindTexture(GL_TEXTURE_2D, fondo_tex)

        # Mover textura
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
