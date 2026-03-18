"""
Sistema Solar 2D - Transformaciones en Dos Dimensiones
=======================================================
Este programa ilustra los tres tipos principales de transformaciones
geometricas 2D aplicadas sobre un sistema solar simplificado:

    1. TRASLACION  -- todo el sistema solar se desplaza por la pantalla.
                      Al salir por un extremo, reaparece por el opuesto.

    2. ROTACION    -- el planeta orbita alrededor del sol (pivote externo).
                      la luna orbita alrededor del planeta (pivote interno).
                      Identico al patron visto en clase: pivote externo +
                      pivote interno que se mueve con el objeto padre.

    3. ESCALADO    -- el sol pulsa (crece y se reduce ciclicamente)
                      siempre respecto a su propio centro como punto fijo.

Las tres transformaciones actuan en conjunto cada frame, formando
una escena coherente donde cada elemento depende del anterior:
    Sol (fijo + pulso) --> Planeta (orbita al sol) --> Luna (orbita al planeta)

Formulas aplicadas:
    Traslacion : x' = x + tx              y' = y + ty
    Rotacion   : x' = (x-px)*cos(a) - (y-py)*sin(a) + px
                 y' = (x-px)*sin(a) + (y-py)*cos(a) + py
    Escalado   : x' = px + (x-px)*sx     y' = py + (y-py)*sy

Nivel de conocimiento aplicado:
    - glfw para ventana y bucle principal
    - OpenGL inmediato: glBegin/glEnd, primitivas basicas
    - math para trigonometria (sin, cos, radians)
    - Funciones separadas por responsabilidad
    - Animacion acumulativa frame a frame (mismo enfoque del codigo de referencia)
"""

import glfw
from OpenGL.GL import *
import math


# ===========================================================================
# VENTANA
# ===========================================================================

def iniciar_ventana():
    """
    Inicializa GLFW y crea la ventana de visualizacion.
    Retorna el objeto ventana para usarlo en el bucle principal.
    """
    if not glfw.init():
        raise Exception("No se pudo iniciar GLFW")
    ventana = glfw.create_window(800, 600,
                                 "Sistema Solar 2D - Transformaciones",
                                 None, None)
    if not ventana:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    glfw.make_context_current(ventana)
    return ventana


# ===========================================================================
# TRANSFORMACIONES
# ===========================================================================

def trasladar_vertice(x, y, tx, ty):
    """
    Desplaza un punto (x, y) sumando el vector de traslacion (tx, ty).

    Parametros:
        x, y -- coordenadas originales del punto
        tx   -- desplazamiento horizontal
        ty   -- desplazamiento vertical

    Retorna:
        [x', y'] -- coordenadas desplazadas

    Formula:
        x' = x + tx
        y' = y + ty

    En el sistema solar: mueve TODOS los elementos del sistema juntos,
    manteniendo sus posiciones relativas entre si.
    """
    return [x + tx, y + ty]


def rotar_vertice(x, y, px, py, angulo_grados):
    """
    Rota un punto (x, y) alrededor de un pivote (px, py).

    Parametros:
        x, y          -- coordenadas originales del punto
        px, py        -- pivote de rotacion
        angulo_grados -- angulo de rotacion en grados

    Retorna:
        [x', y'] -- coordenadas rotadas

    Pasos (identicos al codigo de referencia visto en clase):
        1. Convertir angulo a radianes
        2. Trasladar al origen restando el pivote
        3. Aplicar rotacion con cos y sin
        4. Trasladar de vuelta sumando el pivote

    En el sistema solar:
        - Pivote = centro del sol  --> el planeta orbita alrededor del sol
        - Pivote = centro del planeta --> la luna orbita alrededor del planeta
    """
    # Paso 1: convertir grados a radianes
    rad = math.radians(angulo_grados)

    # Paso 2: trasladar al origen
    x_t = x - px
    y_t = y - py

    # Paso 3: rotar
    x_r = x_t * math.cos(rad) - y_t * math.sin(rad)
    y_r = x_t * math.sin(rad) + y_t * math.cos(rad)

    # Paso 4: trasladar de vuelta al pivote
    return [x_r + px, y_r + py]


