#Juego de adivinar un numero
numeroPersona = 0
numero = 7

#Le pedimos a la persona que adivine el numero

while numeroPersona != numero:
    numeroPersona = int(input("Adivina el numero guardado en memoria: "))
    #Evaluamos las opciones
    if numeroPersona > numero:
        print("El numero que has ingresado es mayor que al que debes encontar!")
    elif numeroPersona < numero:
        print("El numero que has ingresado es menor que al que debes encontar!")

print("Correcto, has adivinado el numero!")
        
