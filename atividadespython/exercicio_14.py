# Crie um programa que calcule o tempo restante até a aposentadoria de uma pessoa. Pergunte a idade e o tempo de contribuição (em anos). A pessoa pode se aposentar com 35 anos de contribuição ou 60 anos de idade. Mostre o tempo restante para a aposentadoria.

idade = int(input("Diga a idade: "))
contribuicao = int(input("Diga quantos anos contribuição: "))
if (idade >= 60) or (contribuicao >= 35):
    print("Já pode aposentar-se!")
else:
    aposentarI = 60-idade
    aposentarC = 35-contribuicao
print(f"Por Idade: {aposentarI} anos restantes")
print(f"Por Contrubuição: {aposentarC} anos restantes")
