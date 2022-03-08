# Pedirle al usario la cantidad de personas a ingresar
# En un for pedir las edades de esas n personas
# Guardar las edades de esas personas en una lista
# Calcular el promedio de esas edades

contPersons = 0
sumAges = 0

numberOfPersons = int(input("Por favor ingrese la cantidad de personas: ")) #Le pedimos al usuario que ingrese la cantidad personas

listOfAges = []

for i in range(0, numberOfPersons): #Con este for recorremos la lista desde 0 hasta la cantidad de personas que ingrese el usuario
    listOfAges.append(int(input("Por favor ingrese la edad de la persona: "))) #Con .append ingresamos informacion a listOfAges
print(listOfAges)

average = sum(listOfAges) / len(listOfAges) #Calculamos el promedio
print(f"El promedio de las edades es {average}")