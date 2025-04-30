# Pide una nota (0-10). Muestra si pedio, aprobado o sobresaliente.

nota = float (input("Ingresa la nota:"))
if nota <5:
    print("Suspenso")
elif nota >=5 and nota <7:
    print("Aprobado")
elif nota >=7 and nota <9:
    print("Sobresaliente")
else:
    print("Matrícula de honor")