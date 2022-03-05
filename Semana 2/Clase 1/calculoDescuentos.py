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

totalCompra = totalHuevos + totalArepas


#Imprimimos los resultados
print(f"El total de los huevos es de: {totalHuevos}")
print(f"El total de las arepas es de: {totalArepas}")
print(f"El total de la compra es: {totalCompra}$")
