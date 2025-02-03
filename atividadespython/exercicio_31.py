# Crie uma classe Livro com os atributos titulo, autor e ano_publicacao.
# Adicione um método verificar_antiguidade(ano_atual) que retorna se o livro é considerado antigo (mais de 50 anos).
# Use __str__ para exibir as informações do livro.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def verificar_antiguidade(self, ano_atual):
        if ano_atual - self.ano_publicacao > 50:
            return True
        return False

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Ano de Publicacao: {self.ano_publicacao}"

livro1 = Livro("O Senhor dos Aneis", "JRR Tolkien", 1954)
print(livro1)

ano_atual = 2023
if livro1.verificar_antiguidade(ano_atual):
    print("Livro antigo")
else:
    print("Livro novo")

livro2 = Livro("O Hobbit", "JRR Tolkien", 1937)
print(livro2)

ano_atual = 2023
if livro2.verificar_antiguidade(ano_atual):
    print("Livro antigo")
else:
    print("Livro novo")

    