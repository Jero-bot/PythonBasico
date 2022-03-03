#Paso 1: Preguntarle al usuario el total de la factuta
totalFactura = int(input("Por favor ingrese el total de su factura: "))

#Paso 2: Pedirle al usario el valor que quiere dar de propina
valorPropina = int(input("Por favor ingrese el valor que quiere dar de propina: "))

#Paso 3: Hacer el calculo de la propina
propina = (totalFactura * valorPropina) / 100

#Paso 4: Mostrarle al usario el valor de la propina
print(f"el total de la propina es de: {propina} $")