# Implemente uma função que receba dois números e uma operação (+, -, *, /) e devolva o resultado.

def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Divisão inválida!"
    else:
        return "Resultado da operacao!"
    
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
print(calcular(num1, num2, operacao))


    