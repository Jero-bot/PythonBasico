#Paso 1: Pedir el total de la factura
totalFactura = int(input("Por favor ingrese el total de la factura: "))

#Paso2: pedir el porcentaje de propina que se quiere entregar
porcentajePropina = int(input("Por favor ingrese el porcentaje de propina que desea entregar: "))

#Paso 3: calcular el valor del IVA del 19%
valorIVA = totalFactura * 19 / 100

#Paso 4: calcular el subtotal (total de la factura - valor del IVA)
subtotal = totalFactura - valorIVA

#Paso 5: calcular el valor de la propina (subtotal * propina / 100)
valorPropina = subtotal * porcentajePropina / 100

#Paso 6: mostrar el resultado
print(f"El valor total de la factura fue {totalFactura}$")
print(f"El valor del IVA fue {valorIVA}")
print(f"El subtotal fue de  {subtotal}$")
print(f"El valor de la propina fue {valorPropina}$")
print(f"El valor total de la compra mas la propina {totalFactura + valorPropina}$")
