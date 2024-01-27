# Se pide al estudiante que realice el siguiente programa en Pyhton 

# Crear una función según los comportamientos que tiene el vehiculo
# Les dejo clase principal con los parámetros que tiene le vehiculo 


class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        if not self.enmarcha:
            self.enmarcha = True
            print("El carro está en funcionamiento.")

    def acelerara(self):
        if self.enmarcha:
                velocidad_a_alcanzar = int(input("Ingrese la velocidad: "))
                if velocidad_a_alcanzar >= 0:
                    # debe mostrar el incremento
                    for i in range(velocidad_a_alcanzar):
                        print(i)

                    self.velocidad = velocidad_a_alcanzar
                    print(f"Ingrese la velocidad: {self.velocidad}")
                else:
                    print("la velocidad no debe ser 0 ")


    def frenara(self):
        if self.enmarcha and self.velocidad > 0:
            perdida_velocidad = int(input("Ingrese la velocidad de pérdida: "))
            if perdida_velocidad >= 0 and perdida_velocidad <= self.velocidad:
                self.velocidad -= perdida_velocidad 

                for i in range(perdida_velocidad) :
                    print(i)

                print(f"El vehículo está frenando. Velocidad actual: {self.velocidad}")
            else:
                print("La velocidad de pérdida debe ser menoar a la velocidad de incremento")

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nVelocidad actual: {self.velocidad}")



if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Corolla")

    vehiculo.arrancar()
    vehiculo.acelerara()
    vehiculo.frenara()
    vehiculo.estado()

# a partir de este clase crear los constructores de arrancar, acelerar, frenar. estado

# Arrancar: el vehiculo no se mueve, debe mostrar en pantalla el carro esta en funcionamiento
# Acelerar: el vehiculo se mueve, en este punto ingresar un valor por teclado para alcanzar la velocidad, y mostrar en pantalla.
# Frenar: el vehiculo se esta deteniendo, en este punto el vehiculo esta perdiendo valor de manera progresiva, debe mostrar en pantalla la velocidad de perdida
# Estado: es un constructor que va a devolver en patalla los datos globales de los constructores