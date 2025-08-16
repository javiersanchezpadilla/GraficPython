""" Dibujando un solo carácter

    Como ya sabes, para dibujar una letra, la tratamos como una textura. Para lograr esto en OpenGL, 
    necesitamos seguir unos pasos clave:

    A) Cargar la textura: Primero, tenemos que cargar la imagen de nuestro atlas de texturas en la memoria 
       de OpenGL. Hay comandos especiales para esto que le dicen a OpenGL que reserve un espacio para una imagen.
    B) Activar el modo de texturas: Antes de dibujar, le decimos a OpenGL: "¡Prepárate, que voy a usar texturas!". 
       Esto se hace con un comando llamado glEnable().
    C) Dibujar el cuadrado (o quad): Usamos los comandos glBegin(GL_QUADS) y glEnd() para dibujar un cuadrado. 
       Este será el "lienzo" donde se pegará nuestra letra.
    D) Mapear la textura: Para cada vértice del cuadrado, usamos el comando glTexCoord2f() para decirle a OpenGL 
       qué parte de la textura (usando las coordenadas de nuestro atlas) debe ir en ese vértice.

Especificar el vértice: Justo después de glTexCoord2f(), usamos glVertex2f() para especificar dónde debe estar ese 
vértice en la pantalla.
Aquí tienes un ejemplo de código que dibuja una sola letra 'A' en la pantalla, suponiendo que nuestro atlas de texturas 
está cargado y listo.


glTexCoord2f(): Le dice a OpenGL qué parte de la textura (nuestro atlas) debe usar para el siguiente vértice.

glVertex2f(): Le dice a OpenGL dónde en la pantalla debe dibujar ese vértice.

Piénsalo como si estuvieras trabajando con sellos. 
glTexCoord2f() te dice qué parte del sello vas a usar (la "H", la "O", etc.), mientras que 
glVertex2f() te dice en qué lugar del papel vas a estampar ese sello.

ESTE EJEMPLO SOLO CONTEMPLA LA CARGA DE UNA IMAGEN QUE REPRESENTA UN ATLAS DE TEXTURAS
NO EJECUTAR 


"""



# Esta función dibuja un solo carácter en la posición (x, y)
# Los parámetros 'u' y 'v' son las coordenadas de nuestro atlas de texturas
def dibujar_caracter(x, y, u, v, tamano):
    # Definimos las coordenadas del atlas para la letra
    # Cada letra ocupa una porción de 0.25x0.25 en nuestro atlas 4x4
    tex_coords = [
        (u, v),         # Esquina inferior izquierda del atlas
        (u + 0.25, v),  # Esquina inferior derecha
        (u + 0.25, v + 0.25), # Esquina superior derecha
        (u, v + 0.25)   # Esquina superior izquierda
    ]

    # Definimos los vértices del cuadrado en la pantalla
    # El tamaño del cuadrado depende del parámetro 'tamano'
    quad_vertices = [
        (x, y),
        (x + tamano, y),
        (x + tamano, y + tamano),
        (x, y + tamano)
    ]
    
    # Comenzamos a dibujar un cuadrado
    glBegin(GL_QUADS)
    for i in range(4):
        # Mapeamos la textura al vértice
        glTexCoord2f(tex_coords[i][0], tex_coords[i][1])
        # Dibujamos el vértice en la pantalla
        glVertex2f(quad_vertices[i][0], quad_vertices[i][1])
    glEnd()

# ... y en nuestro bucle principal lo usaríamos así:
# (asumiendo que la textura está cargada y enlazada)

# dibujar_caracter(0.0, 0.0, 0.0, 0.75, 0.5) # Dibuja la 'A' en la posición (0,0) con un tamaño de 0.5