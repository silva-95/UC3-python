# Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

pessoa1 = Pessoa("Maria", 25)
pessoa1.exibir_informacoes()

pessoa2 = Pessoa("Joaquim", 30)
pessoa2.exibir_informacoes()

pessoa3 = Pessoa("Jorge", 35)
pessoa3.exibir_informacoes()

pessoa4 = Pessoa("Fernando", 40)
pessoa4.exibir_informacoes()

