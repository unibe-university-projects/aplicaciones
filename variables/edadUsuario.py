#escribir un programa que que pregunte la edad y muestre en pantalla si la edad es mayor a 18 años o es menor

age = 0 

#$age = int(input("\n Ingrese su edad"))

if age >= 18:
    print('el usuario es mayor de edad')
else:
    print('el usuario es menor de edad')

# escribir una funcion que muestre por pantalla que muestre el menjsae 'muestre amigo'
    
def hallo():
    print('muestre amigo')

#hallo()

## escriba una funcion que calcule el total de una factura tras aplicar el iva la funcion debe recibir la cantidad sin iva y el % de iva a aplicar,
# devulver el total de la factura.
# si se invica la funcion sin pasar el % de iva, e debera aplicar el 21%

def factura(cantidad: int, iva = 21):
    return cantidad+ cantidad*iva/100

#print(factura(300))
#print(factura (200, 10))


# destro de una funcion que calcule el area del circulo  y otra que calcula el area de un volumen cilindro de la otra fduncion

pi = 3.14

def areaCirculo(radio):
    return pi * radio**2

def cilindro(radio, alto):
    return areaCirculo(radio) * alto

#print(areaCirculo(300))
print(cilindro(3,5) )

