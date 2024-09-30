"""
Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
En ciudades, cambia “Cancún” por “Monterrey”
En las coordenadas, cambia el valor de “latitud” por 9.9355431
"""
print("1. Actualizar valores en diccionarios y listas")
print()

# Definición de la matriz
matriz = [[10, 15, 20], [3, 7, 14]]

# Definición de la lista de cantantes
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

# Definición del diccionario de ciudades
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

# Definición de las coordenadas
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Imprimir los resultados actualizados
print("Matriz original:", matriz)
print("Cantantes original:", cantantes)
print("Ciudades original:", ciudades)
print("Coordenadas original:", coordenadas)


# Cambiar el valor de 3 por 6 en la matriz
matriz[1][0] = 6  # Cambiando el valor de 3

# Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"  # Cambiando a "Enrique Martin Morales"

# Cambiar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"  # Cambiando "Cancún" por "Monterrey"

# Cambiar el valor de "latitud" por 9.9355431
coordenadas[0]["latitud"] = 9.9355431  # Cambiando la latitud

print()
print() 

# Imprimir los resultados actualizados
print("Matriz actualizada:", matriz)
print("Cantantes actualizado:", cantantes)
print("Ciudades actualizada:", ciudades)
print("Coordenadas actualizada:", coordenadas)

print()
print("2. Iterar a través de una lista de diccionarios")
print()
"""
2. Iterar a través de una lista de diccionarios
Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:
"""
def iterarDiccionario(lista):
    for diccionario in lista:
        # Usamos join para crear la salida en el formato deseado
        salida = ', '.join(f"{clave} - {valor}" for clave, valor in diccionario.items())
        print(salida)

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

"""
Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave 
y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario 
que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:
"""
print()
print("3. Obtener valores de una lista de diccionarios")
print("iterarDiccionario2(“nombre”, cantantes)")
print()
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:       # Verificamos si la llave existe en el diccionario
            print(diccionario[llave])  # Imprimimos el valor correspondiente a la llave

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario2("nombre", cantantes)

print()
print("Otro ejemplo: iterarDiccionario2(“pais”, cantantes)")
print()

def iterarDiccionario2_2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:       # Verificamos si la llave existe en el diccionario
            print(diccionario[llave])  # Imprimimos el valor correspondiente a la llave

# Ejemplo de uso
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamamos a la función para imprimir los países
iterarDiccionario2_2("pais", cantantes)

print()
print("4. Iterar a través de un diccionario con valores de lista")
print()

def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():    # Itera sobre cada clave y sus valores
        print(f"{len(valores)} {clave.upper()}")  # Imprime el tamaño de la lista y la clave en mayúsculas
        for valor in valores:                     # Itera sobre cada valor en la lista
            print(valor)                          # Imprime el valor
        print()
# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)
