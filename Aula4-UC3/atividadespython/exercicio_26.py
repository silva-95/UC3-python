# Implemente uma classe Carrinho com os seguintes métodos:
# adicionar_produto(nome, preco) para adicionar um produto ao carrinho.
# exibir_itens() para listar os produtos no carrinho.
# calcular_total() para exibir o valor total da compra.

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco):
        self.produtos.append({"nome": nome, "preco": preco})

    def exibir_itens(self):
        for produto in self.produtos:
            print(f"Nome: {produto['nome']}, Preco: {produto['preco']}")

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto["preco"]
        print(f"Total: {total}")


carrinho = Carrinho()
carrinho.adicionar_produto("Produto 1", 10.99)
carrinho.adicionar_produto("Produto 2", 19.99)
carrinho.exibir_itens()
carrinho.calcular_total()


