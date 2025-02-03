# Crie uma classe ItemEstoque com os seguintes atributos: nome, quantidade e preco_unitario.
# Adicione os métodos:
# adicionar_estoque(quantidade) para aumentar o estoque.
# remover_estoque(quantidade) para reduzir o estoque, verificando a quantidade disponível.
# calcular_valor_total() que retorna o valor total do estoque.

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, unidades):
        if unidades <= self.estoque:
            self.estoque -= unidades
            print(f"{unidades} unidades vendidas.")
        else:
            print(f"Não há {unidades} unidades em estoque.")

    def repor(self, unidades):
        if unidades <= self.estoque:
            self.estoque += unidades
            print(f"{unidades} unidades repor.")
        else:
            print(f"Há {unidades} unidades em estoque.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self.estoque}")

Produto1 = Produto("Camiseta", 29.99, 10)
Produto1.exibir_informacoes()
Produto1.vender(5)
Produto1.repor(5)


Produto2 = Produto("Calça", 59.99, 5)
Produto2.exibir_informacoes()
Produto2.vender(3)
Produto2.repor(2)


Produto3  = Produto("Tênis", 99.99, 3)
Produto3.exibir_informacoes()
Produto3.vender(2)
Produto3.repor(1)


Produto4 = Produto("Bermuda", 39.99, 8)
Produto4.exibir_informacoes() 
Produto4.vender(4)
Produto4.repor(3)