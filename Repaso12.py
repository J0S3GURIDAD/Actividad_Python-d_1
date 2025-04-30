# Dada una lista de frutas, pide al usuario una fruta que quiera eliminar.

frutas = ["manzana", "manzana", "platano", "naranja", "arroz"]
print("Lista de frutas:", frutas)
eliniminar = input("¿Qué fruta quieres eliminar? ").lower()
if eliniminar in frutas:
    frutas.remove(eliniminar)
    print("Fruta eliminada. Lista actualizada:", frutas)