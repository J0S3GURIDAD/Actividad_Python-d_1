# Pregunta si una persona terminó su tarea. Si no terminó, mostrar "Debes terminar la tarea".

tarea = input("¿Terminaste tu tarea? (si/no): ")
if tarea == "no":
    print("Debes terminar la tarea")
else:
    print("Puedes salir a jugar")