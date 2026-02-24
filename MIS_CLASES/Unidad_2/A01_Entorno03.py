""" Mismo código pero orientado a objetos.

    Pasar de un código "lineal" (procedural) a uno basado en clases y objetos
    (Programación Orientada a Objetos) es como pasar de tener herramientas 
    sueltas en una mesa a tener una "caja de herramientas" organizada.

    En lugar de tener funciones y variables flotando, creamos un objeto llamado
    VentanaApp que se encarga de su propia vida: se inicia, se dibuja y se cierra solo.

    ¿Por qué usar clases en OpenGL?
    -------------------------------
    A) Organización: Todo lo relacionado con la ventana vive dentro del objeto.
    B) Estado: Puedes guardar variables (como el color de fondo o el ángulo de rotación) 
       como atributos (self.variable) y acceder a ellos desde cualquier parte de la clase.

       
    Explicación de los cambios:
    ---------------------------
    __init__        Es el punto de partida. En lugar de pasar el ancho y el alto cada vez, 
                    los guardamos dentro del objeto usando self.
    self            Es como decir "mi propio/a". self.ventana significa "mi ventana", lo que 
                    permite que la función renderizar sepa qué ventana debe usar sin necesidad 
                    de pasarla como argumento.

    Método ejecutar Ahora el bucle while está encapsulado. Para que el programa funcione, solo
                    necesitas crear el objeto y llamar a app.ejecutar().

                    
    Separación de responsabilidades:
    --------------------------------
    inicializar()   Se encarga de la configuración.
    renderizar()    Se encarga exclusivamente del dibujo.
    finalizar()     Se encarga de la limpieza.

    Esto hace que el código sea mucho más fácil de ampliar. 
"""
import glfw
from OpenGL.GL import *

class MiAplicacion:
    def __init__(self, ancho, alto, titulo):
        """
        Constructor: Aquí se definen las propiedades iniciales del objeto.
        Es como el 'manual de instrucciones' para crear nuestra app.
        """
        self.ancho = ancho      # Ancho de la ventana
        self.alto = alto        # Altura de la ventana
        self.titulo = titulo    # Nombre visible de la ventana
        self.ventana = None     # Este atributo contendra la ventana

    def inicializar(self):
        """Prepara GLFW y crea la ventana."""
        if not glfw.init():
            raise Exception("No se pudo iniciar GLFW")

        self.ventana = glfw.create_window(self.ancho, self.alto, self.titulo, None, None)
        
        if not self.ventana:
            glfw.terminate()
            raise Exception("No se pudo crear la ventana")

        glfw.make_context_current(self.ventana)
        print("Ventana inicializada correctamente.")

    def renderizar(self):
        """Contiene la lógica de dibujo (lo que se repite)."""
        # Pintamos el fondo de amarillo
        glClearColor(1.0, 1.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Aquí podrías llamar a otras funciones de dibujo como:
        # self.dibujar_cubo()

    def ejecutar(self):
        """El bucle principal de la aplicación."""
        self.inicializar()

        while not glfw.window_should_close(self.ventana):
            # 1. Dibujar
            self.renderizar()

            # 2. Intercambiar buffers y revisar eventos
            glfw.swap_buffers(self.ventana)
            glfw.poll_events()

        # Al salir del bucle, cerramos todo
        self.finalizar()

    def finalizar(self):
        """Limpia los recursos al cerrar."""
        glfw.terminate()
        print("Aplicación finalizada.")



if __name__ == "__main__":
    # 1. Creamos la instancia (el objeto)
    app = MiAplicacion(800, 600, "Ventana con Clases y Objetos")
   
    # 2. Iniciamos el ciclo de vida de la aplicación
    app.ejecutar()
