#imprimir un texto simple
from __future__ import division


print("Hola, como estas?")

#imprimir varios textos separados por espacios
print("Palabra1", "palabra2")

#concatenar textos
primerTexto = "hola"
segundoTexto = "mundo"
holaMundo = primerTexto + " " + segundoTexto
print(holaMundo)

#formatear textos
miEdad = 20
print(f"yo tengo {miEdad} años")

#nombramiento de Variables

#manera 1: PascalCase
VariablePascalCase = "Variable con todas las iniciales mayusculas"

#manera 2: camelCase
variableCamelCase = "variable con su primer inicial en minuscula y el resto de iniciales en mayuscula"

#manera 3: snake_case

variable_snake_case = "variable con sus palabras separadas por un _"


#operaciones aritmeticas
edadUno = 80
edadDos = 50

#Operacion de suma
SumaDeEdad = edadUno + edadDos
print(SumaDeEdad)

#Operacion de resta
diferenciaDeEdad = edadUno - edadDos
print(diferenciaDeEdad)

#Operacion de multiplicacion
numeroUno = 40
numeroDos = 20

multiplicacion = numeroUno * numeroUno
print(multiplicacion)

#Operacion de division
division = numeroUno / numeroDos
print(division) #No divivir por 0 porque sale un error

#Jerarquia de operaciones: potenciacion > multiplicacion y division > sumas y restas
variable1 = 10
variable2 = 20
variable3 = 50
variable4 = -10.1

#primero sumamos (variable1 + variable2) y luego lo dividimos entre el resultado de (variable3 - variable4)
operacionUno = (variable1 + variable2) / (variable3 - variable4)
print(operacionUno)

#comando de input general de tipo texto
inputDelUsuario = input("Por favor ingrese un valor: ")

#comando de input de tipo numerico
inputNumerico = int(input("Por favor ingrese un valor numerico: "))
