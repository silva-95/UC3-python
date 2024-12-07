# Escreva um programa que exiba a tabuada de multiplicação de um número digitado pelo usuário, de 1 a 10.

# num = int(input("Digite um número inteiro: "))
# for i in range(0, 11):
#     print(f"{num} x {i} = {num * i}")

def tabuada():
    num = int (input("Digite um número inteiro: "))
    print(f"Tabuada de {num}:")
    for i in range(11):
        print(f"{num} x {i} = {num * i}")

tabuada()

