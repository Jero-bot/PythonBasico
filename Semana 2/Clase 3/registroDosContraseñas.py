#Le pedimos al usario que ingrese su contraseña
contraseña = input("Por favor ingrese su contraseña: ")

#Le pedimos al usuario que confirme su contraseña
confirmarContraseña = input("Por favor confirme su contraseña: ")

while contraseña != confirmarContraseña:
    contraseña = input("Las contraseñas no coinciden, por favor vuelva a ingresarla: ")
    confirmarContraseña = input("Confirme la contraseña: ")

print("Registro finalizado con exito")


# Variante 2
# contraseñasIguales = False

# while contraseñasIguales == False:
#     contraseña = input("Por favor ingrese la contraseña: ")
#     confirmarContraseña = input("Por favor confirme la contraseña: ")
#     if contraseña == confirmarContraseña:
#         (contraseñasIguales == True)
#     else:
#         print("Las contraseñas no coinciden, ingrese nuevamente")

# print("Registro finalizado con exito")



# Variante 3
# while(input('Ingrese contraseña : ') != input('Confirme contraseña : ')):
#     print('\n Contraseñas diferentes \n')
    
# print('ingreso contraseña adecuada')


