# Escreva um programa que receba três números inteiros e determine qual deles é o maior.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: ")) 

if num1 > num2 and num1 > num3:
    print(f"O primeiro número ({num1}) é o maior.")
elif(num2 > num1 and num2 > num3):
    print(f"O segundo número ({num2}) é o maior.")
else:
    print(f"O terceiro número ({num3}) é o maior.")
