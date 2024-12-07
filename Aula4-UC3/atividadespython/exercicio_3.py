# A padaria Sópão vende diariamente uma certa quantidade de pães franceses e uma quantidade de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total arrecadado, 43% corresponde aos custos de fabricação. Do restante, Seu joão guarda 15% numa conta de poupança e 15% ele converte em Euros para sua viagem Anual. Sabe-se que 1 Euro custa R$ 4,60. Com base nestes fatos, faça um progrma para ler as quantidades de pães e de broas, calcular a venda total de pãos e broas, o custo de fabricação, quanto irá guardar na poupança e quantos euros irá comprar. Ao final exibir os dados calculados.


paozinho = float(input("Informe a quantidade de pães vendida: "))
broa = float(input("Informe a quantidade de broas vendida: "))

venda_total = (paozinho * 0.80) + (broa * 2.50)
custo_fabricacao = venda_total * 0.43
poupanca = (venda_total - custo_fabricacao) * 0.15
euros = (poupanca * 0.15) / 6.32

print(f"Venda total: R$ {venda_total:.2f}")
print(f"Custo de fabricação: R$ {custo_fabricacao:.2f}")
print(f"Poupança: R$ {poupanca:.2f}")
print(f"Comprará: £{euros:.2f} euros.")
