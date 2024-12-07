# Crie uma função cumprimentar que receba o nome e a hora do dia, e retorne uma mensagem personalizada. Bom dia, Boa tarde ou Boa noite.

def cumprimentar(nome: str, hora: int):
    if hora < 12:
        return f"Bom Dia, {nome}!"
    elif hora <= 18:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"


nome = input("Digite seu nome: ")
hora = int(input("Digite a hora do dia: "))
print(cumprimentar(nome, hora))

