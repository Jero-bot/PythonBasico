listOfNames = ["Jeronimo", "Daniel", "Maria", "Charles"] # listaCombinada = ["Carola", 123, -67, "Luigi", ["Elemento dentro de una lista"]]
print(listOfNames)

for name in listOfNames: #Ejemplo de imprimir un elemento de una lista
    print(name)


listOfNumbers = [10, 45, -5, 20, 28.5] #Ejemplo de como imprimir los numeros mayores a 15 de una lista
for number in listOfNumbers:
    if number > 15:
        print(number)

countryList = ["colombia", "uruguay", "España", "Alemania"] 
print(countryList[0])

for position, country in enumerate(countryList): #Ejemplo de como imprimir un elemento y su respectivo indice
    print(position, country)

#Ejemplo de matrix
matrix = [[1, 26, 3],[4, 8, 6],[7, 2, 45.6]]

for row in matrix: #(row: fila) (matrix: una lista de listas)
    print(row)
    for number in row:
        if number > 6: #Imprimimos los numeros mayores a 6 de cada fila -> (row)
            print(number)
