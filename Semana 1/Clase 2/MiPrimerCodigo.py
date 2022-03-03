#imprimir mensaje en la terminal
print("Esto es un mensaje")

#imprimir varios mensajes en una sola linea
print("Hola mundo,", "soy programador,", "este es otro mensaje")

#Declaracion de variables y operaciones aritmeticas basicas
variable1 = 50
variable2 = "Hola"
variable3 = 24
variable4 = "Mundo"
numeroLetra = "100"
numeroLetra2 = "60"

#se realiza la suma entre variables
variable5 = variable1 + variable3
print(variable5)

#concatenacion de textos
print(variable2 + variable4)

#Se convierte (numeroLetra) a int y se hace la suma
print(variable1 + int(numeroLetra))

#En este codigo estamos calculando la diferencia de edad de acuerdo a las variables
diferencia = "la diferencia entre las edades es: " + str(variable1 - variable3) + " años"
print(diferencia)

#En estas lineas estamos calculando la diferencia de edad usando el comando especial f(format)
diferencia2 = f"La diferencia entre las edades es: {variable1 - variable3} años"
print(diferencia2)

#Sumamos dos numeros inicializados como str y luego los convertimos a enteros realizando la operacion
sumaNumerosLetras = int(numeroLetra) + int(numeroLetra2)
print("la suma es igual a", sumaNumerosLetras)