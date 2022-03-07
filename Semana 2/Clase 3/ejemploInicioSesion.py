maxRetries = 3
storePassword = "jeroo"

# Pedirle al usario que ingrese su contraseña
userPassword = input("Ingresa la contraseña: ")
cont = 0

# Si la contraseña coincide con storePassword, mostrarle un mensaje de inicio de sesion correcto
# Si la contraseña no coincide, mostrarle un error y pedirle la contraseña nuevamente
while storePassword != userPassword and cont < maxRetries:
    print("las contraseñas no coinciden")
    cont += 1 #cont + 1
    print(f"valor del contador {cont}")
    userPassword = input("Ingresela nuevamente: ")

if storePassword != userPassword and cont == maxRetries:
    print("Su cuenta ha sido bloqueada temporalmente, intente de nuevo en 5 minutos")
elif storePassword == userPassword:
    print("Inicio de sesion correcto")
