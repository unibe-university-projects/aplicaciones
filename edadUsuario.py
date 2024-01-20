#escribir un programa que que pregunte la edad y muestre en pantalla si la edad es mayor a 18 años o es menor

edad = 0 

edad = int(input("\n Ingrese su edad"))

if edad >= 18:
    print('el usuario es mayor de edad')
else:
    print('el usuario es menor de edad')