# Considere que o preço da tarifa de energia é R$ 0,50 por kWh. Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%.

consumo = float(input("Digite o consumo de energia em kWh: "))

if consumo > 200:
    desconto = consumo * 0.10
    total = consumo * 0.50 - desconto
else:
    total = consumo * 0.50

print(f"O valor total a ser pago pela conta é: R$ {total:.2f}")

