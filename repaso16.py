#Buscar si un número existe en una lista y encontrar su posición.

numeros = [3, 6, 9, 12, 15]

buscando = int(input("Ingresa el número para buscar: "))

if buscando in numeros:
    posicion = numero.index(buscando)
    print(f"El número {buscando} se encuentra en la posición {posicion}.")

else:
    print(f"El número {buscando} no se encuentra en la lista.")