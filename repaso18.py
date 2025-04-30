# Agregar un número en una posición específica.

numeros = [10, 20, 30, 40, 50]

numeros = int(input("Numero a incertar: "))
posicion = int(input("En que posicion (0 a 4): "))

numeros.insert(posicion, numeros)
print("Lista actualizada:", numeros)