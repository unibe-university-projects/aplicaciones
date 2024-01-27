# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasena_correcta = 'steveen123'

while True:
    password = input("\nIngrese la contraseña: ")

    if password == contrasena_correcta:
        print('Contraseña correcta')
        break 
    else:
        print('Contraseña incorrecta')
