# Escreva um programa que receba 10 números inteiros e conte quantos deles são pares.

num = 0
par = 0

for i in range(0, 10):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        par += 1

print(f"Quantidade de números pares: {par}")
