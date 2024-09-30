# Solicitar al usuario que ingrese dos números
n1 = float(input("Ingrese el primer número (n1): "))
n2 = float(input("Ingrese el segundo número (n2): "))

# Realizar las operaciones matemáticas
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2

# Para evitar división por cero
if n2 != 0:
    division = n1 / n2
else:
    division = "Indefinida (división por cero no permitida)"

# Mostrar los resultados
print(f"La suma de {n1} y {n2} es: {suma}")
print(f"La resta de {n1} menos {n2} es: {resta}")
print(f"La multiplicación de {n1} por {n2} es: {multiplicacion}")
print(f"La división de {n1} entre {n2} es: {division}")

type(n1)
lista = [1,2,3,4,5,6]
print(lista)