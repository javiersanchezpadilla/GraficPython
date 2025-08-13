""" Imagínate que OpenGL es como un pintor y tú eres el director de arte. Para que el pintor 
    pueda hacer su trabajo, primero necesita un lienzo. En la programación gráfica, ese lienzo 
    es una ventana. Usaremos la librería GLFW para crearla, ya que es ligera y muy común en 
    Python para este propósito.

    El proceso es como una receta de cocina:

    Inicializar GLFW: Es como preparar la estación de trabajo.
    Crear una ventana: Pedimos el lienzo. Le daremos un título y un tamaño.
    Configurar OpenGL: Le decimos a nuestro "pintor" cómo debe trabajar (versión, perfiles, etc.).

    El "bucle principal": Esto es el corazón de nuestro programa. Es un ciclo while infinito que se encarga de:

    Revisar si el usuario quiere cerrar la ventana.
    Dibujar en la ventana (esto lo veremos en un momento).
    Mostrar lo que hemos dibujado en la pantalla.
"""


import glfw
from OpenGL.GL import *

# 1. Inicializar GLFW
if not glfw.init():
    raise Exception("glfw no puede ser inicializado!")

# 2. Crear una ventana de 800x600 píxeles
window = glfw.create_window(800, 600, "Mi primera ventana en OpenGL", None, None)

if not window:
    glfw.terminate()
    raise Exception("La ventana glfw no puede ser creada!")

# Hacer el contexto de la ventana actual
glfw.make_context_current(window)

# 3. El bucle principal
while not glfw.window_should_close(window):
    # Dibuja aquí (¡por ahora, solo limpiaremos el color!)
    # Piensa en la pantalla como si fuera un lienzo de dos caras. Mientras tú estás 
    # dibujando en una cara, el usuario está viendo la otra. Esto evita que vean 
    # el proceso de dibujo y solo vean el resultado final, lo que elimina parpadeos.
    # Esta instruccción limpia el dibujo previo

    # Esta es la orden para limpiar la cara del lienzo en la que estás trabajando. 
    # El parámetro GL_COLOR_BUFFER_BIT le dice a OpenGL que limpie el "búfer de color", 
    # que es el área donde se almacena la información de color de cada píxel. Es como 
    # si le dieras un borrón y cuenta nueva al lienzo para el siguiente fotograma

    # Seguro te preguntas: "¿De qué color se limpia el lienzo?". OpenGL tiene una 
    # función para eso, que podríamos haber añadido a nuestro código:

    # glClearColor(rojo, verde, azul, alfa)
    # Esta función le dice a OpenGL qué color usar para limpiar. Los valores de 
    # rojo, verde, azul y alfa (transparencia) van de 0.0 a 1.0. Por ejemplo, 
    # glClearColor(1.0, 0.0, 0.0, 1.0) establecería el color de limpieza en un rojo sólido. 
    # Si no la defines, por defecto se usa un color negro.
    glClear(GL_COLOR_BUFFER_BIT)

    # 4. Refresca la pantalla para mostrar lo que hemos dibujado
    # Esta instrucción intercambia las dos caras del lienzo

    # Una vez que has terminado de dibujar todo lo que quieres en un fotograma, esta 
    # función le dice a GLFW que intercambie los lienzos. La cara que el usuario estaba 
    # viendo ahora se convierte en tu lienzo de trabajo y la cara en la que acabas de 
    # dibujar es la que se muestra en la pantalla.
    glfw.swap_buffers(window)
    glfw.poll_events()

# Terminamos el programa y cerramos todo
glfw.terminate()
