print("====================================================================")
print( "1. La lista de ventas original.")
print("====================================================================")
# Lista de diccionarios llamada 'ventas'
ventas = [
    { "fecha": "2024-01-01", "producto": "Televisor", "cantidad": 2, "precio": 450.99 },
    { "fecha": "2024-01-01", "producto": "Reloj inteligente", "cantidad": 4, "precio": 199.99 },
    { "fecha": "2024-01-01", "producto": "Auriculares", "cantidad": 10, "precio": 49.99 },
    { "fecha": "2024-01-01", "producto": "Consola de videojuegos", "cantidad": 1, "precio": 400.00 },
    { "fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1200.50 },
    { "fecha": "2024-01-02", "producto": "Smartphone", "cantidad": 5, "precio": 299.99 },
    { "fecha": "2024-01-02", "producto": "Cámara", "cantidad": 1, "precio": 599.99 },
    { "fecha": "2024-01-02", "producto": "Monitor", "cantidad": 3, "precio": 250.00 },
    { "fecha": "2024-01-03", "producto": "Smartphone", "cantidad": 3, "precio": 699.99 },
    { "fecha": "2024-01-03", "producto": "Tablet", "cantidad": 3, "precio": 199.95 },
    { "fecha": "2024-01-03", "producto": "Impresora", "cantidad": 2, "precio": 150.00 },
    { "fecha": "2024-01-03", "producto": "Teclado", "cantidad": 5, "precio": 49.99 },
    { "fecha": "2024-01-04", "producto": "Auriculares", "cantidad": 10, "precio": 49.99 },
    { "fecha": "2024-01-04", "producto": "Bicicleta", "cantidad": 1, "precio": 350.00 },
    { "fecha": "2024-01-04", "producto": "Ratón", "cantidad": 8, "precio": 25.00 },
    { "fecha": "2024-01-04", "producto": "Altavoces", "cantidad": 4, "precio": 100.00 },
    { "fecha": "2024-01-05", "producto": "Televisor", "cantidad": 2, "precio": 450.99 },
    { "fecha": "2024-01-05", "producto": "Proyector", "cantidad": 1, "precio": 800.00 },
    { "fecha": "2024-01-05", "producto": "Estabilizador", "cantidad": 2, "precio": 120.00 },
    { "fecha": "2024-01-06", "producto": "Mochila para laptop", "cantidad": 3, "precio": 40.00 },
    { "fecha": "2024-01-06", "producto": "Laptop", "cantidad": 1, "precio": 1200.50 },
    { "fecha": "2024-01-06", "producto": "Smartwatch", "cantidad": 2, "precio": 150.00 },
    { "fecha": "2024-01-07", "producto": "Cámara", "cantidad": 1, "precio": 599.99 },
    { "fecha": "2024-01-07", "producto": "Altavoces", "cantidad": 4, "precio": 100.00 },
    { "fecha": "2024-01-07", "producto": "Bicicleta", "cantidad": 1, "precio": 350.00 },
    { "fecha": "2024-01-07", "producto": "Ratón", "cantidad": 8, "precio": 25.00 },
    { "fecha": "2024-01-08", "producto": "Teclado", "cantidad": 5, "precio": 49.99 },
    { "fecha": "2024-01-08", "producto": "Smartphone", "cantidad": 3, "precio": 699.99 },
    { "fecha": "2024-01-08", "producto": "Televisor", "cantidad": 2, "precio": 450.99 },
    { "fecha": "2024-01-12", "producto": "Laptop", "cantidad": 1, "precio": 1200.50 },
    { "fecha": "2024-01-12", "producto": "Smartphone", "cantidad": 15, "precio": 299.99 },
    { "fecha": "2024-01-12", "producto": "Cámara", "cantidad": 11, "precio": 599.99 },
    { "fecha": "2024-01-12", "producto": "Monitor", "cantidad": 13, "precio": 250.00 },
    { "fecha": "2024-01-13", "producto": "Smartphone", "cantidad": 13, "precio": 699.99 },
    { "fecha": "2024-01-23", "producto": "Tablet", "cantidad": 13, "precio": 199.95 },
    { "fecha": "2024-01-23", "producto": "Impresora", "cantidad": 12, "precio": 150.00 },
    { "fecha": "2024-01-23", "producto": "Teclado", "cantidad": 15, "precio": 49.99 },
    { "fecha": "2024-01-24", "producto": "Auriculares", "cantidad": 5, "precio": 49.99 },
    { "fecha": "2024-01-14", "producto": "Bicicleta", "cantidad": 4, "precio": 350.00 },
    { "fecha": "2024-01-14", "producto": "Ratón", "cantidad": 3, "precio": 25.00 },
    { "fecha": "2024-01-14", "producto": "Altavoces", "cantidad": 7, "precio": 100.00 }
]

# Imprimir la lista para verificar
for venta in ventas:
    print(venta)

print()
print("====================================================================")
print("2. Los ingresos totales generados.")
print("====================================================================")
# Inicializar variable para el total de ingresos
ingresos_totales = 0.0

# Iterar sobre la lista de ventas
for venta in ventas:
    # Calcular ingresos para cada venta
    ingresos_venta = venta["cantidad"] * venta["precio"]
    # Sumar al total
    ingresos_totales += ingresos_venta

# Imprimir el total de ingresos
print("Los ingresos totales generados por todas las ventas son: ${:.2f}".format(ingresos_totales))

print()
print("====================================================================")
print("3. El producto más vendido y su cantidad total vendida.")
print("====================================================================")
# Diccionario para acumular las ventas por producto
ventas_por_producto = {}

# Iterar sobre la lista de ventas
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    # Acumular la cantidad vendida en el diccionario
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

# Identificar el producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# Imprimir el producto más vendido y la cantidad total vendida
print(f"El producto más vendido es '{producto_mas_vendido}' con una cantidad total de {cantidad_mas_vendida}.")


"""
"""
print()
print("====================================================================")
print("4. El precio promedio de venta por producto.")
print("====================================================================")
# Diccionario para acumular la suma de precios y la cantidad vendida por producto
precios_por_producto = {}

# Iterar sobre la lista de ventas
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    # Calcular el total y la cantidad en el diccionario
    if producto in precios_por_producto:
        total_precio, total_cantidad = precios_por_producto[producto]
        precios_por_producto[producto] = (total_precio + (precio * cantidad), total_cantidad + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

# Calcular el precio promedio de venta por producto
precios_promedio = {}
for producto, (total_precio, total_cantidad) in precios_por_producto.items():
    precio_promedio = total_precio / total_cantidad
    precios_promedio[producto] = precio_promedio

# Imprimir el precio promedio por producto
for producto, promedio in precios_promedio.items():
    print(f"El precio promedio de '{producto}' es: {promedio:.2f}")


"""
"""
print()
print("====================================================================")
print("5. Los ingresos totales por día.")
print("====================================================================")
# Diccionario para almacenar los ingresos totales por día
ingresos_por_dia = {}

# Iterar sobre la lista de ventas
for venta in ventas:
    fecha = venta["fecha"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    # Calcular el ingreso total de esta venta
    ingreso_total = cantidad * precio
    
    # Acumular el ingreso en el diccionario
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso_total
    else:
        ingresos_por_dia[fecha] = ingreso_total

# Imprimir los ingresos totales por día
for fecha, ingreso in ingresos_por_dia.items():
    print(f"Ingresos del día {fecha}: {ingreso:.2f}")

"""

"""    
print()
print("====================================================================")
print("6. El resumen de ventas por producto.")
print("====================================================================")
# Diccionario para almacenar el resumen de ventas
resumen_ventas = {}

# Iterar sobre la lista de ventas
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    # Si el producto no está en el resumen, inicializarlo
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": 0,
            "ingresos_totales": 0.0,
            "precio_promedio": 0.0
        }
    
    # Acumular la cantidad total y los ingresos totales
    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += cantidad * precio

# Calcular el precio promedio para cada producto
for producto, datos in resumen_ventas.items():
    cantidad_total = datos["cantidad_total"]
    if cantidad_total > 0:
        datos["precio_promedio"] = datos["ingresos_totales"] / cantidad_total

# Imprimir el resumen de ventas
print(f"Producto \t Cantidad Total \tIngresos Totales \tPrecio Promedio")
for producto, datos in resumen_ventas.items():
    """
    print(f"Producto: {producto}")
    print(f"  Cantidad Total: {datos['cantidad_total']}")
    print(f"  Ingresos Totales: {datos['ingresos_totales']:.2f}")
    print(f"  Precio Promedio: {datos['precio_promedio']:.2f}\n")
    """
    print(f"{producto}\t{datos['cantidad_total']}\t{datos['ingresos_totales']}\t{datos['precio_promedio']:.2f}")