def escalar_vertice(x, y, px, py, sx, sy):
    """
    Escala un punto (x, y) respecto a un punto fijo (px, py).

    Parametros:
        x, y   -- coordenadas originales del punto
        px, py -- punto fijo del escalado (el objeto escala hacia/desde aqui)
        sx, sy -- factores de escala en X e Y

    Retorna:
        [x', y'] -- coordenadas escaladas

    Pasos (mismo patron de 3 pasos que la rotacion):
        1. Trasladar el punto fijo al origen
        2. Aplicar el factor de escala
        3. Trasladar de vuelta

    Formula:
        x' = px + (x - px) * sx
        y' = py + (y - py) * sy

    En el sistema solar: el sol crece y se reduce respecto a su propio
    centro, simulando el pulso de una estrella.
    """
    # Paso 1: trasladar al origen
    x_t = x - px
    y_t = y - py

    # Paso 2: escalar
    x_e = x_t * sx
    y_e = y_t * sy

    # Paso 3: trasladar de vuelta
    return [x_e + px, y_e + py]


# ===========================================================================
# UTILIDADES DE DIBUJO
# ===========================================================================

def circulo_vertices(cx, cy, radio, segmentos):
    """
    Calcula los vertices que aproximan un circulo usando segmentos de linea.
    Cuantos mas segmentos, mas suave se ve el circulo.

    Parametros:
        cx, cy    -- centro del circulo
        radio     -- radio del circulo
        segmentos -- cantidad de vertices del poligono aproximado

    Retorna:
        lista plana [x0,y0, x1,y1, ..., xn,yn] de vertices

    Cada vertice se calcula con trigonometria basica:
        x = cx + radio * cos(angulo)
        y = cy + radio * sin(angulo)
    donde el angulo recorre 0 a 2*pi dividido en 'segmentos' pasos.
    """
    puntos = []
    for i in range(segmentos):
        angulo = 2.0 * math.pi * i / segmentos
        puntos.append(cx + radio * math.cos(angulo))
        puntos.append(cy + radio * math.sin(angulo))
    return puntos


def dibuja_circulo_relleno(cx, cy, radio, r, g, b, segmentos=40):
    """
    Dibuja un circulo relleno usando GL_TRIANGLE_FAN.

    GL_TRIANGLE_FAN: el primer vertice es el centro, los siguientes
    forman triangulos con el anterior, creando un abanico que rellena
    el circulo completo.

    Parametros:
        cx, cy    -- centro del circulo
        radio     -- radio
        r, g, b   -- color de relleno
        segmentos -- precision del circulo (mas = mas suave)
    """
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)                      # Centro del abanico
    for i in range(segmentos + 1):          # +1 para cerrar el circulo
        angulo = 2.0 * math.pi * i / segmentos
        glVertex2f(cx + radio * math.cos(angulo),
                   cy + radio * math.sin(angulo))
    glEnd()


def dibuja_circulo_contorno(cx, cy, radio, r, g, b, segmentos=40):
    """
    Dibuja solo el contorno de un circulo usando GL_LINE_LOOP.

    GL_LINE_LOOP: conecta todos los vertices con lineas y cierra
    automaticamente el ultimo con el primero.

    Parametros:
        cx, cy    -- centro del circulo
        radio     -- radio
        r, g, b   -- color del contorno
        segmentos -- precision del circulo
    """
    glColor3f(r, g, b)
    glBegin(GL_LINE_LOOP)
    for i in range(segmentos):
        angulo = 2.0 * math.pi * i / segmentos
        glVertex2f(cx + radio * math.cos(angulo),
                   cy + radio * math.sin(angulo))
    glEnd()


def dibuja_orbita(cx, cy, radio):
    """
    Dibuja la trayectoria circular de una orbita como referencia visual.
    Usa un contorno gris tenue para no distraer del movimiento principal.

    Parametros:
        cx, cy -- centro de la orbita (posicion actual del cuerpo padre)
        radio  -- radio de la orbita
    """
    dibuja_circulo_contorno(cx, cy, radio, 0.25, 0.25, 0.30, segmentos=60)


def dibuja_ejes():
    """
    Dibuja los ejes coordenados X e Y en gris como referencia visual.
    """
    glBegin(GL_LINES)
    glColor3f(0.2, 0.2, 0.25)
    glVertex2f(-1.0,  0.0)
    glVertex2f( 1.0,  0.0)
    glVertex2f( 0.0, -1.0)
    glVertex2f( 0.0,  1.0)
    glEnd()


def dibuja_estrellas(estrellas):
    """
    Dibuja puntos blancos pequenos como fondo de estrellas.
    Las estrellas son estaticas: solo sirven de referencia visual
    para que el movimiento de traslacion del sistema sea perceptible.

    Parametros:
        estrellas -- lista plana [x0,y0, x1,y1, ...] de posiciones fijas
    """
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(0.8, 0.8, 0.8)
    for i in range(0, len(estrellas), 2):
        glVertex2f(estrellas[i], estrellas[i + 1])
    glEnd()


