def pedir_numero(mensaje, tipo=float, minimo=0, maximo=None):
    while True:
        try:
            entrada = input(mensaje)
            numero = tipo(entrada)
            if numero < minimo:
                print("El número debe ser mayor o igual a", minimo)
            elif maximo is not None and numero > maximo:
                print("El número debe ser menor o igual a", maximo)
            else:
                return numero
        except ValueError:
            print("Por favor, introduce un número válido.")

# Pedir el nombre del producto
nombre = input("Nombre del producto: ")

# Pedir el precio unitario (debe ser número positivo)
precio = pedir_numero("Precio unitario: $", float, 0.01)

# Pedir la cantidad (debe ser un número entero mayor a 0)
cantidad = pedir_numero("Cantidad: ", int, 1)

# Pedir el descuento (debe estar entre 0 y 100)
descuento = pedir_numero("Descuento (%): ", float, 0, 100)

# Calcular el total sin descuento
subtotal = precio * cantidad

# Calcular cuánto se descuenta
rebaja = subtotal * (descuento / 100)

# Calcular el total final
total = subtotal - rebaja

# Mostrar resultados (sin concatenar)
print()
print("Producto:", nombre)
print("Subtotal: $", format(subtotal, ".2f"))
print("Descuento aplicado:", descuento, "%")
print("Total final: $", format(total, ".2f"))