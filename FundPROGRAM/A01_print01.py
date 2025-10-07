""" Es ente ejercico aprenderemos el uso de la funcion print()"""

# Print se usa para mostrar informacion en la consola
# Podemos mostrar textos envolviendo el texto en comillas simples o dobles
# solo debemos ser consistentes en el uso de las comillas
# si iniciamos con comillas simples debemos terminar con comillas simples
# si iniciamos con comillas dobles debemos terminar con comillas dobles
# Tambien es importante señalar que los textos se conocen como cadenas de caracteres o strings
# y siempre deberan ir entre comillas simples o dobles.

print("Hola Mundo")     # Podemos usar comillas dobles
print('Hola Mundo')     # Podemos usar comillas simples

# podemos combinar comillas simples y dobles
print("La pelicula se llama 'Stars Wars'")   # Podemos usar comillas simples dentro de comillas dobles, resulta  Hola 'Mundo'
print('La pelicula se llama "Stars Wars"')   # Podemos usar comillas dobles dentro de comillas simples, resulta  Hola "Mundo"

print('Este es el resultado cuando usamos la coma en print:')
print('H'+"o"+'l'+"a"+' '+"M"+'u'+"n"+'d'+"o")  # Podemos concatenar caracteres para formar una cadena de texto


# Podemos usar la coma para separar caracteres y formar una cadena de texto, 
# esto agrega un espacio entre cada caracter
print('H','o','l','a',' ','M','u','n','d','o')  


# tambien podemos usar comillas triples para textos largos
print("""Este es un ejemplo de un texto largo
      donde requerimos del uso de varias 'lineas'
      podemos apreciar que el texto comienza
      con las triples comillas "dobles"
      y de esta forma se puede capturar
      un texto largo de varias lineas  """)   # Podemos usar comillas triples para textos largos

print('''Este es un ejemplo de un texto largo
donde requerimos del uso de varias "lineas"
podemos apreciar que el texto comienza
con las triples comillas 'simples'
y de esta forma se puede capturar
un texto largo de varias lineas  ''')   # Podemos usar comillas triples para textos largos


# Como escapar caracteres especiales
print('El caracter de comilla simple se escapa asi: \' ')
print("El caracter de comilla doble se escapa asi: \" ")
print("El caracter de diagonal invertida se escapa asi: \\ ")
print("El caracter de salto de linea se escapa asi: \n ")

# Imprimimos varias lineas usando \n (salto de linea o nueva linea)
print('Linea 1\nLinea 2\nLinea 3')

# impresion de tabulaciones usando \t
print('Impresion con tabulaciones:')
print('A\tB\tC')
print('D\tE\tF')
print('G\tH\tI')


print('Barra Normal: /')
print('Barra Invertida: \\')


# Podemos insertar saltos de linea en un texto usando \n
print("Este es otro ejemplo de un texto largo\n"\
"pero en este caso estamos usando la comilla doble'\n"\
"sin embargo estamos partiendo la linea en varias mas\n "\
"haciendo uso del caracter de salto de linea y la diagonal invertidacomillas \"dobles\"\n "\
"y de esta forma se puede capturar\n un texto largo de varias lineas  ")


# Podemos mostrar el resultado de operaciones matematicas
print("\nEl resultado de las siguientes operaciones matematicas es:")
print(2 + 2)
print(3 * 5)
print(10 / 2)
print(10 - 3)


# podemos mostrar la concatenacion de textos
print("\nHola" + " " + "Mundo")
print("El resultado de 2 + 2 es: ", 2 + 2 )
print("El resultado de 3 * 4 es: ", 3 * 4 )
print("El resultado de 10 / 2 es: ", 10 / 2 )
print("El resultado de 10 - 3 es: ", 10 - 3 )