# ===========================================================================
# FUNCION PRINCIPAL DE DIBUJO
# ===========================================================================

def dibuja(sistema, estrellas):
    """
    Renderiza un frame completo del sistema solar aplicando las tres
    transformaciones en el orden correcto cada frame.

    Orden de aplicacion por frame:
        1. Traslacion  -- mueve el centro del sol (y con el, todo lo demas)
        2. Escalado    -- pulsa el sol respecto a su centro actual
        3. Rotacion    -- orbita planeta alrededor del sol
                         orbita luna alrededor del planeta

    Parametro:
        sistema   -- diccionario con todo el estado del sistema solar
        estrellas -- lista de posiciones fijas de estrellas de fondo

    El uso de un diccionario agrupa el estado de forma clara, igual que
    el codigo de referencia agrupa los datos en listas separadas por objeto.
    """
    glClearColor(0.02, 0.02, 0.08, 1.0)    # Fondo azul muy oscuro (espacio)
    glClear(GL_COLOR_BUFFER_BIT)

    # Referencia visual fija
    dibuja_estrellas(estrellas)
    dibuja_ejes()

    # Extraer posiciones actuales para facilitar lectura
    sx  = sistema["sol_x"]
    sy  = sistema["sol_y"]
    px  = sistema["planeta_x"]
    py  = sistema["planeta_y"]
    lx  = sistema["luna_x"]
    ly  = sistema["luna_y"]
    sr  = sistema["sol_radio"]

    # -------------------------------------------------------------------
    # DIBUJO de orbitas (trayectorias de referencia visual)
    # La orbita del planeta se centra en el sol
    # La orbita de la luna se centra en el planeta
    # -------------------------------------------------------------------
    dibuja_orbita(sx, sy, sistema["orbita_planeta"])
    dibuja_orbita(px, py, sistema["orbita_luna"])

    # -------------------------------------------------------------------
    # DIBUJO de los cuerpos celestes
    # -------------------------------------------------------------------

    # Sol: circulo amarillo-naranja con contorno mas brillante
    dibuja_circulo_relleno(sx,  sy,  sr,        0.98, 0.78, 0.10)
    dibuja_circulo_contorno(sx, sy,  sr,        1.00, 0.95, 0.40)

    # Planeta: circulo azul-verdoso
    dibuja_circulo_relleno(px,  py,  0.06,      0.20, 0.55, 0.90)
    dibuja_circulo_contorno(px, py,  0.06,      0.50, 0.80, 1.00)

    # Luna: circulo gris pequeno
    dibuja_circulo_relleno(lx,  ly,  0.025,     0.70, 0.70, 0.72)
    dibuja_circulo_contorno(lx, ly,  0.025,     0.90, 0.90, 0.92)

    # Linea de referencia: sol --> planeta (muestra el radio orbital)
    glBegin(GL_LINES)
    glColor3f(0.30, 0.30, 0.15)
    glVertex2f(sx, sy)
    glVertex2f(px, py)
    glEnd()

    # Linea de referencia: planeta --> luna
    glBegin(GL_LINES)
    glColor3f(0.25, 0.25, 0.30)
    glVertex2f(px, py)
    glVertex2f(lx, ly)
    glEnd()

    # ===================================================================
    # TRANSFORMACION 1: TRASLACION
    # Todo el sistema se desplaza tx en X cada frame.
    # Se trasladan: centro del sol, posicion del planeta y posicion de
    # la luna, manteniendo sus posiciones relativas intactas.
    # ===================================================================
    tx = sistema["traslacion_tx"]

    sistema["sol_x"],     sistema["sol_y"]     = trasladar_vertice(sx, sy, tx, 0.0)
    sistema["planeta_x"], sistema["planeta_y"] = trasladar_vertice(px, py, tx, 0.0)
    sistema["luna_x"],    sistema["luna_y"]    = trasladar_vertice(lx, ly, tx, 0.0)

    # Ciclo de traslacion: si el sol sale por la derecha, reaparece por la izquierda
    # Se verifica con el centro del sol
    if sistema["sol_x"] > 1.3:
        sistema["sol_x"]     -= 2.6
        sistema["planeta_x"] -= 2.6
        sistema["luna_x"]    -= 2.6

    # Actualizar coordenadas locales tras traslacion para usar en las
    # siguientes transformaciones dentro de este mismo frame
    sx = sistema["sol_x"]
    sy = sistema["sol_y"]
    px = sistema["planeta_x"]
    py = sistema["planeta_y"]
    lx = sistema["luna_x"]
    ly = sistema["luna_y"]

    # ===================================================================
    # TRANSFORMACION 2: ESCALADO (pulso del sol)
    # El radio del sol crece y se reduce ciclicamente.
    # El escalado se aplica al radio directamente porque el circulo
    # se recalcula cada frame con circulo_vertices(), por lo que
    # escalar el radio es equivalente a escalar todos sus vertices
    # respecto al centro del sol.
    # ===================================================================

    # Incremento del radio segun la direccion actual del pulso
    delta = 0.0003 * sistema["pulso_dir"]
    sistema["sol_radio"] += delta

    # Inversion de direccion al alcanzar los limites del pulso
    if sistema["sol_radio"] >= 0.165:   # Radio maximo del pulso
        sistema["pulso_dir"] = -1
    if sistema["sol_radio"] <= 0.120:   # Radio minimo del pulso
        sistema["pulso_dir"] =  1

    # ===================================================================
    # TRANSFORMACION 3: ROTACION
    # Patron identico al codigo de referencia:
    #   a) El planeta rota alrededor del sol (pivote externo = centro sol)
    #   b) La luna rota alrededor del planeta (pivote interno = centro planeta)
    #      El pivote interno (planeta) ya fue trasladado arriba, por lo que
    #      la luna hereda automaticamente el movimiento orbital del planeta.
    # ===================================================================

    # a) Planeta orbita alrededor del sol
    angulo_planeta = sistema["angulo_planeta"]
    sistema["planeta_x"], sistema["planeta_y"] = rotar_vertice(
        px, py, sx, sy, angulo_planeta
    )

    # b) Luna orbita alrededor del planeta
    #    Se usa la nueva posicion del planeta como pivote
    angulo_luna = sistema["angulo_luna"]
    sistema["luna_x"], sistema["luna_y"] = rotar_vertice(
        lx, ly,
        sistema["planeta_x"], sistema["planeta_y"],
        angulo_luna
    )


