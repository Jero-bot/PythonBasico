#Pedirle al usuario los ingresos
ingresos = float(input("Por registre los ingresos de la empresa: "))

#Pedirle al usario los costos
costos = float(input("Por favor ingrese los costos de la empresa: "))

#Calcular la utilidad bruta (ingresos - costos)
utilidadBruta = (ingresos - costos)
print(f"la utilidad bruta es de: {utilidadBruta}$")

#Pedirle al usuario los gastos
gastos = int(input("Por favor ingrese los gastos de la empresa: "))

#Calcular la utilidad operativa (utilida bruta - gastos)
utilidadOperativa = (utilidadBruta - gastos)
print(f"la utilidad operativa es de {utilidadOperativa}$")

#Calcular el impuesto a la renta del 30% (utilidad operativa * 30%)
impuestoRenta = (utilidadOperativa * 30) / 100 
print(f"El impuesto a la renta es de {impuestoRenta}$")

#Calcular utilidad neta (utilidad operativa - impuesto a la renta)
utilidadNeta = (utilidadOperativa - impuestoRenta)
print(f"la utilidad neta es de {utilidadNeta}$")