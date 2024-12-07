# Faça um programa para calcular a quantidade de latas de tintas para pintar uma parede. O programa deverá solicitar ao usuário, a altura (float) e o comprimento(float) da parede. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 3,6 litros, que custam R$ 107,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math # Importando a biblioteca math para usar a funcao ceil matematicas e trigonometricas

altura = float(input('Informe a altura da parede em metros: '))
comprimento = float(input('Informe o comprimento da parede em metros: '))

area = altura * comprimento

litros_necessarios = area / 3

latas_necessarias = math.ceil(litros_necessarios // 3.6)  # Arredondando para cima

preco_total = latas_necessarias * 107

print(f'Quantidade de latas a serem compradas: {latas_necessarias}')
print(f'Preço total: R$ {preco_total:.2f}')
