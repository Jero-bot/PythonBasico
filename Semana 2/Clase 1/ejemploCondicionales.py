#Juego de adivinar un numero
numero = 7

#Le pedimos a la persona que adivine el numero
numeroPersona = int(input("Adivina el numero: "))

#Evaluamos las opciones
if numeroPersona == numero:
    print("¡Felicidades, has adivinado el numero!")
elif numeroPersona < numero:
    print("Fallaste, el numero que debes adivinar es mayor que el que ingresastte")
else:
    print("Fallaste, el numero que debes adivinar es menor que el que ingresaste ")