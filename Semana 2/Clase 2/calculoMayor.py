#  Pedirle al usuario dos valors numericos. Imprimir el mayor de ellos

numeroUno = int(input("Por favor ingrese el primer numero: "))

numeroDos = int(input("Por favor ingrese el segundo numero: "))

if numeroUno > numeroDos:
    print(f"el numero mayor es el: {numeroUno}")
elif numeroUno < numeroDos:
    print(f"el numero mayor es el: {numeroDos}")
else:
    print("Ambos numeros son iguales")
