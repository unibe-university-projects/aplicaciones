# Se pide al estudiante que cree el siguiente programa con funciones o constructores en python 

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

#  Nota:

# Si el programa cumple todos los requerimientos obtendra la calificacion de 1, si cumple la mitad del comportamiento 0.5, caso contrario se calificará con cero a esta pregunta.


def letras(frase, letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
            print(contador)
    return contador

frase = input("\n Ingrese el frase [1]")
letra =  input("\n Ingrese letra [1]")

letras(frase,letra )

# debe c