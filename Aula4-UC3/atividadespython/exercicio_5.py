# Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. Exiba a soma de todos os números positivos digitados.

soma = 0
numero = 0
while numero >= 0:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    

print(f"A soma dos números positivos digitados é: {soma}")

