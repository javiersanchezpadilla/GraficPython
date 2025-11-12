""" Mis pruebas de perspectiva con gluPerspective """

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *       # <-- Aqui estamos importando la biblioteca GLUT FreeGLUT para las figuras precargadas.


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
    glutInit()  # Inicializar GLUT para usar figuras precargadas
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
def dibujar_figuras_precargadas(angulo_rotacion):

    glMatrixMode(GL_PROJECTION)                     # --- PROYECCIÓN ---
    glLoadIdentity()                                # borrar cualquier transformación de matriz anterior
    
    # Elegir gluPerspective(45, 800/600, 0.1, 50)     es como decidir: "Quiero una toma con un ángulo de 45 grados 
    #                                                 en una pantalla con relación 4:3 (800x600 = 4:3), y solo me 
    #                                                 interesan los objetos que están entre 0.1 y 50 metros de distancia."
    #                                                 600/600 = 1:1

    # gluPerspective(fovy, aspect, zNear, zFar)

    # fovy (Field of View Y)          Es el ángulo vertical de visión.
    # Angulo PEQUEÑO (ej: 30°)        Es como usar un teleobjetivo. Verás el mundo "acercado" o 
    #                                 con zoom. La perspectiva es más plana.
    # Ángulo GRANDE (ej: 90°)         Es como usar un gran angular. Verás más del mundo, pero con 
    #                                 una distorsión de perspectiva más pronunciada (los objetos 
    #                                 cercanos se verán muy grandes).
    #                                 <<<Sugerencia: Un valor común es 45 o 60.>>>
    # aspect (Aspect Ratio)           Es la relación de aspecto de la ventana (ANCHO / ALTO).
    #                                 Esto es crucial para que los objetos no se vean estirados. 
    #                                 Si tu ventana es 800x600, el aspect es 800 / 600 = 1.33.
    # zNear y zFar                    Son los planos de corte cercano y lejano.
    # zNear                           Es la distancia mínima que la cámara ve. Los objetos más cerca 
    #                                 de este plano se cortan. Debe ser un valor pequeño (ej: 0.1).
    # zFar                            Es la distancia máxima que la cámara ve. Los objetos más allá 
    #                                 de este plano no se dibujan, lo que ayuda a ahorrar recursos. 
    #                                 Debe ser un valor grande (ej: 50.0).


    gluPerspective(100, 600/600, 1, 50)


    glMatrixMode(GL_MODELVIEW)                      # --- CÁMARA ---
    glLoadIdentity()
    # Usar gluLookAt(0, 2, 5, 0, 0, 0, 0, 1, 0)       es como decir: "Coloca al fotógrafo 5 metros delante del 
    #                                                 origen y 2 metros por encima, apuntando al centro, y mantén 
    #                                                 la cabeza derecha (el eje Y es arriba)."
    gluLookAt(5, 0, 15, 0, 0, 0, 0, 1, 0)
                                                    
    # Dibujo de los ejes de coordenadas 
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)        # Verde para X
    glVertex3f(-15.0, 0.0, 0.0)
    glVertex3f(15.0, 0.0, 0.0)

    glColor3f(1.0, 0.0, 0.0)        # Rojo para Y
    glVertex3f(0.0,-15.0, 0.0)
    glVertex3f(0.0, 15.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)        # Azul para Z
    glVertex3f( 0.0, 0.0, -15.0)
    glVertex3f(0.0, 0.0, 15.0)
    glEnd()
    glPopMatrix()

    glColor3f(1.0,1.0,1.0)
	# Texto(6,-6,14,"FUNCIONES PRECARGADAS EN OPENGL");

    glColor3f(1.0,1.0,0.0)
    # Texto(1,-14,12,"Cono");
    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(angulo_rotacion, 1.0, 1.0, 1.0)
    glutWireCone(5, 5, 30, 30)
    glPopMatrix()




def programa_principal():
    ventana = iniciar_ventana() 
    # ya no es necesario definir las coordenadas de ventana ortogonales
    # configurar_coordenadas_ventana(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)
    angulo_lento = 0.0

    while not glfw.window_should_close(ventana):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        dibujar_figuras_precargadas(angulo_lento) 
        angulo_lento += 0.8

        glfw.swap_buffers(ventana)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    programa_principal()
