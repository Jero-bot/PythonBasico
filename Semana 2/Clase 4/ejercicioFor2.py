listOfGrades = [
    1.0,
    4.5,
    2.4,
    3.2,
    5.0,
    5.0,
    3.2,
    2.5,
    4.4,
    3.7,
    2.7,
    5.0,
    4.2,
    3.4,
    3.9,
    1.6,
    4.3,
    2.8,
    2.8,
    3.9   
]

contInsuficente = 0
contAceptable = 0 
contSobresaliente = 0

sumaInsuficiente = 0
sumaAceptable = 0
sumaSobresaliente = 0


for grade in listOfGrades:
    if grade < 3:
        contInsuficente = contInsuficente + 1
        sumaInsuficiente = sumaInsuficiente + grade
    elif grade >= 3 and grade < 4:
        contAceptable = contAceptable + 1
        sumaAceptable = sumaAceptable + grade
    else:
        contSobresaliente = contSobresaliente + 1
        sumaSobresaliente = sumaSobresaliente + grade


print(f"la cantidad de estudiantes con nota insuficientes es {contInsuficente}")
print(f"la cantidad de estudiantes con nota aceptable es {contAceptable}")
print(f"la cantidad de estudiantes con nota sobresaliente es {contSobresaliente}")

print(f"la sumatoria de las notas de los estudiantes con nota insuficiente es {sumaInsuficiente}")
print(f"la sumatoria de las notas de los estudiantes con nota aceptable es {sumaAceptable}")
print(f"la sumatoria de las notas de los estudiantes con nota sobresaliente es {sumaSobresaliente}")



print(f"el promedio de los estudiantes con nota insuficiente es {sumaInsuficiente / contInsuficente}")
print(f"el promedio de los estudiantes con nota aceptable es {sumaAceptable / contAceptable}")
print(f"el promedio de los estudiantes con nota sobresaliente es {sumaSobresaliente / contSobresaliente}")