# ===========================================================================
# PUNTO DE ENTRADA
# ===========================================================================

if __name__ == "__main__":
    ventana = iniciar_ventana()

    # -----------------------------------------------------------------------
    # Estado inicial del sistema solar
    # Todas las posiciones, radios y parametros de animacion en un solo lugar
    # -----------------------------------------------------------------------
    sistema = {
        # Posicion inicial del sol (centro del sistema)
        "sol_x"          :  0.0,
        "sol_y"          :  0.0,
        "sol_radio"      :  0.14,       # Radio inicial del sol

        # Posicion inicial del planeta (a la derecha del sol)
        "planeta_x"      :  0.35,
        "planeta_y"      :  0.0,

        # Posicion inicial de la luna (a la derecha del planeta)
        "luna_x"         :  0.45,
        "luna_y"         :  0.0,

        # Radios orbitales (solo para dibujar las trayectorias de referencia)
        "orbita_planeta" :  0.35,       # Distancia sol-planeta
        "orbita_luna"    :  0.10,       # Distancia planeta-luna

        # TRASLACION: velocidad de desplazamiento del sistema por frame
        "traslacion_tx"  :  0.0015,

        # ESCALADO: estado del pulso del sol
        "pulso_dir"      :  1,          # 1 = creciendo, -1 = reduciendose

        # ROTACION: angulos incrementales por frame
        "angulo_planeta" :  1.2,        # Grados por frame (orbita del planeta)
        "angulo_luna"    : -3.5,        # Grados por frame (orbita de la luna, sentido inverso)
    }

    # Estrellas de fondo: posiciones fijas calculadas con distribucion
    # trigonometrica para que no sean completamente aleatorias
    # Se generan usando sin/cos para distribuirlas de forma organica
    estrellas = []
    for i in range(80):
        angulo = 2.0 * math.pi * i / 80
        dist   = 0.3 + 0.6 * math.sin(i * 1.7) * math.cos(i * 0.9)
        ex     = dist * math.cos(angulo + i * 0.4)
        ey     = dist * math.sin(angulo + i * 0.4)
        # Solo agregar si cae dentro del espacio visible
        if -1.0 < ex < 1.0 and -1.0 < ey < 1.0:
            estrellas.append(ex)
            estrellas.append(ey)

    # Bucle principal
    while not glfw.window_should_close(ventana):
        dibuja(sistema, estrellas)
        glfw.swap_buffers(ventana)
        glfw.poll_events()
        glfw.wait_events_timeout(0.016)

    glfw.terminate()
