#Juego de adivinar un numero
numeroPersona = 0
numero = 7

#Le pedimos a la persona que adivine el numero

while numeroPersona != numero:
    numeroPersona = int(input("Adivina el numero: "))
    #Evaluamos las opciones
    if numeroPersona == numero:
        print("¡Felicidades, has adivinado el numero!")
    elif numeroPersona < numero:
        print("Fallaste, el numero que debes adivinar es mayor que el que ingresaste")
    else:
        print("Fallaste, el numero que debes adivinar es menor que el que ingresaste ")
