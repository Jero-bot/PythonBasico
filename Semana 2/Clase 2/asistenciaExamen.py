#ejericio 5: mostrar si un estudiante está habilitado para presentar el examen
# si el estudiante fue a mas del 75% de las clases 
# puede hacer el examen
# si el estudiante fue a menos del 75% de las clases, solo puede hacer el examen si tiene excusa médica

totalClases = int(input("Por favor ingrese el total de las clases: "))
clasesAsisitidas = int(input("Por favor ingrese a cuantas clases asisitio el estudiante: "))

porcentajeAsistencia = clasesAsisitidas / totalClases 

if porcentajeAsistencia > 0.75: 
    print("Puede presentar el examen")
else:
    tieneExcusa = (input("¿Tiene excusa? ")).lower()
    if tieneExcusa == "si":
        print("Puede presentar el examen")
    else:
        print("No puede presentar el examen")
        
print("el porcentaje de asistencia del estudainte es {:.2f}%".format(porcentajeAsistencia * 100))