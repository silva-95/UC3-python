# Implemente uma classe chamada Produto com:
# Atributos: nome, preco e estoque.
# Um método chamado vender que reduz o estoque ao vender o produto, se houver unidades disponíveis.
# Um método chamado repor que aumenta o estoque ao receber novas unidades.

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
  

