""" USO DE GLUPERSPECTIVE Y GLULOOKAT, EXPLICACIÓN DETALLADA.
    
    Imagina que estás mirando a través de una pirámide truncada (llamada Frustum):
    Elegir gluPerspective() es como decidir: "Quiero una toma con un ángulo de 45 grados en una 
    pantalla con relación 4:3, y solo me interesan los objetos que están entre 0.1 y 50 metros de 
    distancia."

    gluPerspective(fovy, aspect, zNear, zFar)

    fovy (Field of View Y)          Es el ángulo vertical de visión.
    Angulo PEQUEÑO (ej: 30°)        Es como usar un teleobjetivo. Verás el mundo "acercado" o 
                                    con zoom. La perspectiva es más plana.
    Ángulo GRANDE (ej: 90°)         Es como usar un gran angular. Verás más del mundo, pero con 
                                    una distorsión de perspectiva más pronunciada (los objetos 
                                    cercanos se verán muy grandes).
                                    <<<Sugerencia: Un valor común es 45 o 60.>>>
    aspect (Aspect Ratio)           Es la relación de aspecto de la ventana (ANCHO / ALTO).
                                    Esto es crucial para que los objetos no se vean estirados. 
                                    Si tu ventana es 800x600, el aspect es 800 / 600 = 1.33.
    zNear y zFar                    Son los planos de corte cercano y lejano.
    zNear                           Es la distancia mínima que la cámara ve. Los objetos más cerca 
                                    de este plano se cortan. Debe ser un valor pequeño (ej: 0.1).
    zFar                            Es la distancia máxima que la cámara ve. Los objetos más allá 
                                    de este plano no se dibujan, lo que ayuda a ahorrar recursos. 
                                    Debe ser un valor grande (ej: 50.0).

                                    
    gluLookAt(): Colocar y Apuntar la Cámara (Matriz de Vista)
    gluLookAt() define dónde está la cámara, hacia dónde está mirando y cuál es su orientación vertical.
    Su Función: Mueve el mundo entero de forma que parezca que la cámara se ha movido o rotado.

    ¿Cómo funciona?
    Esta función toma 9 argumentos que se organizan en 3 grupos de coordenadas (X, Y, Z):

    gluLookAt(eyeX, eyeY, eyeZ,               1. Posición de la Cámara (Eye)
              centerX, centerY, centerZ,      2. El Punto al que Mira (Center)
              upX, upY, upZ)                  3. La Orientación Vertical (Up)

    eye (Posición de la Cámara): ¿Dónde está el fotógrafo? Si pones (0, 0, 10), la cámara está en (0, 0, 10).
    center (Punto al que Mira): ¿Hacia dónde apunta el fotógrafo? Si pones (0, 0, 0), la cámara mira 
    directamente al origen del mundo 3D.
    up (Orientación Vertical): ¿Qué es "arriba" para la cámara? Casi siempre es (0, 1, 0). Esto significa que 
    el eje Y es la dirección vertical de tu cámara (el lado superior de la pantalla).

    Analogía:
    Usar gluLookAt(0, 2, 5, 0, 0, 0, 0, 1, 0)       es como decir: "Coloca al fotógrafo 5 metros delante del 
                                                    origen y 2 metros por encima, apuntando al centro, y mantén 
                                                    la cabeza derecha (el eje Y es arriba)."


    ¿Cómo Instalar las Dependencias?

    pip install PyOpenGL PyOpenGL_accelerate glfw

    Explicación Visual, Imagina que:

        Ángulo 45°      Como mirar a través de un telescopio corto
        Ángulo 90°      Visión periférica normal
        Cerca=0.1       No ves objetos más cerca de 10cm
        Lejos=100       No ves objetos más lejos de 100 metros

    Efectos de Cambiar los Parámetros

    # Visión de ángulo amplio (como ojo de pez)
    gluPerspective(120, ancho/alto, 0.1, 100.0)

    # Visión telescópica (como mirar con binoculares)
    gluPerspective(20, ancho/alto, 0.1, 100.0)

    # Campo de visión muy cercano
    gluPerspective(45, ancho/alto, 10.0, 100.0)  # Solo objetos lejanos


"""


import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Variables globales
rotation_x = 0.0
rotation_y = 0.0


def inicializar_ventana():
    if not glfw.init():
        return None
    
    # Crear ventana
    ventana = glfw.create_window(800, 600, "Ejemplo de Perspectiva - OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        return None
    
    glfw.make_context_current(ventana)
    return ventana


def configurar_perspectiva(ancho, alto):
    # Configurar viewport
    glViewport(0, 0, ancho, alto)
    
    # Configurar proyección en perspectiva
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # ¡Aquí está la magia de la perspectiva!
    gluPerspective(
        45,                 # 45° - ángulo de visión (como unos binoculares)
        ancho/alto,         # Relación de aspecto (forma de la ventana)
        0.1,                # Distancia mínima visible (muy cercano)
        100.0               # Distancia máxima visible (muy lejano)
    )
    
    # Volver al modo de modelo/vista
    glMatrixMode(GL_MODELVIEW)


def dibujar_cubo():
    # Dibujar un cubo simple con caras de colores
    glBegin(GL_QUADS)
    
    # Cara frontal (roja)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    
    # Cara trasera (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    
    # Cara superior (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    
    # Cara inferior (amarilla)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    
    # Cara derecha (magenta)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    
    # Cara izquierda (cyan)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    
    glEnd()


def main():
    ventana = inicializar_ventana()
    if not ventana:
        return
    
    # Configurar perspectiva inicial
    ancho, alto = glfw.get_window_size(ventana)
    configurar_perspectiva(ancho, alto)
    
    # Habilitar depth testing para perspectiva correcta
    glEnable(GL_DEPTH_TEST)
    
    while not glfw.window_should_close(ventana):
        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Configurar cámara
        gluLookAt(
            0, 0, 5,    # Posición de la cámara (x, y, z)
            0, 0, 0,    # Punto al que mira (x, y, z)
            0, 1, 0     # Vector "arriba" (x, y, z)
        )
        
        # Rotar el cubo
        global rotation_x, rotation_y
        rotation_x += 0.5
        rotation_y += 0.3

        # Lo que se busca con estas dos rotaciones son distintas velocidades, 
        # una para el eje "x"
        glRotatef(rotation_x, 1, 0, 0)
        # y la otra para el eje "y"
        glRotatef(rotation_y, 0, 1, 0)
        # glRotatef(rotation_x, 1, 1, 0)
        
        # Dibujar escena
        dibujar_cubo()
        
        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(ventana)
        glfw.poll_events()
    
    glfw.terminate()


if __name__ == "__main__":
    main()