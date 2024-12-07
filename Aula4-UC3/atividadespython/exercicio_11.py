# Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário.

def calcular_irpf(salario):
    # Definindo as faixas de salário e suas respectivas alíquotas
    if salario <= 1903.98:
        return 0  # Isento
    elif salario <= 2826.65:
        return (salario - 1903.98) * 0.075
    elif salario <= 3751.05:
        return (salario - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075
    elif salario <= 4664.68:
        return (salario - 3751.05) * 0.225 + (3751.05 - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075
    else:
        return (salario - 4664.68) * 0.275 + (4664.68 - 3751.05) * 0.225 + (3751.05 - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075

def main():
    # Leitura do salário
    salario = float(input("Digite o salário do funcionário: R$ "))
    
    # Calcular o IRPF
    irpf = calcular_irpf(salario)
    
    # Exibir o valor do imposto a ser descontado
    print(f'O valor do Imposto de Renda a ser descontado é: R$ {irpf:.2f}')
    
# Chama a função principal
main()

