numero1 = 70     # asignacion de valor numerico entero a la variable numero1
numero2 = 3.14   # asignacion de valor numerico float a la variable numero2
booleano = False # asignacion de bool false a la variable booleano
cadena = 'Hola Mundo'  # asignacion de string a la variable cadena
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']
# asigna una lista de valores string a la lista ingredientes_pastel
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}
# asigna valor a persona (diccionario)  clave:valor
frutas = ('guayaba', 'fresa', 'papaya')
# asigna valor a la tupla frutas.
print(type(frutas))  # imprime el tipo de variables... seria tuple
print(ingredientes_pastel[2])  # imprime el valor de la posicion 2 de la lista ingredientes:pastel
ingredientes_pastel.append('Mantequilla') # agrega un valor a la lista ingrediente, seria el 5to elemento
print(persona['nombre']) # imprime el valor que contiene la clave nombre del dicionario persona
persona['nombre'] = 'Kevin'  # modifica el valor de la clave nombre del diccionario persona
persona['color_ojos'] = 'cafe' # agrega la clave color_ojos con su valor al diccionario persona
print(frutas[2]) # imprime el valor del elemento numero 2 de la tupla frutas

if numero1 > 45:          # evalua si el valor de la variable numero1 es mayor a 45
    print("Numero mayor") # imprime Numero mayor
else:                     # sino
    print("Numero menor") # imprime Numero menor

if len(cadena) < 5:       # evalua la longitud de la variable cadena si es menor a 5(cantidad de elementos del string cadena)
    print("Cadena corta") # imprime Cadena corta
elif len(cadena) > 15:    # evalua si la longitud de la variable cadena es mayor a 15 (cantidad de elementos del string cadena)
    print("Cadena larga") # imprime Cadena larga
else:                         # sino
    print("Cadena perfecta")  # imprime Cadena perfecta

for x in range(8):   # recorre desde 0 a 7 (8-1 )
    print(x)         # imprime valor de la variable x (0..7)
for x in range(2,8): # recirre desde 2 hasta 7
    print(x)         # imprime valor de la variable x (2..7)
for x in range(2,8,2): # recorre desde 2 hasta 7, incrementado de a 2
    print(x)           # imprime 2,4,6
x = 0                  # asigna valor 0 a la variable numerica x
while(x < 8):          # mientras x sea menor a 8 (repetir)
    print(x)           # imprime valor de la variable x (0..7)
    x += 1             # suma el valor 1 a la variable x

ingredientes_pastel.pop() # elimina el ultimo valor de la lista ingredientes_pastel (Mantequilla) y devuelve el valor de la lista eliminada (Mantequilla)
ingredientes_pastel.pop(1) # elimina el elemento de la posicion 1 de la lista y lo devuelve Leche

print(persona)   # imprime los valores del diccionario persona
persona.pop('color_ojos') # elimina la clave color_ojos del diccionario persona
print(persona)   # imprime los valores el diccionario persona

for ingrediente in ingredientes_pastel:   # recorre elementos de  lista ingredientes pastel (3, 4 o 5 dependiente se se corre la sentencia pop)
    if ingrediente == 'Harina':    # ['Harina', 'Vainilla', 'Chocolate'] esto queda despues de hacer 1 append y 2 pop
        continue                   # continua en la linea for si se cuemple la condicion que el elemento se igual a Harina
    print('Después de la primera sentencia') # imprime Despues de la primera sentencia
    if ingrediente == 'Chocolate': # evalua si ingrediente (variable) es igual a Chocolate
        break                      # si se cumple el valor = Chocolate, corte el loop del ciclo for.

def imprime_hola_10_veces():    # define nombre de funcion imprime_hola_10_veces
    for numero in range(10):    # dentro de la funcion, realiza un bucle - ciclo de rango 0 a 9, osea 10 veces iniciando en 0-9
        print('Hola')           # imprime hola

imprime_hola_10_veces()         # llama a la ejecucion a la funcion imprime_hola_10_veces

def imprime_hola_n_veces(n):    # define la funcion imprime_hola_n_veces (n recibe como parametro)
    for numero in range(n):     # ciclo de 0 a valor n (recibido como parametro)
        print('Hola')           # imprime Hola

imprime_hola_n_veces(5)         # llama a la funcion imprime_hola_n_veces (5 envia como parametro)

def imprime_hola_n_o_diez_veces(n = 10): # define la funcion imprime_hola_n_o_diez_veces (n recibe como parametro o 10 sin no viene valor)
    for numero in range(n):              # ciclo de 0 a valor n (recibido como parametro o 10 sino viene como parametro)
        print('Hola')                    # imprime Hola

imprime_hola_n_o_diez_veces()            # llama a la funcion imprime_hola_n_o_diez_veces( )  no envia ningun parametro
imprime_hola_n_o_diez_veces(5)           # llama a la funcion imprime_hola_n_o_diez_veces( 5 )  envia valor 5 como parametro


"""                                       inicio de comentario multiple lineas
Sección BONUS                             comentario Seccion BONUS
"""                                     # Final de comentarios multiples lineas

# print(numero3)                        # imprime variable numero3... en este caso va dar error, porque aun no se inicializa
# numero3 = 86                          # Inicializa/asigna valor 86 a la variable numero3
# frutas[0] = 'naranja'                 # modifica el valor del elemento 0 de la lista frutas. (definirlo como lista para que funcione. en el codigo esta como tupla)--> frutas = ['guayaba', 'fresa', 'papaya']
# print(persona['hobbies'])             # imprime el valor asociado con la clave 'hobbies' en el diccionario persona. (aun no asignada en nuestro codigo)
# print(ingredientes_pastel[11])        # intenta imprimir el elemento en el índice 11 de la lista ingredientes_pastel. No tenemos ese elemento en nuestro codigo
# print(booleano)                       # se utiliza para imprimir el valor de una variable llamada booleano. False segun nuestro codigo
# frutas.append('manzana')              # se utiliza para agregar el elemento 'manzana' al final de la lista llamada frutas.
# frutas.pop(1)                         # elimina el elemento 1 de la lista de frutas.