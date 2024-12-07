# Um determinado prêmio de loteria saiu para um bolão de três amigos. Uma lei garante que todo prêmio de loteria deva pagar um imposto de 7% para os cofres estaduais. Do total descontado o imposto, os amigos irão dividir o prêmio da seguinte maneira:
# O primeiro ganhador recebera 46%;
# O segundo recebera 32%;
# O terceiro recebera o restante; Faça um programa que leia o valor total do prêmio, calcule o desconto, o valor que cada um tem direito e imprima o total do prêmio, o premio descontado o imposto e a quantia recebida por cada um dos ganhadores.


valor_total = float(input("Informe o valor total do prêmio: "))

# Calcula o valor descontado o imposto
imposto = valor_total * 0.07
premio_liquido = valor_total - imposto

# Calcula a quantia recebida por cada ganhador
primeiro_ganhador = premio_liquido * 0.46
segundo_ganhador = premio_liquido * 0.32
terceiro_ganhador = premio_liquido - (primeiro_ganhador + segundo_ganhador)

# Imprime os resultados
print(f"Total do prêmio: R$ {valor_total:.2f}")
print(f"Prêmio descontado o imposto: R$ {premio_liquido:.2f}")
print(f"Quantia recebida pelo primeiro ganhador: R$ {primeiro_ganhador:.2f}")
print(f"Quantia recebida pelo segundo ganhador: R$ {segundo_ganhador:.2f}")
print(f"Quantia recebida pelo terceiro ganhador: R$ {terceiro_ganhador:.2f}")
