listOfNumbers = [-10, 50, 700, 9, 21,24.5]
print(len(listOfNumbers))

# cont = 0
# for element in listOfNumbers:
#     cont += 1

# print(F"El contador de elemntos que hay en la lista es {cont}")

suma = 0
for number in listOfNumbers:
    suma = suma + number
print(f"La suma de los elementos de la lista es {suma}")

print(f"El promedio de los datos es {suma / len(listOfNumbers)}")