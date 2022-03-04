# Paso 1: Le pedimos al usario que ingrese su estatura
estatura = float(input("Por favor ingrese su estatura en m: "))

# Paso 2: Le pedimos al usario que ingrese su peso
peso = int(input("Por favor ingrese su peso en kg: "))

# Paso 3: Calcular el IMC aplicando la formula
imc = peso / (estatura ** 2)

# Paso 4: Mostramos el resultado del imc dependiendo del caso
if imc < 18.5:
    print(f"cuidado, Su peso es menor al normal. tu IMC es de {imc} kg/m2")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Su peso es normal. Tu IMC es de {imc} kg/m2")
elif imc >= 25.0 and imc <= 29.9:
    print(f"Su peso es superior al normal. Tu IMC es de {imc} kg/m2")
else:
    print(f"Cuidado, sufres de obesidad. Tu IMC es de {imc} kg/m2")