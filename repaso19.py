# Pide 5 números y crea una lista solo con los pares.

pares = []

for i in range(5):
    numero = int(input(f"Ingrese el numero {i +1}: "))
if numero % 2 == 0:
        pares.append(numero)
print(f"Números pares ingresado es: {pares}")