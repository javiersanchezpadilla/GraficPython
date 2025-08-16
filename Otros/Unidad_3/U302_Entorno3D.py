""" Configuración del entorno 3D
    Para que OpenGL sepa cómo proyectar objetos 3D en tu pantalla 2D, necesitamos hacer dos cosas: 
    decirle a la "cámara" cómo debe ver el mundo y activar la percepción de profundidad.

    1. CONFIGURANDO LA CÁMARA (LA MATRIZ DE PROYECCIÓN)

    La matriz de proyección es como la lente de una cámara. Le dice a OpenGL cómo debe representar 
    la profundidad. Usaremos el comando gluPerspective() para esto. Aunque no es de OpenGL "puro", 
    es una función de una biblioteca complementaria (glu) que simplifica la configuración y se usa 
    a menudo.

                    gluPerspective(angulo, relacion_aspecto, cerca, lejos)

    angulo: El campo de visión de la cámara. Un valor de 45.0 es un buen punto de partida, ya que 
            simula una visión humana.
    relacion_aspecto: La relación entre el ancho y el alto de la ventana. Esto evita que los objetos 
            se vean estirados. Por ejemplo, en una ventana de 800x600, sería 800/600.
    cerca y lejos: Son las distancias mínima y máxima que la cámara puede "ver". Cualquier cosa más 
            cerca que el valor cerca o más lejos que el valor lejos no se dibujará. Esto nos ayuda a 
            optimizar el rendimiento.

    2. HABILITANDO LA PROFUNDIDAD (EL Z-Buffer)

    Para que los objetos más cercanos cubran a los más lejanos, OpenGL necesita una forma de guardar 
    la profundidad de cada píxel. A esto se le llama el Z-Buffer o Buffer de Profundidad. Debemos 
    habilitarlo con el comando glEnable(GL_DEPTH_TEST) y limpiarlo en cada fotograma con 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT).

    Aquí tienes el código completo para configurar un entorno 3D. Fíjate que hay una nueva sección en main() para la configuración 3D."""


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
    pygame.init()
    # Habilitamos el doble buffer y la profundidad
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    
    # --- Configuración 3D ---
    glEnable(GL_DEPTH_TEST) # Habilitamos el buffer de profundidad
    glClearColor(0.0, 0.0, 0.0, 1.0) # Color de fondo
    glMatrixMode(GL_PROJECTION) # Le decimos a OpenGL que vamos a configurar la cámara
    glLoadIdentity()
    gluPerspective(45, (800/600), 0.1, 50.0) # Configuramos nuestra cámara

    glMatrixMode(GL_MODELVIEW) # Volvemos al modo de modelado
    glLoadIdentity()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Limpiamos el color y la profundidad en cada fotograma
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # **********************************************************  
        # --- Aquí irá nuestro código para dibujar objetos 3D ---
        # **********************************************************

        pygame.display.flip()

main()