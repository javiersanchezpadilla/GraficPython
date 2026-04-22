"""

    Este código aún no funciona pero es la alternativa para no usar glut.gluPerspective() ni glut.gluLookAt(),
    en su lugar es 

    proyeccion = glm.perspective(glm.radians(45.0), ancho / alto, 0.1, 100.0)
    vista = glm.lookAt(posicion_ojo, mirar_a, arriba)

    Requerimiento de instalación

    pip3 install PyGLM

"""

import glfw
from OpenGL.GL import *
import glm                  # Importamos la libreria moderna
import math

def main():
    if not glfw.init(): return
    
    ancho, alto = 800, 600
    ventana = glfw.create_window(ancho, alto, "Camara con PyGLM", None, None)
    glfw.make_context_current(ventana)
    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(ventana):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # --- CONFIGURACION MODERNA CON GLM ---

        # 1. Matriz de Proyeccion (La lente)
        # glm.perspective(fovy_en_radianes, aspecto, cerca, lejos)
        # Nota: GLM usa radianes, por eso usamos glm.radians(45)
        proyeccion = glm.perspective(glm.radians(45.0), ancho / alto, 0.1, 100.0)

        # 2. Matriz de Vista (La posicion)
        # glm.lookAt(posicion_ojo, centro_mirada, vector_arriba)
        tiempo = glfw.get_time()
        radio = 5.0
        # Hacemos que la camara gire en circulo usando seno y coseno
        cam_x = math.sin(tiempo) * radio
        cam_z = math.cos(tiempo) * radio
        
        posicion_ojo = glm.vec3(cam_x, 2.0, cam_z)
        mirar_a = glm.vec3(0.0, 0.0, 0.0)
        arriba = glm.vec3(0.0, 1.0, 0.0)
        
        vista = glm.lookAt(posicion_ojo, mirar_a, arriba)

        # --- APLICAR LAS MATRICES ---
        # En OpenGL "Fixed Pipeline" (el que estas usando), las cargamos asi:
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMultMatrixf(glm.value_ptr(proyeccion)) # Enviamos la matriz de GLM a OpenGL

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glMultMatrixf(glm.value_ptr(vista)) # Enviamos la matriz de GLM a OpenGL

        # --- DIBUJAR ALGO ---
        # Dibujamos un triangulo simple en el centro
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0); glVertex3f(-0.5, -0.5, 0)
        glColor3f(0, 1, 0); glVertex3f(0.5, -0.5, 0)
        glColor3f(0, 0, 1); glVertex3f(0, 0.5, 0)
        glEnd()

        glfw.swap_buffers(ventana)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()