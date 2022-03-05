# Precio base de los huevos: 1.800
# Precio de base de las arepas: 5000
# Si alguien compra mas de 10 canastas, el precio es de 1000

# Si alguien compra mas de 10 canastas de huevos y ademas compra 10 paquetes de arepas ->
# El precio de los huevos es 1000 y el de las arepas 2000

# Paso 1: Preguntarle al usuario cuantos huevos quiere comprar
cantidadHuevos = int(input("Ingrese la cantidad de canastas de huevos que quiere comprar: "))

# Paso 2: Preguntarle al usuario si quiere comprar arepas
quiereArepas = input("¿Quieres comprar arepas?: ").lower()

# Paso 3: Si la persona quiere arepas, preguntar cuantas 
cantidadArepas = 0
if quiereArepas == "si":
    cantidadArepas = int(input("Ingrese la cantidad de arepas quiere comprar: "))

# Paso 4: Calcular el total de la compra
precioHuevos = 1800
precioArepas = 5000 

if cantidadHuevos > 10:
    precioHuevos = 1000

if cantidadHuevos > 10 and cantidadArepas > 10:
    precioHuevos = 800
    precioArepas = 2000

totalHuevos = (cantidadHuevos * precioHuevos)

totalArepas = (cantidadArepas * precioArepas)

subTotal = totalHuevos + totalArepas

#Imprimimos los resultados
print(f"El total de los huevos es de: {totalHuevos}")
print(f"El total de las arepas es de: {totalArepas}")
print(f"El total de la compra es de: {subTotal}$")

#Condiciones adicionales que se deben cumplir:
#1. Si el total de la compra es mayor a 50.000, y solo estoy comprando un producto, dar un descuento adicional del 10%
if subTotal > 50000 and (cantidadHuevos == 0 or cantidadArepas == 0):
    descuento = subTotal * 10 / 100
    totalCompra = subTotal - descuento
    print(f"El descuento de la compra es de {descuento}")
    print(f"El precio final de la compra con el 10% de descuento es de: {totalCompra}")
#2. Si el total de la compra es mayor a 50.000 y 
# además se están comprando huevos y arepas, el descuento no es 10% sino que es 15%
elif subTotal > 50000 and(cantidadHuevos > 0 and cantidadArepas > 0):
    descuento = subTotal * 15 / 100
    totalCompra = subTotal - descuento
    print(f"El descuento de la compra es de {descuento}")
    print(f"El precio final de la compra con el 15% de descuento es de: {totalCompra}")


# Mostrarle al usuario el total de la compra y también el total del descuento