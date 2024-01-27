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




def contar_letras(frase, letra):
    count = 0
    for char in frase:
        if char == letra:
            count += 1
    return count

def main():
    frase = input("\nIngrese la frase: ")
    letra = input("\nIngrese la letra: ")

    resultado = contar_letras(frase, letra)

    print(f"\nLa letra '{letra}' aparece {resultado} veces en la frase '{frase}'.")

if __name__ == "__main__":
    main()





class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.velocidad = 0

    def arrancar(self):
        if not self.enmarcha:
            self.enmarcha = True
            print("El vehículo está en funcionamiento.")

    def acelerar(self):
        if self.enmarcha:
            try:
                velocidad_aceleracion = float(input("Ingrese la velocidad de aceleración: "))
                self.velocidad += velocidad_aceleracion
                print(f"El vehículo está acelerando a {self.velocidad} km/h.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

    def frenar(self):
        if self.enmarcha:
            try:
                velocidad_frenado = float(input("Ingrese la velocidad de frenado: "))
                if velocidad_frenado <= self.velocidad:
                    self.velocidad -= velocidad_frenado
                    print(f"El vehículo está frenando. Velocidad actual: {self.velocidad} km/h.")
                else:
                    print("Error: La velocidad de frenado no puede ser mayor que la velocidad actual.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nVelocidad: {self.velocidad} km/h")

# Ejemplo de uso:
if __name__ == "__main__":
    vehiculo_ejemplo = Vehiculo("Toyota", "Corolla")

    vehiculo_ejemplo.arrancar()
    vehiculo_ejemplo.acelerar()
    vehiculo_ejemplo.frenar()
    vehiculo_ejemplo.estado()
