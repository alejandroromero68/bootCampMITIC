"""
Multiplica por 2: crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos, desde el 0 hasta el número proporcionado como entrada.
Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]
correccion: el 7 no puee ser porque no es un valor resultante de multiplicar por 2
"""
print("Crea el archivo un Python llamado funciones_basicas_2.py")
print()
print("Crea la función multiplica_por_dos(num)")

def multiplica_por_2(n):
    # Crea una lista con los números multiplicados por 2
    return [i * 2 for i in range(n + 1)]

# Ejemplo de uso
resultado = multiplica_por_2(5)
print(resultado)  # $ python funciones_basicas_2.py: [0, 2, 4, 6, 8, 10]

"""
Suma y resta: crea una función que reciba una lista con dos números. Imprime la suma de los dos números y regresa la resta de los dos números.
Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
"""
print()
print("Crea la función suma_y_resta(lista)")
def suma_y_resta(numeros):
    # Sumar los dos números
    suma = sum(numeros)
    print(suma)  # Imprimir la suma
    
    # Calcular la resta
    resta = numeros[0] - numeros[1]
    return resta  # Regresar la resta

# Ejemplo de uso
resultado = suma_y_resta([5, 4])
print("La resta es:", resultado)  # # $ python funciones_basicas_2.py: 9 La resta es: 1

"""
Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
"""
print()
print("Crea la función sumatoria_menos_longitud(lista)")
def sumatoria_menos_longitud(numeros):
    # Calcular la sumatoria de los números en la lista
    sumatoria = sum(numeros)
    # Calcular la longitud de la lista
    longitud = len(numeros)
    # Regresar la sumatoria menos la longitud
    return sumatoria - longitud

# Ejemplo de uso
resultado = sumatoria_menos_longitud([1, 2, 3, 4])
print("El resultado es:", resultado)  # Salida: El resultado es: 6

"""
Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]
"""
print()
print("Crea la función valores_multiplicados_segundo(lista)")
def valores_multiplicados_segundo(numeros):
    # Imprimir la longitud de la lista original
    print(len(numeros))
    
    # Verificar si la lista tiene menos de 2 elementos
    if len(numeros) < 2:
        return []  # Regresar lista vacía
    
    # Obtener el segundo número
    segundo_numero = numeros[1]
    
    # Crear una nueva lista con los valores multiplicados por el segundo número
    nueva_lista = [numero * segundo_numero for numero in numeros]
    
    # Regresar la nueva lista
    return nueva_lista

# Ejemplo de uso
resultado1 = valores_multiplicados_segundo([1, 3, 5, 7])
print("Resultado:", resultado1)  # Salida: Resultado: [3, 9, 15, 21]

resultado2 = valores_multiplicados_segundo([1])
print("Resultado:", resultado2)  # Salida: Resultado: []

"""
Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]
"""
print()
print("Crea la función valor_multiplicado_longitud(valor, longitud)")

def valor_multiplicado_longitud(valor, longitud):
    # Crear una lista cuyo tamaño sea igual a la longitud
    # y cuyos valores sean igual a longitud multiplicada por valor
    lista_resultado = [valor * longitud for _ in range(longitud)]
    
    return lista_resultado

# Ejemplos de uso
resultado1 = valor_multiplicado_longitud(5, 2)
print("Resultado:", resultado1)  # Salida: Resultado: [10, 10]

resultado2 = valor_multiplicado_longitud(7, 5)
print("Resultado:", resultado2)  # Salida: Resultado: [35, 35, 35, 35, 35]
