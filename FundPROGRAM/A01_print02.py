""" Ejercicios de prueba para evaluar la funcion print()

    10 Ejercicios de Programación en Python (Solo con print())
    Ejercicios, ordenados de menor a mayor complejidad, que solo requieren el 
    uso de la función print() para resolverlos.

    Consejo para el Alumno
    Recuerde a su alumno que, aunque se sienta limitado al principio, dominar el output (print()) es crucial. 
    Todos los programas, sin importar lo complejos que sean, usan esta función para mostrar sus resultados o 
    para depurar errores. ¡Es la primera forma en que el programa "habla" con el mundo! 
"""


# NIVEL BASICO: IMPRIMIR TEXTO Y CARACTERES

""" 1) Saludo Simple: Escribe un programa que imprima en la pantalla el mensaje: 
"¡Hola, Python! Estoy listo para programar. """ 

print("¡Hola, Python! Estoy listo para programar")    
    
    
""" 2) Información Personal: Imprime en tres líneas diferentes tu nombre completo, 
       tu ciudad favorita (por ejemplo, Acapulco), y el año actual.
       (El alumno debe usar print() tres veces, o usar el caracter de nueva línea \n 
       dentro de una sola llamada a print()). """

# Solucion 1
print("Javier\nAcapulco\n2025")

# Solución 2
print('Javier')
print('Acapulco')
print(2025)


""" 3) Dibujo de Caracteres (Bandera): Utiliza solo asteriscos (*) y espacios para 
       imprimir un pequeño cuadrado de 5X5 en la consola.

       Ejemplo esperado:
        *****
        *   *
        *   *
        *   *
        ***** """

print('*****')
print('*   *')
print('*   *')
print('*   *')
print('*****')


# NIVEL INTERMEDIO: FORMATO Y ARGUMENTOS DE PRINT

""" 4) Separadores Personalizados: Imprime la palabra "CODIGO" y los números 1,2,3 en 
       una sola línea utilizando una sola llamada a print(), pero asegúrate de que 
       estén separados por el símbolo de pipe (|). 
       (Debe usar el argumento sep de la función print()). """

print('CODIGO',123,sep='|')


""" 5) Pausar la Línea: Imprime las palabras "PRUEBA" y "COMPLETA" en la misma línea, 
       pero la palabra "PRUEBA" debe terminar sin un salto de línea.
       (Debe usar el argumento end de la función print()). """

print("PRUEBA ", end="")
print("COMPLETA")

""" 6) Dibujo de Caracteres (Triángulo): Imprime un triángulo rectángulo usando el símbolo 
       de almohadilla (#), de la siguiente manera:

       Ejemplo esperado:
        #
        ##
        ###
        ####
        ##### """

print("#")
print("##")
print("###")
print("####")
print("#####")


""" 7) Operación Básica Impresa: Imprime el resultado de la siguiente operación matemática: 
       (100 - 50) X 2
       (El alumno debe incluir la operación directamente dentro de la función print() para 
       que Python la evalúe e imprima el resultado: print((100 - 50) * 2)).
"""
print((100 - 50) * 2 )


# NIVEL AVANZADO: CADENAS LARGAS Y ESCAPE.

""" 8)Cita Famosa: Imprime la siguiente cita, incluyendo las comillas dobles, en una sola línea.
        "La mejor manera de predecir el futuro es creándolo."

       (Debe usar comillas simples para la cadena o usar el carácter de escape \" para incluir 
       las comillas dobles). """

# Solución 1
print('"La mejor manera de predecir el futuro es creándolo."')

# Solución 2
print("\"La mejor manera de predecir el futuro es creándolo.\"")


""""   9) Tabla Sencilla: Imprime los siguientes encabezados y datos usando tabulaciones (\t) 
       para que parezca una tabla rudimentaria: "Nombre", "Edad", "Ciudad". Luego, imprime tus 
       propios datos debajo, alineándolos con los encabezados.
        Ejemplo esperado:

        Nombre	Edad	Ciudad
        Carlos	30	Acapulco """

print('Nombre\tEdad\tCiudad')
print('Carlos\t30\tAcapulco')

""" 10) Líneas Múltiples: Imprime el siguiente poema o fragmento de código exactamente como se muestra, 
    incluyendo los saltos de línea, utilizando una sola llamada a print().

    Primer verso
    Un poco de
    espacio
    Tercer verso
    (Debe usar cadenas de texto de múltiples líneas (triple comilla doble o sencilla) o usar el caracter 
    de nueva línea \n varias veces).
"""

# Solución 1
print("""Primer verso
Un poco de
espacio
Tercer verso
(Debe usar cadenas de texto de múltiples líneas (triple comilla doble o sencilla) o usar el caracter 
de nueva línea \n varias veces). """)

# Solución 2
print('''Primer verso
Un poco de
espacio
Tercer verso
(Debe usar cadenas de texto de múltiples líneas (triple comilla doble o sencilla) o usar el caracter 
de nueva línea \n varias veces). ''')

# Solución 3
print('print("""Primer verso\nUn poco de\nespacio\nTercer verso\n')

