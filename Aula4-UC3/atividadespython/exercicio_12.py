# Crie um programa que calcule o valor total de uma compra feita em várias parcelas. Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.

soma = 0
num_parcelas = int(input("Digite o número de parcelas: "))
valor_parcela = float(input("Digite o valor de cada parcela: "))

for i in range(1, num_parcelas + 1):
    soma += valor_parcela

if soma > 1000:
    soma *= 1.05    

print(f"O valor total das parcelas é: R$ {soma:.2f}")

