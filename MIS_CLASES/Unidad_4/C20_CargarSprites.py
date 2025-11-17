import glfw
from OpenGL.GL import *
from PIL import Image
import time

# --------------------------
# Función para cargar textura
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

    return tex_id

# ----------------------------
# Programa principal GLFW
# ----------------------------
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

    # -------------------------
    # Loop de renderizado
    # -------------------------
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
