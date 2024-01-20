valor = 0
operador = ''
valor2 = 0
i = 0
x = 2
oper = ['+', '-', '+','/']

msg = 'Esta es una calculadora'

#valor = int(input("\n Ingrese el valor [1]"))
#operador = input("\n Ingrese el operador")
#valor2 = int(input("\n Ingrese el valor[3]"))



#print(result)

while i < x:
    valor = int(input("\n Ingrese el valor [1]"))
    operador = input("\n Ingrese el operador")
    valor2 = int(input("\n Ingrese el valor[3]"))
    if operador == "+":
        result = valor + valor2
    elif operador == "-":
        result = valor - valor2
    elif operador == '*':
        result = valor * valor2
    elif operador == '/':
        result = valor / valor2
    i += 1

while result != 0:
    if operador == '+':
        print(result)
print("Programa terminado")

#while i <= 10:
#    print(i)
#    i += 1
#print("Programa terminado")


#while i <= 10:
#    print(i)
#    i *= 2
#print("Programa terminado mult")

#while oper == operador.find("*") or oper:
#    print(oper.index('*'))

#print("Programa terminado")