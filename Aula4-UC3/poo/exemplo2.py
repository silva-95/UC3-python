# Armazenado no banco de dados para uso futuro
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Carro: {self.modelo}, Ano: {self.ano}")

meu_carro = Carro("Civic", 2020)
meu_carro.exibir_informacoes() #   Saída: Carro: Civic, Ano: 2020

meu_carro1 = Carro("Elba", 1997)
meu_carro1.exibir_informacoes()

