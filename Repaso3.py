# Un programa pide la edad de una persona. Si es mayor de 18, puede votar.

edad = int(input("¿Cuál es tu edad? "))
if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")