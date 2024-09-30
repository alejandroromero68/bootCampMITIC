#1

def cantidad_de_vocales():
    return 5

print(cantidad_de_vocales())
## retorn valor 5


#2
def cantidad_de_glaciares_argentina():
    return 16968

#print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())
## da error, falta las comillas al string y convertir a str el retorno de la funcion

print("cantidad_de_dias_o_meses_o_semanas_en_anio(): " + str(cantidad_de_glaciares_argentina()))
## retorna 16968


#3
def anio_independencia_chile():
    return 1810
    return 1851

print(anio_independencia_chile())
## retorna 1810, ya alli termina la funcion, pues, retorna antes de la ejecucion de la siguiente linea.

#4
def cantidad_de_departamentos_colombia():
    return(32)
    print(33)

print(cantidad_de_departamentos_colombia())
## retonr 32, misma situacion del ejercio anterior, la funcion termina en la sentencia return, no ejecuta mas siguiente instruccion
#5
def altura_machu_picchu():
    print(2438)

x = altura_machu_picchu()
print(x)
## salida en pantalla, 2438, esto lo imprime en la funcion, pero lueguo retorna none, y lo imprime tambien 


#6
def suma(a, b):
    print(a+b)

print(suma(10, 5) + suma(4, 3))
## imprime 15 y 7, luego da error 

def suma(a, b):
    return a + b  # Cambiar print por return

resultado = suma(10, 5) + suma(4, 3)  # Sumar los resultados
print(resultado)  # Imprimir el resultado total
## esto imprimira 22

#7
def concatenar(a, b):
    return str(b) + str(a)

print(concatenar(7, 15))
## retorna e imprime 157  (concateno string de 15 mas string de 7)

#8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21

print(paises_latinoamerica_o_lenguas_indigenas())
## salida por pantalla: 560 y 46


#9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52

print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
## salida por pantalla 365, 12 y 377 ==>  (a < b), (a > b) y ((a < b) + (a > b))

#10
def sumatoria(a, b):
    return a + b
    return 157

print(sumatoria(3, 4))
## 7 (a+b) alli termina la funcion

#11
a = 150
print(a)

def funcion():
    a = 350
    print(a)

print(a)
funcion()
print(a)
## la salida por pantalla 1) 150,  2) 150, 3) 350 y 150  

#12
a = 150
print(a)

def funcion():
    a = 350
    print(a)
    return a

print(a)
funcion()
print(a)
## la salida por pantalla 1) 150,  2) 150, 3) 350, 4) 350 y 5) 150  

#13
a = 150
print(a)

def funcion():
    a = 350
    print(a)
    return a

print(a)
a = funcion()
print(a)
## la salida por pantalla 1) 150,  2) 150, 3) 350, 4) 350 


#14
def funcion1():
    print(3)
    funcion2()
    print(2)

def funcion2():
    print(1)

funcion1()
## Salida por pantalla: 3, 1, 2

#15
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4

def funcion2():
    print(1)
    return 0

b = funcion1()
print(b)

## 3,1,0,4
