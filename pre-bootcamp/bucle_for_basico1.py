# Codifica el ejercicio 1. Básico
for i in range(101):
    print(i)

# Codifica el ejercicio 2. Múltiples de 2
for i in range(2, 501, 2):
    print(i)    

# Codifica el ejercicio 3. Contando Vanilla Ice
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Codifica el ejercicio 4. Wow. Número gigante a la vista
def suma_pares():
    total_sum = sum(i for i in range(0, 500001, 2))
    return total_sum

# Llamar a la función e imprimir el resultado
resultado = suma_pares()
print(f"La suma de los números pares del 0 al 500,000 es: {resultado}")        

# Codifica el ejercicio 5. Regrésame al 3
for i in range(2024, 0, -3):
    print(i)

# Definir las variables
numInicial = 3
numFinal = 10
multiplo = 2

# Codifica el ejercicio 6. Contador dinámico
# Comenzar desde numInicial hasta numFinal y verificar los múltiplos
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)    