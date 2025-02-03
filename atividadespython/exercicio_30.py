# Crie uma classe Produto com os atributos nome, codigo e preco.
# Adicione um método especial __str__ para exibir os detalhes do produto e um método para aplicar desconto (aplicar_desconto(percentual)).

class Produto:
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco  

    def __str__(self):
        return f"Nome: {self.nome}, Codigo: {self.codigo}, Preço: R${self.preco:.2f}"

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        return self.preco

produto1 = Produto("Produto 1", 123, 10.99)
print(produto1)
print(f"Preço com desconto: R${produto1.aplicar_desconto(10):.2f}")

produto2 = Produto("Produto 2", 456, 19.99)
print(produto2)
print(f"Preço com desconto: R${produto2.aplicar_desconto(15):.2f}")

produto3 = Produto("Produto 3", 789, 29.99)
print(produto3)
print(f"Preço com desconto: R${produto3.aplicar_desconto(20):.2f}")