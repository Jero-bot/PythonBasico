# ejercicio 3: preguntar el total de una compra. 
# Si el valor es mayor a 100.000, dar un descuento del 10%

valorCompra = int(input("Por favor ingrese el total de la compra: "))

if valorCompra > 100000:
    descuento = (valorCompra * 10 / 100)
    print(f"El descuento de su compra es: {descuento}")
else:
    descuento = 0
    
totalFinal = (valorCompra - descuento)
print(f"El total de la compra es de: {totalFinal}$")

