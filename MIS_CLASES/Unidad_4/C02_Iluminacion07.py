""" EJEMPLO OPTIMIZADO PARA EL USO DE LAS LUCES.

    Este código solo muestra la función no está completo.

    Casos de Uso Comunes para el manejo de mas luces:
    -------------------------------------------------
    ESCENARIO DE VIDEOJUEGO:
        glEnable(GL_LIGHT0)  # Sol/luz ambiente
        glEnable(GL_LIGHT1)  # Linterna del jugador (foco)
        glEnable(GL_LIGHT2)  # Lámparas estáticas
        glEnable(GL_LIGHT3)  # Efectos especiales (explosiones, etc.)

    ESCENA DE INTERIOR:
        glEnable(GL_LIGHT0)  # Luz general del techo
        glEnable(GL_LIGHT1)  # Lámpara de mesa
        glEnable(GL_LIGHT2)  # Pantalla de computadora
        glEnable(GL_LIGHT3)  # Luz de ventana

    EFECTOS ESPECIALES:
        glEnable(GL_LIGHT0)  # Luz base
        glEnable(GL_LIGHT1)  # Luz roja intermitente (alarma)
        glEnable(GL_LIGHT2)  # Luz azul (neón)
        glEnable(GL_LIGHT3)  # Luz verde (radioactivo)


        
        
    Solo activar las luces que se requieren en el momento
    Usar valores por defecto cuando sea posible
    Luces secundarias posicionales (requieren menos computo)        

    Evitar efectos costosos si no son necesarios
        glLightf(luz, GL_SPOT_CUTOFF, 180.0)  # No usar foco
        glLightf(luz, GL_QUADRATIC_ATTENUATION, 0.0)  # No usar atenuación compleja
"""


def configurar_luces_optimizadas():
    """Configuración eficiente de múltiples luces"""
    
    # Solo activar las luces que realmente necesitas
    luces_activas = [GL_LIGHT0, GL_LIGHT1, GL_LIGHT2]  # Solo 3
    
    for luz in luces_activas:
        glEnable(luz)
        
        # Usar valores por defecto cuando sea posible
        if luz == GL_LIGHT0:
            # Luz principal - direccional (más eficiente)
            glLightfv(luz, GL_POSITION, [0, 1, 0, 0.0])
        else:
            # Luces secundarias - posicionales
            glLightfv(luz, GL_POSITION, [x, y, z, 1.0])
        
        # Evitar efectos costosos si no son necesarios
        # glLightf(luz, GL_SPOT_CUTOFF, 180.0)  # No usar foco
        # glLightf(luz, GL_QUADRATIC_ATTENUATION, 0.0)  # No usar atenuación compleja

