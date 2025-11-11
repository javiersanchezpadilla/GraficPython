""" El siguiente código permite entender el concepto de profundidad en una escena 3D.
    Usando OpenGL y GLFW, se dibujan dos cuadros (quads) a distintas distancias en el eje Z.
    El cuadro más cercano se dibuja en verde y el más lejano en amarillo.
    
    Observemos que la ubicación del cuadro amarillo con respecto al cuadro verde tiene coordenadas 
    en el eje “z” que indican que estará ubicado por atrás del cuadro verde, pero entonces 
    ¿por que cuando ejecutamos el programa no obtenemos este resultado?
    Cundo trabajos tres dimensiones (eje “X”, eje “Y”, eje “Z”), requerimos habilitar un buffer que 
    nos permita en todo momento calcular la ubicación de los objetos representados en la pantalla, 
    tenemos que recordar que hemos trabajado con dos ejes hasta el momento (eje “X”, eje “Y”), 
    el concepto de profundidad no era importante y simplemente dibujamos las figuras las cuales 
    se representaban una seguida de otra, en este caso si representamos figuras simplemente se 
    dibujaran arriba de cualquier figura dibujada previamente sin importar su ubicación en el eje “Z”, 
    debemos considerar que nuestra pantalla es  plana, si lo pensamos realmente no existe el eje “Z” 
    se requiere 'algo' que nos permita calcular esta posición para  visualizar correctamente con base 
    a los resultados esperados simulando la la distancia en el eje “Z” de forma correcta (profundidad), 
    para esto declararemos el uso del buffer GL_DEPTH_TEST, el cual nos permitirá calcular la profundidad
    de los objetos en la escena 3D.

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    Ahora lo activamos en la de iniciar_ventana() con la instrucción:
        glEnable(GL_DEPTH_TEST)


    Tambien podriamos indicar ambas lineas directamente en el ciclo principal o dentro dela funcion de dibujo
    
    def dibujar_cuadros(z1, z2):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

    De esta forma nos aseguramos que en cada cuadro se limpie el buffer de profundidad y se active
    la prueba de profundidad.    
    """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def iniciar_ventana():
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(600, 600, "Uso de los puertos de vision", None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)

    # Activar buffer de profundidad, necesario para trabajar en 3D y calcular la profundidad de los
    # objetos en la escena.
    glEnable(GL_DEPTH_TEST)

    return ventana


def configurar_coordenadas_ventana(menos_x, mas_x, menos_y, mas_y, menos_z=-1.0, mas_z=1.0):
    # Configura la proyección para usar coordenadas de píxeles (ventana).
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    # Esto mapea [0, ancho] en X y [0, alto] en Y
    glOrtho(menos_x, mas_x, menos_y, mas_y, menos_z, mas_z)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# Función para dibujar un cuadro
def dibujar_cuadros(z1, z2):

    glColor3f(1.0, 1.0, 1.0)        # Ejes coordenados
    glBegin(GL_LINES)
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)
    glVertex3f(0.0, -15.0, 0.0)
    glVertex3f(0.0,  15.0, 0.0)
    glEnd()

    glColor3f(0.3, 0.6, 0.1)        # Cuadro verde
    glBegin(GL_QUADS)
    glVertex3f(-5.0, 12.0, z1)
    glVertex3f(5.0, 12.0, z1)
    glVertex3f(5.0, -12.0, z1)
    glVertex3f(-5.0, -12.0, z1)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)        # Cuadro amarillo
    glBegin(GL_QUADS)
    glVertex3f(-4.0, 11.0, z2)
    glVertex3f(7.0, 11.0, z2)
    glVertex3f(7.0, -7.0, z2)
    glVertex3f(-4.0, -7.0, z2)
    glEnd()



def programa_principal():
    ventana = iniciar_ventana() 
    configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)

    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Distancias iniciales de los cuadros
        z_cuadro1 = -3   # más cercano
        z_cuadro2 = -7   # más lejano
        dibujar_cuadros(z_cuadro2, z_cuadro1) 
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
