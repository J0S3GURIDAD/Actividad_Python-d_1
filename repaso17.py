# Contar cuántas veces aparece un nombre en la lista.

nombres = ["Ana", "Luis","Ana", "Pedro", "Ana"]
nombre_buscado = input("Ingresa un nombre para contar: ")
cantidad = nombres.count(nombre_buscado)
print(f"El nombre {nombre_buscado} aparece {cantidad} veces.")